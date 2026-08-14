# Security

## What this repo does

A local CLI + skill prompt for SEO/GEO content planning. Config lives at
`~/.smf/skills/smf-seo-gee/config.json`.

## Known issues addressed in 0.2

- `shared_path` was referenced before assignment if the bundled auth file was missing (`NameError`).
- Wizard launch used `os.system` with a path interpolation. It now uses `subprocess.run([sys.executable, path])`.
- `get` treated missing keys as empty dicts. Missing keys now fail closed.

## Reporting

Open a private GitHub security advisory or email security@smfworks.com.

## Notes

- JWT verification requires `PyJWT` + `cryptography` if you use `shared_auth.py`.
- Do not commit live tokens. `~/.smf/token` stays on the operator machine.
- Pricing or subscription claims in older copies of this skill are not verified here and should not be repeated in public posts without confirmation.
