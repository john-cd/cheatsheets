import contextlib
import io
import socket
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import check_links  # noqa: E402


def http_error(code: int) -> check_links.urllib.error.HTTPError:
    return check_links.urllib.error.HTTPError("https://example.com", code, "status", {}, None)


class CheckLinksTests(unittest.TestCase):
    def test_extract_links_skips_ignored_hosts(self):
        text = "[a](https://example.com/x). [b](http://localhost:8000) <https://example.org/y>"
        self.assertEqual(
            check_links.extract_links(text), {"https://example.com/x", "https://example.org/y"}
        )

    def test_network_failures_are_not_reported_as_broken(self):
        for error in (OSError("blocked"), socket.timeout("timed out")):
            with self.subTest(error=type(error).__name__):
                with mock.patch.object(check_links, "_fetch", side_effect=error):
                    self.assertEqual(check_links.classify("https://example.com"), "network")

    def test_extract_links_keeps_balanced_parentheses(self):
        text = "[w](https://en.wikipedia.org/wiki/WAR_(file_format)), done"
        self.assertEqual(
            check_links.extract_links(text), {"https://en.wikipedia.org/wiki/WAR_(file_format)"}
        )

    def test_head_unsupported_retries_with_get(self):
        with mock.patch.object(check_links, "_fetch", side_effect=[http_error(405), 200]) as fetch:
            self.assertEqual(check_links.classify("https://example.com"), "ok")

        self.assertEqual(
            fetch.call_args_list,
            [
                mock.call("https://example.com", "HEAD", 10.0),
                mock.call("https://example.com", "GET", 10.0),
            ],
        )

    def test_get_access_policy_after_unsupported_head_is_blocked(self):
        with mock.patch.object(
            check_links, "_fetch", side_effect=[http_error(405), http_error(403)]
        ):
            self.assertEqual(check_links.classify("https://example.com"), "blocked")

    def test_head_not_found_retries_with_get(self):
        with mock.patch.object(check_links, "_fetch", side_effect=[http_error(404), 200]):
            self.assertEqual(check_links.classify("https://example.com"), "ok")

    def test_get_not_found_after_head_fallback_is_broken(self):
        with mock.patch.object(
            check_links, "_fetch", side_effect=[http_error(404), http_error(404)]
        ):
            self.assertEqual(check_links.classify("https://example.com"), "broken")

    def test_inconclusive_http_statuses_are_blocked(self):
        for status in (403, 405, 429, 500, 503):
            with self.subTest(status=status):
                with mock.patch.object(check_links, "_fetch", side_effect=http_error(status)):
                    self.assertEqual(check_links.classify("https://example.com"), "blocked")

    def test_missing_destination_is_broken(self):
        with mock.patch.object(check_links, "_fetch", side_effect=http_error(404)):
            self.assertEqual(check_links.classify("https://example.com"), "broken")

    def test_cli_reports_blocked_targets_and_returns_inconclusive_status(self):
        with tempfile.TemporaryDirectory() as directory:
            markdown = Path(directory) / "page.md"
            markdown.write_text("[site](https://example.com)", encoding="utf-8")
            output = io.StringIO()
            with (
                mock.patch.object(check_links, "classify", return_value="blocked"),
                contextlib.redirect_stdout(output),
            ):
                result = check_links.main([str(markdown)])

        self.assertEqual(result, 2)
        self.assertIn("BLOCKED: https://example.com", output.getvalue())
        self.assertIn(
            "checked=1 broken=0 blocked=1 network_failures=0 unresolved=1", output.getvalue()
        )

    def test_cli_only_allows_network_failures_when_requested(self):
        with tempfile.TemporaryDirectory() as directory:
            markdown = Path(directory) / "page.md"
            markdown.write_text("[site](https://example.com)", encoding="utf-8")
            with mock.patch.object(check_links, "classify", return_value="network"):
                self.assertEqual(check_links.main([str(markdown)]), 2)
                self.assertEqual(check_links.main([str(markdown), "--allow-network-failures"]), 0)

    def test_cli_returns_broken_status_for_definite_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            markdown = Path(directory) / "page.md"
            markdown.write_text("[site](https://example.com)", encoding="utf-8")
            with mock.patch.object(check_links, "classify", return_value="broken"):
                self.assertEqual(check_links.main([str(markdown)]), 1)


if __name__ == "__main__":
    unittest.main()
