"""List or search the published workflow catalog without executing skills."""
from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

def load_catalog():
    return json.loads((ROOT / 'catalog/skills.json').read_text(encoding='utf-8'))['skills']

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--category', choices=['competition', 'academic', 'documents'])
    parser.add_argument('--search')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    rows = load_catalog()
    if args.category:
        rows = [s for s in rows if s['category'] == args.category]
    if args.search:
        term = args.search.casefold()
        rows = [s for s in rows if term in json.dumps(s, ensure_ascii=False).casefold()]
    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    else:
        for s in rows:
            print(f"{s['id']} | {s['category']} | {s['title']}\n  {s['summary']}")
        print(f'{len(rows)} skills')

if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    main()
