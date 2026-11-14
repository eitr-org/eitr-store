"""Offline index contract and lossless migration checks."""
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'vendor'))
from eitr_community import validate_index


class IndexTests(unittest.TestCase):
    def row(self):
        return dict(id='northern', repository='https://github.com/eitr-org/art', folder='themes/northern',
                    maintainer='Example', license='MIT', description='Northern art')

    def test_versions_pins_duplicates_and_removed_entries(self):
        old = dict(schemaVersion=1, themes=[self.row()], plugins=[], removed=[])
        self.assertEqual(validate_index(old), old)
        current = dict(old, schemaVersion=2, wallpapers=[dict(self.row(), official=True)])
        self.assertEqual(validate_index(current), current)
        for invalid in (dict(current, plugins=[dict(self.row(), commit='HEAD')]),
                        dict(current, wallpapers=[self.row(), self.row()]),
                        dict(current, wallpapers=[dict(self.row(), official='yes')]),
                        dict(current, removed=[dict(kind='themes', id='northern', reason='Removed')])):
            with self.assertRaises(ValueError):
                validate_index(invalid)

    def test_migration_keeps_entries_removals_and_license_bytes(self):
        spec = importlib.util.spec_from_file_location('migrate', ROOT / 'migrate.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            old = dict(schemaVersion=1, themes=[self.row()], plugins=[],
                       removed=[dict(kind='plugins', id='retired', reason='Retired')])
            source = folder / 'old-index.json'
            license_path = folder / 'old-license'
            source.write_text(json.dumps(old))
            license_path.write_bytes(b'License fixture\n\nExact bytes.\n')
            (folder / 'index.json').write_text(json.dumps(dict(schemaVersion=2, themes=[], plugins=[], wallpapers=[], removed=[])))
            with patch.object(module, 'ROOT', folder):
                module.migrate(source, license_path)
                result = validate_index(json.loads((folder / 'index.json').read_text()))
                self.assertEqual(result['themes'], [dict(self.row(), official=True)])
                self.assertEqual(result['removed'], old['removed'])
                self.assertEqual((folder / 'LICENSE').read_bytes(), license_path.read_bytes())
                with self.assertRaises(ValueError):
                    module.migrate(source, license_path)
