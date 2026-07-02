# Pull Request Template

## Summary

Describe the purpose of this pull request.

Examples:

* Add new domains
* Remove incorrect domains
* Fix formatting
* Documentation improvements
* CI/workflow changes

---

## Type of Change

* [ ] Add domains
* [ ] Remove domains
* [ ] Update existing domains
* [ ] Documentation
* [ ] CI / GitHub Actions
* [ ] Other

---

## Domain Changes

If this PR adds or removes domains, list them here.

Added:

*

Removed:

*

---

## Verification Checklist

* [ ] I edited **BlockList.txt** only (if changing domains).
* [ ] All entries are plain normalized domains.
* [ ] No protocol (`http://` or `https://`).
* [ ] No paths or query parameters.
* [ ] No duplicate entries.
* [ ] Domains are relevant to the scope of this project.
* [ ] Generated files (**uBlock.txt**, **LeechBlock.txt**, reports, etc.) were **not** edited manually.

---

## Additional Information

Provide any supporting information, references, or rationale for the changes.

If adding domains, explain why they belong in this blocklist.
