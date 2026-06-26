# Anti-Extremism Blocklist

This repository provides an automated, normalized blocklist of domains associated with far-right, extremist, and anti-semitic content.

The list is designed for use with filtering tools such as:

- [uBlock Origin](https://github.com/gorhill/uBlock)
- [LeechBlock NG](https://addons.mozilla.org/de/firefox/addon/leechblock-ng/)

---

## How it works

This repository is fully automated:

- A central `BlockList.txt` is used as the source of truth
- GitHub Actions periodically sync and normalize all entries
- Output files are generated automatically:
  - `uBlock.txt`
  - `LeechBlock.txt`
- Removed domains are automatically deleted on sync

---

## Features

- Strict domain normalization (no URLs, no paths)
- Automatic sorting and deduplication
- Subdomain support for broader blocking
- Fully automated CI pipeline
- Transparent change reporting (diff + logs)

---

## File Structure

BlockList.txt # Source list (normalized domains only)
uBlock.txt # uBlock Origin filters
LeechBlock.txt # LeechBlock rules
report.md # Auto-generated sync report


---

## Installation

### uBlock Origin

1. Install uBlock Origin
2. Open Dashboard → "My Filters"
3. Paste contents of `uBlock.txt`
4. Apply changes

---

### LeechBlock NG

1. Install LeechBlock NG
2. Create a block set
3. Add domains from `LeechBlock.txt`

Supported formats:
- `example.com`
- `*.example.com`

---

## Updates

- Automatic sync via GitHub Actions
- Runs on schedule
- Fully regenerated each run
- No manual editing of generated files

---

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md)

All contributions must follow strict formatting rules.

---

## License

This project is released into the public domain under the **Unlicense**.

See [LICENSE](./LICENSE).