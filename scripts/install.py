"""Install selected original CRV skills. Existing destinations are never overwritten."""
from pathlib import Path
import argparse
import json
import os
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]

def catalog():
    return json.loads((ROOT / 'catalog/skills.json').read_text(encoding='utf-8'))['skills']

def select_skills(category=None, names=None):
    rows = catalog()
    available = {s['id']: s for s in rows}
    if bool(category) == bool(names):
        raise ValueError('Choose exactly one of --category or --skill.')
    if names:
        unique = list(dict.fromkeys(names))
        unknown = [name for name in unique if name not in available]
        if unknown:
            raise ValueError('Unknown skills: ' + ', '.join(unknown))
        return unique
    selected = [s['id'] for s in rows if category == 'all' or s['category'] == category]
    if not selected:
        raise ValueError('Unknown or empty category: ' + str(category))
    return selected

def default_target():
    configured = os.environ.get('CODEX_HOME')
    return (Path(configured).expanduser() if configured else Path.home() / '.codex') / 'skills'

def install(names, target, dry_run=False):
    known = {s['id'] for s in catalog()}
    if not names or len(names) != len(set(names)) or not set(names) <= known:
        raise ValueError('Select nonempty, unique, known skill names.')
    target = Path(target).expanduser().resolve()
    if target == ROOT or target.is_relative_to(ROOT) or ROOT.is_relative_to(target):
        raise ValueError('The target must be separate from this repository and its ancestors.')
    plan = []
    for name in names:
        source = ROOT / 'skills' / name
        destination = target / name
        if not source.is_dir() or source.is_symlink() or not (source / 'SKILL.md').is_file():
            raise ValueError('Invalid source skill: ' + name)
        if any(p.is_symlink() for p in source.rglob('*')):
            raise ValueError('Source symlinks are not supported: ' + name)
        if destination.exists() or destination.is_symlink():
            raise FileExistsError('Destination already exists: ' + str(destination))
        plan.append((source, destination))
    if dry_run:
        return [str(destination) for _, destination in plan]
    target.mkdir(parents=True, exist_ok=True)
    for source, destination in plan:
        shutil.copytree(source, destination)
        shutil.copy2(ROOT / 'LICENSE', destination / 'LICENSE')
    return [str(destination) for _, destination in plan]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument('--category', choices=['competition', 'academic', 'documents', 'all'])
    selection.add_argument('--skill', nargs='+')
    parser.add_argument('--target', type=Path, default=default_target())
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        names = select_skills(args.category, args.skill)
        paths = install(names, args.target, args.dry_run)
    except (ValueError, OSError) as error:
        parser.exit(1, str(error) + '\n')
    print(json.dumps({'status': 'dry-run' if args.dry_run else 'installed', 'count': len(paths), 'destinations': paths}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    main()
