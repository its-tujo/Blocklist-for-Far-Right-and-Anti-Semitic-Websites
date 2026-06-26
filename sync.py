import requests
from datetime import datetime

SOURCE = "https://raw.githubusercontent.com/its-tujo/Blocklist-for-Far-Right-and-Anti-Semitic-Websites/main/BlockList.txt"

def normalize(line):
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    return line.replace("https://", "").replace("http://", "").strip("/")

def main():
    raw = requests.get(SOURCE, timeout=30).text.splitlines()

    new_domains = set()

    for line in raw:
        d = normalize(line)
        if d:
            new_domains.add(d)

    try:
        with open("BlockList.txt", "r") as f:
            old_domains = set(f.read().splitlines())
    except FileNotFoundError:
        old_domains = set()

    added = sorted(new_domains - old_domains)
    removed = sorted(old_domains - new_domains)
    all_domains = sorted(new_domains)

    ublock = sorted(f"||{d}^" for d in all_domains)

    leechblock = sorted(
        {d for d in all_domains} |
        {f"*.{d}" for d in all_domains}
    )

    # write files
    with open("BlockList.txt", "w") as f:
        f.write("\n".join(all_domains))

    with open("uBlock.txt", "w") as f:
        f.write("\n".join(ublock))

    with open("LeechBlock.txt", "w") as f:
        f.write("\n".join(leechblock))

    # markdown report
    report = []
    report.append(f"# Blocklist Sync Report")
    report.append(f"Generated: {datetime.utcnow().isoformat()} UTC\n")

    report.append(f"## Summary")
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

    with open("report.md", "w") as f:
        f.write("\n".join(report))

    # GitHub Step Summary (special file)
    with open("step_summary.md", "w") as f:
        f.write("\n".join(report))


if __name__ == "__main__":
    main()