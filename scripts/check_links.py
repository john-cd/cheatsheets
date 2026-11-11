"""Check external Markdown links, separating blocked networks from broken destinations.

Exit status: 0 = no broken or blocked targets (network failures may be allowed),
1 = broken destinations (HTTP 404/410), 2 = unresolved blocked or network checks.
"""

from __future__ import annotations

import argparse
import re
import socket
import sys
import urllib.error
import urllib.request
from pathlib import Path

LINK_RE = re.compile(r"\]\((https?://(?:[^()\s]|\([^()\s]*\))+)\)|<(https?://[^>\s]+)>")
IGNORED = re.compile(r"^https?://(localhost|127\.0\.0\.1|twitter\.com|www\.linkedin\.com)")
BROKEN_STATUSES = {404, 410}
HEAD_FALLBACK_STATUSES = BROKEN_STATUSES | {405, 501}
USER_AGENT = "cheatsheets-link-check/1.0"


def extract_links(text: str) -> set[str]:
    """Return unique external URLs found in Markdown text."""
    links = {m.group(1) or m.group(2) for m in LINK_RE.finditer(text)}
    return {url.rstrip(".,;") for url in links if not IGNORED.match(url)}


def _fetch(url: str, method: str, timeout: float) -> int:
    """Request one URL and return its HTTP status, raising on transport failures."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT}, method=method)
    with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310
        status = response.getcode()
        if status is None:
            raise urllib.error.URLError("response did not include an HTTP status")
        return status


def _classify_http_status(status: int) -> str:
    """Treat 404/410 as broken, other error statuses as blocked, and lower statuses as okay."""
    if status in BROKEN_STATUSES:
        return "broken"
    if status >= 400:
        return "blocked"
    return "ok"


def classify(url: str, timeout: float = 10.0) -> str:
    """Return 'ok', 'broken', 'blocked', or 'network' after checking one URL.

    Try HEAD first and retry with GET when the server reports a missing resource or does
    not support HEAD. Network failures remain separate from definite missing-link results.
    """
    try:
        try:
            status = _fetch(url, "HEAD", timeout)
        except urllib.error.HTTPError as error:
            if error.code not in HEAD_FALLBACK_STATUSES:
                status = error.code
                error.close()
                return _classify_http_status(status)
            error.close()
            try:
                status = _fetch(url, "GET", timeout)
            except urllib.error.HTTPError as get_error:
                status = get_error.code
                get_error.close()
    except urllib.error.HTTPError as error:
        return _classify_http_status(error.code)
    except urllib.error.URLError, socket.timeout, ConnectionError, OSError:
        return "network"
    return _classify_http_status(status)


def main(argv: list[str] | None = None) -> int:
    """Check links in selected Markdown files and return the documented CLI status."""
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
    for kind in ("broken", "blocked", "network"):
        for url, status in results.items():
            if status == kind:
                print(f"{kind.upper()}: {url} ({urls[url][0]})")
    broken = sum(s == "broken" for s in results.values())
    blocked = sum(s == "blocked" for s in results.values())
    network = sum(s == "network" for s in results.values())
    unresolved = blocked + network
    print(
        f"checked={len(results)} broken={broken} blocked={blocked} "
        f"network_failures={network} unresolved={unresolved}"
    )
    if broken:
        return 1
    if blocked:
        return 2
    if network and not args.allow_network_failures:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
