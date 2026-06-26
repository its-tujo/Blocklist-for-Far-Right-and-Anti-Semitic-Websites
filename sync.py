import requests

SOURCE = "https://raw.githubusercontent.com/its-tujo/Blocklist-for-Far-Right-and-Anti-Semitic-Websites/main/BlockList.txt"

def normalize(line):
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    return line.replace("https://", "").replace("http://", "").strip("/")

def main():
    raw = requests.get(SOURCE, timeout=30).text.splitlines()

    domains = set()

    for line in raw:
        d = normalize(line)
        if d:
            domains.add(d)

    # 1) sauber sortiert
    sorted_domains = sorted(domains)

    # 2) uBlock Format
    ublock = sorted(f"||{d}^" for d in sorted_domains)

    # 3) LeechBlock Format (beide Varianten pro Domain)
    leechblock = set()
    for d in domains:
        leechblock.add(d)
        leechblock.add(f"*.{d}")

    leechblock_sorted = sorted(leechblock)

    # 4) Dateien komplett überschreiben (wichtig!)
    with open("BlockList.txt", "w") as f:
        f.write("\n".join(sorted_domains))

    with open("uBlock.txt", "w") as f:
        f.write("\n".join(ublock))

    with open("LeechBlock.txt", "w") as f:
        f.write("\n".join(leechblock_sorted))


if __name__ == "__main__":
    main()