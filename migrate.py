#!/usr/bin/env python3
"""Migrate reviewed local copies of the old index and license, without network."""
import argparse
import json
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'vendor'))
from eitr_community import validate_index
from eitr_plugin_manifest import unique_object
from eitr_plugin_install import normalized_url


def migrate(index_path, license_path):
    if index_path.stat().st_size > 1024 * 1024 or license_path.stat().st_size > 1024 * 1024:
        raise ValueError('Oversized migration input')
    source = validate_index(json.loads(index_path.read_text(), object_pairs_hook=unique_object))
    current = validate_index(json.loads((ROOT / 'index.json').read_text(), object_pairs_hook=unique_object))
    if any(current[kind] for kind in ('themes', 'plugins', 'wallpapers', 'removed')):
        raise ValueError('Migration only replaces an empty prepared index')
    if not license_path.read_text().strip():
        raise ValueError('Source license is empty')
    result = dict(schemaVersion=2, themes=[], plugins=[], wallpapers=source.get('wallpapers', []), removed=source['removed'])
    for kind in ('themes', 'plugins'):
        for row in source[kind]:
            official = normalized_url(row['repository']).startswith('github.com/eitr-org/')
            result[kind].append(dict(row, **({'official': True} if official else {})))
    validate_index(result)
    shutil.copyfile(license_path, ROOT / 'LICENSE')
    (ROOT / 'index.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-index', required=True, type=Path)
    parser.add_argument('--source-license', required=True, type=Path)
    args = parser.parse_args()
    migrate(args.source_index, args.source_license)
