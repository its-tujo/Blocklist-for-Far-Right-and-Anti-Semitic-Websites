import requests
from datetime import datetime

SOURCE = "https://raw.githubusercontent.com/its-tujo/Blocklist-for-Far-Right-and-Anti-Semitic-Websites/main/BlockList.txt"


def normalize(line: str):
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    return line.replace("https://", "").replace("http://", "").strip("/")


def load_set_from_file(path):
    try:
        with open(path, "r") as f:
            return {normalize(l) for l in f.read().splitlines() if normalize(l)}
    except FileNotFoundError:
        return set()


def write_file(path, lines):
    with open(path, "w") as f:
        f.write("\n".join(lines))


def main():
    raw = requests.get(SOURCE, timeout=30).text.splitlines()

    # clean upstream
    new_domains = {normalize(l) for l in raw}
    new_domains = {d for d in new_domains if d}

    # old local
    old_domains = load_set_from_file("BlockList.txt")

    # diff (NOW consistent)
    added = sorted(new_domains - old_domains)
    removed = sorted(old_domains - new_domains)

    all_domains = sorted(new_domains)

    # uBlock format
    ublock = sorted(f"||{d}^" for d in all_domains)

    # LeechBlock format
    leechblock = sorted(
        {d for d in all_domains} |
        {f"*.{d}" for d in all_domains}
    )

    # write outputs
    write_file("BlockList.txt", all_domains)
    write_file("uBlock.txt", ublock)
    write_file("LeechBlock.txt", leechblock)

    # report (for logs / artifacts)
    report = []
    report.append(f"# Blocklist Sync Report")
    report.append(f"Generated: {datetime.utcnow().isoformat()} UTC\n")

    report.append("## Summary")
    report.append(f"- Total domains: {len(all_domains)}")
    report.append(f"- Added: {len(added)}")
    report.append(f"- Removed: {len(removed)}\n")

    if added:
        report.append("## Added")
        report.extend([f"- {d}" for d in added])
        report.append("")

    if removed:
        report.append("## Removed")
        report.extend([f"- {d}" for d in removed])
        report.append("")

    write_file("report.md", report)

    # GitHub Step Summary
    write_file("step_summary.md", report)


if __name__ == "__main__":
    main()