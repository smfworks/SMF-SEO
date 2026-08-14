#!/usr/bin/env python3
"""
SMF SEO+GEO — Setup Configuration Helper
Reads and writes config for the SMF SEO+GEO skill.
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
from datetime import datetime
from pathlib import Path

CONFIG_DIR = Path.home() / ".smf" / "skills" / "smf-seo-gee"
CONFIG_FILE = CONFIG_DIR / "config.json"

ALLOWED_ROOTS = frozenset({"organization", "brand", "preferences"})


def default_config() -> dict:
    return {
        "_schema_version": 1,
        "_setup_completed": False,
        "_setup_version": "1.0",
        "_created_at": None,
        "organization": {
            "domain": None,
            "name": None,
            "primary_services": None,
            "content_pillars": None,
            "target_audience": None,
            "audience_pain_points": None,
            "key_competitors": None,
            "existing_high_performing_content": None,
        },
        "brand": {
            "voice": None,
            "cta_style": None,
            "author_name": None,
            "author_credentials": None,
        },
        "preferences": {
            "default_word_count": 2000,
            "default_tone": "professional but approachable",
            "primary_platform": "google",
        },
    }


def ensure_config_dir():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    if not CONFIG_FILE.exists():
        save_config(default_config())
    return CONFIG_FILE


def load_config():
    ensure_config_dir()
    try:
        data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"corrupt config at {CONFIG_FILE}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"corrupt config at {CONFIG_FILE}: root must be an object")
    return data


def save_config(config):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(config, indent=2) + "\n"
    fd, tmp_name = tempfile.mkstemp(prefix="config.", suffix=".json", dir=str(CONFIG_DIR))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, CONFIG_FILE)
    except Exception:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)
        raise


def is_setup_complete():
    return bool(load_config().get("_setup_completed", False))


def mark_setup_complete():
    config = load_config()
    config["_setup_completed"] = True
    config["_created_at"] = datetime.now().isoformat()
    save_config(config)


def set_dotted_key(key: str, value: str) -> None:
    """Set organization.domain / brand.voice / preferences.default_word_count."""
    parts = [p for p in key.split(".") if p]
    if len(parts) != 2 or parts[0] not in ALLOWED_ROOTS:
        raise ValueError(
            f"refusing key {key!r}; use organization.*, brand.*, or preferences.*"
        )
    config = load_config()
    section = config.setdefault(parts[0], {})
    if not isinstance(section, dict) or parts[1] not in section:
        raise ValueError(f"unknown key: {key}")
    if parts[0] == "preferences" and parts[1] == "default_word_count":
        try:
            section[parts[1]] = int(value)
        except ValueError as exc:
            raise ValueError("preferences.default_word_count must be an integer") from exc
    else:
        section[parts[1]] = value
    save_config(config)


def update_organization(**kwargs):
    config = load_config()
    for key, value in kwargs.items():
        if key in config["organization"]:
            config["organization"][key] = value
    save_config(config)


def update_brand(**kwargs):
    config = load_config()
    for key, value in kwargs.items():
        if key in config["brand"]:
            config["brand"][key] = value
    save_config(config)


def update_preferences(**kwargs):
    config = load_config()
    for key, value in kwargs.items():
        if key in config["preferences"]:
            config["preferences"][key] = value
    save_config(config)


def get_organization():
    return load_config().get("organization", {})


def get_brand():
    return load_config().get("brand", {})


def get_preferences():
    return load_config().get("preferences", {})


def show_config():
    print(json.dumps(load_config(), indent=2))


def reset_config():
    if CONFIG_FILE.exists():
        CONFIG_FILE.unlink()
    ensure_config_dir()
    print("Config reset to defaults.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_config()
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == "show":
        show_config()
    elif cmd == "complete":
        mark_setup_complete()
        print("Setup marked as complete.")
    elif cmd == "reset":
        reset_config()
    elif cmd == "is-ready":
        print("yes" if is_setup_complete() else "no")
    elif cmd == "update-org":
        if len(sys.argv) >= 4:
            update_organization(**{sys.argv[2]: sys.argv[3]})
            print(f"Updated organization.{sys.argv[2]}")
        else:
            print("Usage: update-org <key> <value>")
    elif cmd == "update-brand":
        if len(sys.argv) >= 4:
            update_brand(**{sys.argv[2]: sys.argv[3]})
            print(f"Updated brand.{sys.argv[2]}")
        else:
            print("Usage: update-brand <key> <value>")
    elif cmd == "update-prefs":
        if len(sys.argv) >= 4:
            update_preferences(**{sys.argv[2]: sys.argv[3]})
            print(f"Updated preferences.{sys.argv[2]}")
        else:
            print("Usage: update-prefs <key> <value>")
    elif cmd == "get":
        if len(sys.argv) >= 3:
            section = sys.argv[2]
            config = load_config()
            if section == "org":
                print(json.dumps(config.get("organization", {}), indent=2))
            elif section == "brand":
                print(json.dumps(config.get("brand", {}), indent=2))
            elif section == "prefs":
                print(json.dumps(config.get("preferences", {}), indent=2))
            else:
                print(json.dumps(config.get(section, {}), indent=2))
        else:
            print("Usage: get <org|brand|prefs>")
    else:
        print(f"Unknown command: {cmd}")
        print("Commands: show, complete, reset, is-ready, update-org, update-brand, update-prefs, get")
