"""Check external Markdown links, separating blocked networks from broken destinations.

Exit status: 0 = all reachable (or only network failures with --allow-network-failures),
1 = broken destinations (HTTP 404/410 or similar), 2 = only network failures.
"""

from __future__ import annotations

import argparse
import re
import socket
import sys
import urllib.error
import urllib.request
from pathlib import Path

LINK_RE = re.compile(r"\]\((https?://[^)\s]+)\)|<(https?://[^>\s]+)>")
IGNORED = re.compile(r"^https?://(localhost|127\.0\.0\.1|twitter\.com|www\.linkedin\.com)")
BROKEN_STATUSES = {404, 410}
USER_AGENT = "cheatsheets-link-check/1.0"


def extract_links(text: str) -> set[str]:
    """Return unique external URLs found in Markdown text."""
    links = {m.group(1) or m.group(2) for m in LINK_RE.finditer(text)}
    return {url.rstrip(".,;") for url in links if not IGNORED.match(url)}


def classify(url: str, timeout: float = 10.0) -> str:
    """Return 'ok', 'broken', or 'network' for a URL."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT}, method="HEAD")
    try:
        with urllib.request.urlopen(request, timeout=timeout):  # noqa: S310
            return "ok"
    except urllib.error.HTTPError as error:
        if error.code in BROKEN_STATUSES:
            return "broken"
        return "ok"  # 403/405/429/5xx: reachable, access policy differs from a broken target
    except urllib.error.URLError, socket.timeout, ConnectionError, OSError:
        return "network"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", default=[Path("docs")], type=Path)
    parser.add_argument("--allow-network-failures", action="store_true")
    args = parser.parse_args(argv)

    files = [f for p in args.paths for f in ([p] if p.is_file() else sorted(p.rglob("*.md")))]
    urls: dict[str, list[Path]] = {}
    for file in files:
        for url in extract_links(file.read_text(encoding="utf-8")):
            urls.setdefault(url, []).append(file)

    results = {url: classify(url) for url in sorted(urls)}
    for kind in ("broken", "network"):
        for url, status in results.items():
            if status == kind:
                print(f"{kind.upper()}: {url} ({urls[url][0]})")
    broken = sum(s == "broken" for s in results.values())
    network = sum(s == "network" for s in results.values())
    print(f"checked={len(results)} broken={broken} network_failures={network}")
    if broken:
        return 1
    if network and not args.allow_network_failures:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
