"""Tests for the Claude agent to Codex agent compatibility layer."""

from __future__ import annotations

import sys
import tempfile
import tomllib
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import install_codex_agents as converter  # noqa: E402


class CodexAgentConversionTest(unittest.TestCase):
    def test_all_agents_generate_valid_toml(self) -> None:
        generated = converter.build_all()
        self.assertEqual(5, len(generated))
        for content in generated.values():
            parsed = tomllib.loads(content)
            self.assertIn("name", parsed)
            self.assertIn("description", parsed)
            self.assertIn("developer_instructions", parsed)

    def test_list_form_tools_are_parsed(self) -> None:
        source = ROOT / "agents" / "blog-writer.md"
        header, _ = converter.split_document(source.read_text(encoding="utf-8"))
        metadata = converter.parse_frontmatter(header)
        self.assertIn("Write", converter.tool_names(metadata["tools"]))

    def test_read_only_agents_remain_read_only(self) -> None:
        _, content = converter.build_agent(ROOT / "agents" / "blog-reviewer.md")
        self.assertEqual("read-only", tomllib.loads(content)["sandbox_mode"])

    def test_installer_writes_project_scoped_agents(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            written = converter.install(Path(directory))
            self.assertEqual(5, len(written))
            self.assertTrue(all(path.parent.name == "agents" for path in written))


if __name__ == "__main__":
    unittest.main()
