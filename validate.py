#!/usr/bin/env python3
"""Validate Store metadata offline using the vendored Eitr rules."""
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / 'vendor'))
from eitr_community import validate_index
from eitr_plugin_manifest import unique_object


def main():
    path = Path(__file__).with_name('index.json')
    if path.stat().st_size > 1024 * 1024:
        raise ValueError('Store index exceeds size limit')
    validate_index(json.loads(path.read_text(), object_pairs_hook=unique_object))
    print('Store index valid')


if __name__ == '__main__':
    main()
