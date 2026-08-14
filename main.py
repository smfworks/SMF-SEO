#!/usr/bin/env python3
"""
SMF SEO+GEO — Content Optimization Engine
Main entry point for smfw CLI integration.

Usage:
    python3 main.py                    # Check status / guide user
    python3 main.py configure          # Run setup wizard
    python3 main.py reconfigure        # Reset and run setup wizard
    python3 main.py status             # Check configuration status
    python3 main.py get <key>          # Get config value
    python3 main.py quick-test <kw>    # Quick SEO keyword test
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
shared_path = SCRIPT_DIR.parent / "shared"
bundled_auth = SCRIPT_DIR / "shared_auth.py"

HAS_AUTH = False
require_subscription = None
show_subscription_error = None

if bundled_auth.exists():
    sys.path.insert(0, str(SCRIPT_DIR))
    try:
        from shared_auth import require_subscription, show_subscription_error

        HAS_AUTH = True
    except ImportError:
        HAS_AUTH = False
elif shared_path.exists():
    sys.path.insert(0, str(shared_path))
    try:
        from smf_auth import require_subscription, show_subscription_error

        HAS_AUTH = True
    except ImportError:
        HAS_AUTH = False

scripts_path = SCRIPT_DIR / "scripts"
if scripts_path.exists():
    sys.path.insert(0, str(scripts_path))

try:
    from config_manager import (
        get_brand,
        get_organization,
        get_preferences,
        is_setup_complete,
        load_config,
        mark_setup_complete,
        reset_config,
        save_config,
    )
except ImportError:
    CONFIG_DIR = Path.home() / ".smf" / "skills" / "smf-seo-gee"
    CONFIG_FILE = CONFIG_DIR / "config.json"

    def load_config():
        if CONFIG_FILE.exists():
            return json.loads(CONFIG_FILE.read_text())
        return {}

    def is_setup_complete():
        return load_config().get("_setup_completed", False)

    def reset_config():
        if CONFIG_FILE.exists():
            CONFIG_FILE.unlink()

    def save_config(config):
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        CONFIG_FILE.write_text(json.dumps(config, indent=2))

    def get_organization():
        return load_config().get("organization", {})

    def get_brand():
        return load_config().get("brand", {})

    def get_preferences():
        return load_config().get("preferences", {})

    def mark_setup_complete():
        cfg = load_config()
        cfg["_setup_completed"] = True
        save_config(cfg)


SKILL_NAME = "smf-seo-gee"
MIN_TIER = "pro"
AUTH_REQUIRED = {"configure", "reconfigure"}


def lookup_key(config: dict, key: str):
    """Walk a dotted key. Returns (found, value). Missing keys are not {}."""
    cur = config
    for part in key.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return False, None
        cur = cur[part]
    return True, cur


def check_pro_subscription() -> bool:
    if os.environ.get("SMF_SEO_SKIP_AUTH") == "1":
        return True
    if not HAS_AUTH:
        print("Warning: Auth system not available, skipping subscription check")
        return True

    if require_subscription is None or show_subscription_error is None:
        print("Warning: Auth system not available, skipping subscription check")
        return True

    result = require_subscription(SKILL_NAME, MIN_TIER)
    if not result.get("valid"):
        print("SMF SEO+GEO — Pro Skill")
        print("=" * 40)
        show_subscription_error(result)
        return False
    return True


def run_wizard() -> int:
    wizard_path = SCRIPT_DIR / "scripts" / "setup_wizard.py"
    if not wizard_path.exists():
        print("Error: setup_wizard.py not found", file=sys.stderr)
        return 1
    completed = subprocess.run([sys.executable, str(wizard_path)], check=False)
    return completed.returncode


def show_status() -> None:
    config = load_config()
    if config.get("_setup_completed"):
        print("SEO+GEO is configured and ready.")
        org = config.get("organization", {})
        print()
        print(f"Domain: {org.get('domain', 'Not set')}")
        print(f"Organization: {org.get('name', 'Not set')}")
        print(f"Content pillars: {org.get('content_pillars', 'Not set')}")
        print()
        brand = config.get("brand", {})
        print(f"Brand voice: {brand.get('voice', 'Not set')}")
        print(f"Author: {brand.get('author_name', 'Not set')}")
    else:
        print("SEO+GEO is not configured.")
        print()
        print("Run 'python3 main.py configure' to set up.")


def quick_test(keyword: str) -> None:
    print(f"\nQuick SEO keyword analysis: {keyword}")
    print("=" * 50)
    print()
    print("This CLI does not scrape SERPs itself.")
    print("Use Hermes / OpenClaw web tools, then apply the SKILL.md workflow:")
    print(f'  Analyze the keyword "{keyword}" for SEO and GEO')


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        if is_setup_complete():
            print("SMF SEO+GEO")
            print()
            print("Usage:")
            print("  python3 main.py status")
            print("  python3 main.py configure")
            print("  python3 main.py quick-test <keyword>")
        else:
            print("Welcome to SMF SEO+GEO.")
            print()
            print("Run 'python3 main.py configure' to set up for your organization.")
        return 0

    cmd = args[0].lower()

    if cmd in AUTH_REQUIRED and not check_pro_subscription():
        return 1

    if cmd == "configure":
        return run_wizard()
    if cmd == "reconfigure":
        print("Resetting configuration...")
        reset_config()
        return run_wizard()
    if cmd == "status":
        try:
            show_status()
        except ValueError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 3
        return 0
    if cmd == "get":
        if len(args) < 2:
            print("Usage: get <key> (e.g., organization.domain)", file=sys.stderr)
            return 2
        try:
            found, val = lookup_key(load_config(), args[1])
        except ValueError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 3
        if not found:
            print(f"Key not found: {args[1]}", file=sys.stderr)
            return 2
        if isinstance(val, (dict, list)):
            print(json.dumps(val, indent=2))
        else:
            print(val)
        return 0
    if cmd == "update":
        if len(args) < 3:
            print("Usage: update <key> <value>", file=sys.stderr)
            return 2
        try:
            from config_manager import set_dotted_key

            set_dotted_key(args[1], args[2])
        except ValueError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 2
        print(f"Updated {args[1]}")
        return 0
    if cmd == "quick-test":
        keyword = " ".join(args[1:]) if len(args) > 1 else "your keyword"
        quick_test(keyword)
        return 0
    if cmd in {"help", "--help", "-h"}:
        print(__doc__)
        return 0

    print(f"Unknown command: {cmd}", file=sys.stderr)
    print("Usage: python3 main.py [configure|status|quick-test|get|help]", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
