"""Validate catalog coverage, source metadata, documentation links, and public content scope."""
from pathlib import Path
from collections import Counter
import json
import re

ROOT = Path(__file__).resolve().parents[1]

def main():
    data = json.loads((ROOT / 'catalog/skills.json').read_text(encoding='utf-8'))
    rows = data['skills']
    names = [s['id'] for s in rows]
    assert len(names) == len(set(names)) == 31
    assert Counter(s['category'] for s in rows) == {'competition': 6, 'academic': 5, 'documents': 20}
    assert {p.parent.name for p in (ROOT / 'skills').glob('*/SKILL.md')} == set(names)
    for s in rows:
        assert re.fullmatch(r'crv-[a-z0-9-]{1,59}', s['id'])
        path = ROOT / 'skills' / s['id'] / 'SKILL.md'
        content = path.read_text(encoding='utf-8')
        assert content.startswith('---\nname: ' + s['id'] + '\n')
        description = re.search(r'^description: (.+)$', content, re.M)
        assert description and json.loads(description[1]) == s['summary']
        assert s['original_distribution'] == 'not-bundled'
        assert all(s[k] for k in ('inputs', 'outputs', 'steps', 'boundaries', 'tools', 'example'))
        for step in s['steps']:
            assert step in content
        for output in s['outputs']:
            assert output in content
        assert '$' + s['id'] in content
        assert s['summary'] in (ROOT / 'docs' / (s['category'] + '.md')).read_text(encoding='utf-8')
    links = 0
    files = []
    for p in ROOT.rglob('*'):
        if not p.is_file() or any(part in {'.git', '__pycache__', '.venv'} for part in p.relative_to(ROOT).parts):
            continue
        assert not p.is_symlink()
        if p.suffix not in {'.md', '.py', '.json', '.yml'} and p.name not in {'LICENSE', '.gitignore'}:
            raise AssertionError('Unexpected public file: ' + str(p))
        files.append(p)
        text = p.read_text(encoding='utf-8')
        # Detect concrete local paths and credential-shaped values, not generic API names.
        path_patterns = (r'(?<![A-Za-z0-9])[A-Za-z]:[\\/]', '/' + 'Users/', r'/home/[A-Za-z0-9_.-]+/')
        assert not any(re.search(pattern, text) for pattern in path_patterns), p
        assert not re.search(r'gh[pousr]_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{16}|sk-[A-Za-z0-9]{24,}', text), p
        if p.suffix == '.md':
            assert text.count('```') % 2 == 0, p
            for target in re.findall(r'\[[^\]]+\]\(([^\n)]+)\)', text):
                if target.startswith(('http://', 'https://', '#')):
                    continue
                resolved = (p.parent / target.split('#', 1)[0]).resolve()
                assert resolved.is_relative_to(ROOT) and resolved.is_file(), (p, target)
                links += 1
    print(json.dumps({'status': 'passed', 'skills': len(rows), 'categories': 3, 'public_files': len(files), 'local_links_checked': links}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
