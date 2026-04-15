from pathlib import Path
import re
import unittest


DOCS_DIR = Path(__file__).resolve().parents[1] / "docs"


def _docs():
    return sorted(p for p in DOCS_DIR.rglob("*.md") if not p.name.endswith(".orig"))


class DocsQualityTests(unittest.TestCase):
    def test_each_cheatsheet_has_h1_or_frontmatter_title(self):
        for path in _docs():
            text = path.read_text(encoding="utf-8")
            has_h1 = re.search(r"^#\s+\S", text, re.MULTILINE) is not None
            has_title = re.search(r"^title:\s*\S", text, re.MULTILINE) is not None
            self.assertTrue(has_h1 or has_title, f"Missing title in {path}")

    def test_each_cheatsheet_has_a_section(self):
        for path in _docs():
            if path.name == "index.md":
                continue
            text = path.read_text(encoding="utf-8")
            self.assertIsNotNone(
                re.search(r"^##\s+\S", text, re.MULTILINE),
                f"Missing H2 section in {path}",
            )

    def test_each_cheatsheet_has_at_least_one_example_block(self):
        for path in _docs():
            if path.name == "index.md":
                continue
            text = path.read_text(encoding="utf-8")
            self.assertIn("```", text, f"Missing code/example block in {path}")


if __name__ == "__main__":
    unittest.main()
