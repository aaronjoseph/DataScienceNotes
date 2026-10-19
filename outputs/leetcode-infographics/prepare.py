"""Read tagged notes and prepare a preservation-first infographic migration."""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def tagged_notes():
    notes = []
    for path in ROOT.rglob('*.md'):
        rel = path.relative_to(ROOT)
        if any(part.startswith('.') or part in {'copilot', 'outputs'} for part in rel.parts):
            continue
        text = path.read_text()
        if not text.startswith('---\n'):
            continue
        end = text.find('\n---', 4)
        frontmatter = text[:end + 4]
        match = re.search(r'^tags:\s*\n((?:[ \t]+-.*\n)+)', frontmatter, re.M)
        inline = re.search(r'^tags:\s*\[([^\n]+)\]', frontmatter, re.M)
        tags = re.findall(r'[\w/-]+', match.group(1) if match else inline.group(1) if inline else '')
        if 'leetcode' not in [tag.lower() for tag in tags]:
            continue
        number = re.search(r'^problem_number:\s*(\d+)', frontmatter, re.M)
        ident = int(number.group(1)) if number else 0
        body_start = end + 4
        template = text.index('\n## Template', body_start)
        overview = text.index('\n## Overview', body_start)
        refs = text.index('\n## References & Useful Links', overview)
        if template < overview:
            header, top, body = text[:template], text[template:overview], text[overview:refs]
        else:
            visual = text.index('\n## Algorithm at a glance', body_start)
            header, top, body = text[:visual], text[template:refs], text[overview:template]
        notes.append({
            'path': rel.as_posix(), 'number': ident, 'title': path.stem,
            'sha256': hashlib.sha256(text.encode()).hexdigest(), 'original': text,
            'header': header, 'top': top,
            'body': body, 'references': text[refs:],
            'image': f'Attachements/LeetCode/LC{ident:04d} - {path.stem}.png',
        })
    return sorted(notes, key=lambda note: (note['number'], note['path']))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--offset', type=int, default=0)
    parser.add_argument('--limit', type=int, default=10)
    parser.add_argument('--numbers', nargs='*', type=int)
    parser.add_argument('--list', action='store_true')
    args = parser.parse_args()
    notes = tagged_notes()
    if args.numbers:
        notes = [note for note in notes if note['number'] in args.numbers]
    elif not args.list:
        notes = notes[args.offset:args.offset + args.limit]
    if args.list:
        notes = [{key: note[key] for key in ('path', 'number', 'title', 'sha256', 'image')} for note in notes]
    print(json.dumps(notes, ensure_ascii=False))
