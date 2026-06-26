<!-- omit in toc -->
# Contributing to Blocklist for Far-Right and Anti Semitic Websites


# Contributing to the Blocklist

First off, thanks for taking the time to contribute! ❤️

This project relies on **strictly normalized domain data** to ensure automation works correctly.

Invalid formatting will break generation pipelines.

---

## ⚠️ Core Rules

### 1. Domains only

✔ Correct:

example.com
sub.example.com


✘ Incorrect:

https://example.com
http://example.com/page
example.com/path


---

### 2. No paths or parameters

Do NOT include:
- `/path`
- `?query=`
- `#fragment`

---

### 3. One domain per line

No comments, metadata, or formatting.

---

### 4. Lowercase only

All domains must be lowercase.

---

## How to Contribute

### Option 1: Pull Request

1. Fork repository
2. Edit `BlockList.txt`
3. Ensure:
   - valid domain format
   - no duplicates
4. Submit PR

---

### Option 2: Issue Submission

If unsure:

- Open an issue
- Provide:
  - domain
  - reason for inclusion
  - optional source/context

---

## Validation Rules

Your contribution will be rejected if:

- URLs are submitted instead of domains
- formatting is invalid
- duplicates are intentionally added
- non-domain content is included

---

## Automated Processing

After merging:

- domains are normalized
- list is sorted automatically
- duplicates are removed
- outputs are regenerated via CI

---

## Review Process

All contributions are:

1. checked via GitHub PR template
2. validated during CI run
3. normalized automatically
4. merged only if clean

---

## Code of Conduct

Be factual and respectful.

Do not:
- spam entries
- submit unrelated domains
- break formatting intentionally

---

## License

By contributing, you agree that your changes are released under the same license (Unlicense).
