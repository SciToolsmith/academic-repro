from __future__ import annotations

import re
import subprocess
import sys
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SKILL = REPO / "academic-repro"
REFERENCE_LINK = re.compile(r"\[[^\]]+\]\((references/[^)#]+\.md)(?:#[^)]+)?\)")


class RepositoryTests(unittest.TestCase):
    def test_python_sources_compile(self) -> None:
        sources = sorted((SKILL / "scripts").glob("*.py")) + sorted((REPO / "tests").glob("*.py"))
        completed = subprocess.run(
            [sys.executable, "-m", "py_compile", *map(str, sources)],
            cwd=REPO,
            text=True,
            capture_output=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)

    def test_skill_entrypoint_is_valid_and_progressively_disclosed(self) -> None:
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        frontmatter = text.split("---", 2)[1]
        self.assertRegex(frontmatter, r"(?m)^name:\s*academic-repro\s*$")
        self.assertRegex(frontmatter, r"(?m)^description:\s*\S")

        links = list(dict.fromkeys(REFERENCE_LINK.findall(text)))
        self.assertGreaterEqual(len(links), 4)
        self.assertTrue({
            "references/diagram-handoff.md",
            "references/image-derived-reconstruction.md",
            "references/target-figure-acquisition.md",
            "references/source-environment-audit.md",
            "references/execution-validation.md",
            "references/evidence-contract.md",
            "references/delivery-contract.md",
        }.issubset(links))
        for relative in links:
            self.assertTrue((SKILL / relative).is_file(), relative)

        # The entrypoint should remain a routing and decision surface, not a manual.
        self.assertLessEqual(len(text.split()), 1200)

    def test_instruction_surface_stays_compact(self) -> None:
        references = sorted((SKILL / "references").glob("*.md"))
        total_words = len((SKILL / "SKILL.md").read_text(encoding="utf-8").split())
        for path in references:
            words = len(path.read_text(encoding="utf-8").split())
            self.assertLessEqual(words, 1500, f"{path.name} has become a second entrypoint")
            total_words += words
        self.assertLessEqual(total_words, 6500, "policy surface has grown beyond progressive disclosure")

    def test_policy_has_no_case_specific_or_platform_specific_rules(self) -> None:
        policy_files = [SKILL / "SKILL.md", *sorted((SKILL / "references").glob("*.md"))]
        policy = "\n".join(path.read_text(encoding="utf-8") for path in policy_files)
        for pattern in (
            r"\bfeature mode decomposition\b",
            r"\bimckd\b",
            r"\bsig1(?:\.mat)?\b",
            r"\b90\s*%",
            r"\b96\s*%",
            r"\b250\s*MiB\b",
            r"\b2\s*GiB\b",
            r"\bWindows PowerShell\b",
            r"\bradar chart\b",
        ):
            self.assertNotRegex(policy, pattern)

    def test_readmes_present_the_same_small_public_contract(self) -> None:
        chinese = (REPO / "README.md").read_text(encoding="utf-8")
        english = (REPO / "README.en.md").read_text(encoding="utf-8")
        self.assertEqual(chinese.count('<h1 align="center">Academic Repro</h1>'), 1)
        self.assertEqual(english.count('<h1 align="center">Academic Repro</h1>'), 1)
        for required in ("使用 $skill-installer", "使用 $academic-repro", "可信生成", "论点保持", "视觉语义"):
            self.assertIn(required, chinese)
        for required in ("Use $skill-installer", "Use $academic-repro", "Credible generation", "Claim preservation", "Visual-semantic preservation"):
            self.assertIn(required, english)

    def test_runtime_dependencies_and_pdf_ci_are_declared(self) -> None:
        requirements = (SKILL / "requirements.txt").read_text(encoding="utf-8")
        workflow = (REPO / ".github" / "workflows" / "test.yml").read_text(encoding="utf-8")
        self.assertIn("Pillow", requirements)
        self.assertIn("pdfplumber", requirements)
        self.assertIn("poppler", workflow)
        self.assertIn('"3.10"', workflow)

    def test_helpers_are_present(self) -> None:
        for relative in (
            "scripts/materialize_target_figures.py",
            "scripts/assemble_delivery.py",
            "scripts/evidence_record.py",
            "scripts/inspect_artifact.py",
            "scripts/probe_environment.py",
        ):
            self.assertTrue((SKILL / relative).is_file(), relative)

    def test_generated_cache_files_are_not_tracked(self) -> None:
        completed = subprocess.run(
            ["git", "ls-files"], cwd=REPO, text=True, capture_output=True, check=True,
        )
        forbidden = [
            path for path in completed.stdout.splitlines()
            if path.endswith((".pyc", ".pyo", ".DS_Store")) or "/__pycache__/" in f"/{path}/"
        ]
        self.assertEqual(forbidden, [])


if __name__ == "__main__":
    unittest.main()
