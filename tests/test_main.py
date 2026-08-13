from __future__ import annotations

import json
from pathlib import Path

import main as seo


def test_lookup_key_found_and_missing():
    cfg = {"organization": {"domain": "example.com"}}
    found, val = seo.lookup_key(cfg, "organization.domain")
    assert found is True
    assert val == "example.com"
    found, val = seo.lookup_key(cfg, "organization.missing")
    assert found is False
    assert val is None


def test_main_help():
    assert seo.main(["help"]) == 0


def test_main_unknown():
    assert seo.main(["nope"]) == 2


def test_main_get_missing(tmp_path: Path, monkeypatch):
    monkeypatch.setattr(seo, "load_config", lambda: {"organization": {}})
    monkeypatch.setattr(seo, "check_pro_subscription", lambda: True)
    assert seo.main(["get", "organization.domain"]) == 2


def test_main_get_value(tmp_path: Path, monkeypatch):
    monkeypatch.setattr(seo, "load_config", lambda: {"organization": {"domain": "x.test"}})
    monkeypatch.setattr(seo, "check_pro_subscription", lambda: True)
    assert seo.main(["get", "organization.domain"]) == 0


def test_main_status_unconfigured(monkeypatch, capsys):
    monkeypatch.setattr(seo, "load_config", lambda: {})
    monkeypatch.setattr(seo, "check_pro_subscription", lambda: True)
    assert seo.main(["status"]) == 0
    assert "not configured" in capsys.readouterr().out.lower()
