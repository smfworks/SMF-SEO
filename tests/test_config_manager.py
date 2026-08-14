from __future__ import annotations

import json
from pathlib import Path

import pytest

import config_manager as cm


@pytest.fixture
def isolated_config(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    cfg_dir = tmp_path / "cfg"
    cfg_file = cfg_dir / "config.json"
    monkeypatch.setattr(cm, "CONFIG_DIR", cfg_dir)
    monkeypatch.setattr(cm, "CONFIG_FILE", cfg_file)
    return cfg_file


def test_set_dotted_key_persists(isolated_config: Path):
    cm.ensure_config_dir()
    cm.set_dotted_key("organization.domain", "example.com")
    data = json.loads(isolated_config.read_text())
    assert data["organization"]["domain"] == "example.com"


def test_set_dotted_key_rejects_unknown(isolated_config: Path):
    cm.ensure_config_dir()
    with pytest.raises(ValueError, match="unknown key"):
        cm.set_dotted_key("organization.not_a_field", "x")
    with pytest.raises(ValueError, match="refusing"):
        cm.set_dotted_key("_setup_completed", "true")


def test_corrupt_config_raises(isolated_config: Path):
    isolated_config.parent.mkdir(parents=True, exist_ok=True)
    isolated_config.write_text("{not json")
    with pytest.raises(ValueError, match="corrupt"):
        cm.load_config()


def test_word_count_must_be_int(isolated_config: Path):
    cm.ensure_config_dir()
    with pytest.raises(ValueError, match="integer"):
        cm.set_dotted_key("preferences.default_word_count", "lots")
    cm.set_dotted_key("preferences.default_word_count", "1800")
    assert cm.load_config()["preferences"]["default_word_count"] == 1800
