import sys
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import check_links  # noqa: E402


class CheckLinksTests(unittest.TestCase):
    def test_extract_links_skips_ignored_hosts(self):
        text = "[a](https://example.com/x). [b](http://localhost:8000) <https://example.org/y>"
        self.assertEqual(
            check_links.extract_links(text), {"https://example.com/x", "https://example.org/y"}
        )

    def test_network_failure_is_not_broken(self):
        with mock.patch("urllib.request.urlopen", side_effect=OSError("blocked")):
            self.assertEqual(check_links.classify("https://example.com"), "network")

    def test_extract_links_keeps_balanced_parentheses(self):
        text = "[w](https://en.wikipedia.org/wiki/WAR_(file_format)), done"
        self.assertEqual(
            check_links.extract_links(text), {"https://en.wikipedia.org/wiki/WAR_(file_format)"}
        )

    def test_head_404_retried_with_get(self):
        error = check_links.urllib.error.HTTPError("u", 404, "nf", {}, None)
        with mock.patch("urllib.request.urlopen", side_effect=[error, mock.MagicMock()]):
            self.assertEqual(check_links.classify("https://example.com"), "ok")

    def test_404_is_broken(self):
        error = check_links.urllib.error.HTTPError("u", 404, "nf", {}, None)
        with mock.patch("urllib.request.urlopen", side_effect=error):
            self.assertEqual(check_links.classify("https://example.com"), "broken")


if __name__ == "__main__":
    unittest.main()
