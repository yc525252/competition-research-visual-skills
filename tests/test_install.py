from pathlib import Path
import importlib.util
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('crv_install', ROOT / 'scripts/install.py')
INSTALL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INSTALL)

class InstallerBehavior(unittest.TestCase):
    def test_category_selection_and_invalid_inputs(self):
        self.assertEqual(len(INSTALL.select_skills('competition')), 6)
        self.assertEqual(len(INSTALL.select_skills('academic')), 5)
        self.assertEqual(len(INSTALL.select_skills('documents')), 20)
        self.assertEqual(len(INSTALL.select_skills('all')), 31)
        for category, names in [(None, None), ('all', ['crv-docx']), (None, ['../escape']), ('missing', None)]:
            with self.assertRaises(ValueError):
                INSTALL.select_skills(category, names)

    def test_install_preserves_content_and_license(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'skills'
            installed = INSTALL.install(['crv-docx'], target)
            self.assertEqual(installed, [str((target / 'crv-docx').resolve())])
            self.assertEqual((target / 'crv-docx/SKILL.md').read_bytes(), (ROOT / 'skills/crv-docx/SKILL.md').read_bytes())
            self.assertEqual((target / 'crv-docx/LICENSE').read_bytes(), (ROOT / 'LICENSE').read_bytes())

    def test_existing_target_prevents_all_writes(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'skills'
            existing = target / 'crv-docx'
            existing.mkdir(parents=True)
            sentinel = existing / 'SKILL.md'
            sentinel.write_text('user content', encoding='utf-8')
            with self.assertRaises(FileExistsError):
                INSTALL.install(['crv-pdf', 'crv-docx'], target)
            self.assertEqual(sentinel.read_text(encoding='utf-8'), 'user content')
            self.assertFalse((target / 'crv-pdf').exists())

    def test_dry_run_does_not_create_destination(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'not-created'
            plan = INSTALL.install(['crv-docx'], target, dry_run=True)
            self.assertEqual(len(plan), 1)
            self.assertFalse(target.exists())

    def test_repository_target_is_rejected(self):
        for target in (ROOT, ROOT / 'installed', ROOT.parent):
            with self.assertRaises(ValueError):
                INSTALL.install(['crv-docx'], target, dry_run=True)

    def test_cli_dry_run_and_unknown_skill(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'cli-target'
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/install.py'), '--category', 'academic', '--target', str(target), '--dry-run'], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(target.exists())
            invalid = subprocess.run([sys.executable, str(ROOT / 'scripts/install.py'), '--skill', 'missing', '--target', str(target)], capture_output=True)
            self.assertNotEqual(invalid.returncode, 0)
            self.assertFalse(target.exists())

if __name__ == '__main__':
    unittest.main()
