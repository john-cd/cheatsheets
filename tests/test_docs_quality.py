# TODO Reviewed ??-??-2026

# Check the published Markdown collection for titles, sections, and examples.

from pathlib import Path
import re
import unittest


DOCS_DIR = Path(__file__).resolve().parents[1] / "docs"


def _docs():
    """Return sorted Markdown pages while excluding archived `.orig` copies."""
    return sorted(p for p in DOCS_DIR.rglob("*.md") if not p.name.endswith(".orig"))


class DocsQualityTests(unittest.TestCase):
    """Enforce the minimum structure expected for published cheat sheets."""

    def test_each_cheatsheet_has_h1_or_frontmatter_title(self):
        """Require every Markdown page to expose a page title."""
        for path in _docs():
            text = path.read_text(encoding="utf-8")
            has_h1 = re.search(r"^#\s+\S", text, re.MULTILINE) is not None
            has_title = re.search(r"^title:\s*\S", text, re.MULTILINE) is not None
            self.assertTrue(has_h1 or has_title, f"Missing title in {path}")

    def test_each_cheatsheet_has_a_section(self):
        """Require each non-index page to contain a second-level section."""
        for path in _docs():
            if path.name == "index.md":
                continue
            text = path.read_text(encoding="utf-8")
            self.assertIsNotNone(
                re.search(r"^##\s+\S", text, re.MULTILINE),
                f"Missing H2 section in {path}",
            )

    def test_each_cheatsheet_has_at_least_one_example_block(self):
        """Require each non-index page to include a fenced example block."""
        for path in _docs():
            if path.name == "index.md":
                continue
            text = path.read_text(encoding="utf-8")
            self.assertIn("```", text, f"Missing code/example block in {path}")


if __name__ == "__main__":
    unittest.main()
