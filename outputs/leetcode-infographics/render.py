"""Render precise PNG study cards from existing notes; never write note files."""
import argparse
import ast
import copy
import hashlib
import json
import re
import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from prepare import ROOT, tagged_notes
from pseudocode_overrides import OVERRIDES

W, PAD = 1600, 64
NAVY, BLUE, TEAL = '#152e4b', '#225eae', '#087f7a'
FONT_DIR = Path('/System/Library/Fonts')
FONTS = {
    'title': ImageFont.truetype(str(FONT_DIR / 'Supplemental/Arial Bold.ttf'), 62),
    'heading': ImageFont.truetype(str(FONT_DIR / 'Supplemental/Arial Bold.ttf'), 35),
    'body': ImageFont.truetype(str(FONT_DIR / 'Supplemental/Arial.ttf'), 35),
    'small': ImageFont.truetype(str(FONT_DIR / 'Supplemental/Arial.ttf'), 28),
    'code': ImageFont.truetype(str(FONT_DIR / 'Menlo.ttc'), 34),
}


def plain(text):
    text = re.sub(r'\[\^.*?\]', '', text)
    text = re.sub(r'\[\[([^]|]+)\|([^]]+)\]\]', r'\2', text)
    text = re.sub(r'\[\[([^]]+)\]\]', r'\1', text)
    text = re.sub(r'(?<!\w)\*([A-Za-z][A-Za-z ]*[A-Za-z])\*(?!\w)', r'\1', text)
    for old, new in [('\\max', 'max'), ('\\min', 'min'), ('\\log', 'log '),
                     ('\\alpha', 'alpha'), ('\\,', ' '), ('\\bigl', ''), ('\\bigr', ''),
                     ('\\times', ' × '), ('\\cdot', ' × ')]:
        text = text.replace(old, new)
    return text.replace('$', '').replace('`', '').replace('**', '').replace('{', '(').replace('}', ')').strip()


class RemoveTypes(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        node.returns = None
        for arg in node.args.posonlyargs + node.args.args + node.args.kwonlyargs:
            arg.annotation = None
        return self.generic_visit(node)


class RemoveSolutionSelf(ast.NodeTransformer):
    def visit_Attribute(self, node):
        if isinstance(node.value, ast.Name) and node.value.id == 'self':
            return ast.copy_location(ast.Name(id=node.attr, ctx=node.ctx), node)
        return self.generic_visit(node)


def pseudocode(note):
    if note['number'] in OVERRIDES:
        return OVERRIDES[note['number']]
    if note['number'] == 875:
        return '''function minimumSpeed(piles, h):
    function hoursRequired(speed):
        total = 0
        for each pile in piles:
            total += (pile + speed - 1) // speed
        return total

    low, high = 1, max(piles)
    while low < high:
        middle = low + (high - low) // 2
        if hoursRequired(middle) <= h:
            high = middle
        else:
            low = middle + 1
    return low'''
    blocks = re.findall(r'```python\n(.*?)```', note['top'], re.S)
    if not blocks:
        raise ValueError(f"No primary Python implementation: {note['path']}")
    tree = ast.parse(blocks[0])
    body = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            continue
        if isinstance(node, ast.ClassDef) and node.name == 'Solution':
            for member in node.body:
                if isinstance(member, ast.FunctionDef):
                    if member.args.args and member.args.args[0].arg == 'self':
                        member.args.args.pop(0)
                    member = RemoveSolutionSelf().visit(member)
                body.append(member)
        else:
            body.append(node)
    tree.body = body
    tree = ast.fix_missing_locations(RemoveTypes().visit(tree))
    normalized = ast.unparse(tree)
    ast.parse(normalized)
    return re.sub(r'\bdef ', 'function ', normalized)


def details(note):
    overview = re.search(r'^## Overview\n\n(.*?)(?=\n\n)', note['body'], re.M | re.S).group(1)
    how = re.search(r'^#{2,3} How to Solve\n(.*?)(?=\n#{2,3} |\Z)', note['body'], re.M | re.S)
    steps = re.findall(r'^\d+\. (.+)$', how.group(1), re.M)
    complexity = note['top'].split('## Complexity', 1)[1].strip().split('\n\n', 1)[0]
    complexity = complexity.replace(' Bounds describe the implementation above and exclude required output unless stated otherwise.', '')
    if note['number'] == 875:
        overview = 'Search over possible eating speeds to find the smallest speed that finishes all piles within h hours.'
        complexity = 'Time: O(n(1 + log M)), usually written O(n log M) for M >= 2. Auxiliary space: O(1). Each speed check scans n piles; binary search halves the speed range. n = number of piles; M = largest pile size.'
    return plain(overview), [plain(step) for step in steps], plain(complexity)


def glossary(note, complexity):
    number, pattern = note['number'], re.search(r'^pattern:\s*(.+)$', note['header'], re.M).group(1).strip('"')
    if pattern in {'Trees', 'Linked List'}:
        n = 'number of nodes'; m = 'number of nodes in the second input'
    elif pattern in {'2-D Dynamic Programming', 'Sliding Window', 'Stack'} and any(x in note['original'] for x in ['str1', 'text1', 'word1', 's: str', 's: ']):
        n = 'input string length'; m = 'second string or pattern length'
    elif number in {48, 73, 778}:
        n = 'grid side length'
        m = 'second input length'
    else:
        n = 'input length'; m = 'second input length'
    definitions = {'n': n, 'm': m, 'V': 'vertices', 'E': 'edges', 'R': 'rows', 'C': 'columns',
                   'h': 'tree height', 'w': 'maximum tree width', 'L': 'word length',
                   'S': 'total input characters', 'u': 'distinct tracked values', 'k': 'requested rank or size',
                   'N': 'total input items', 'q': 'queries', 'c': 'candidate count', 'T': 'half-total target',
                   'A': 'target amount', 'F': 'feed sources, including self', 'Q': 'number of solutions',
                   'b': 'set-bit count', 'd': 'wildcard count', 'g': 'groups', 'alpha': 'inverse Ackermann function'}
    if number == 146: definitions['C'] = 'cache capacity'
    if number == 70: definitions['n'] = 'number of stairs'
    if number == 51: definitions['n'] = 'board side length'
    if number == 62: definitions.update(m='grid rows', n='grid columns')
    if number == 338: definitions['n'] = 'largest requested integer'
    if number in {190, 371}: definitions['w'] = 'integer bit width'
    if number in {322, 518}: definitions['c'] = 'coin types'
    if number == 39: definitions['D'] = 'target / minimum candidate'; definitions['c'] = 'candidate count'
    if number == 49: definitions.update(L='total characters', n='number of words', g='anagram groups')
    if number == 17: definitions['L'] = 'number of input digits'
    if number == 19: definitions['L'] = 'list length'
    if number == 23: definitions.update(N='total list nodes', k='number of input lists')
    if number == 127: definitions.update(N='dictionary word count', L='word length')
    if number == 139: definitions.update(n='input string length', D='dictionary word count', L='maximum dictionary word length')
    if number in {208, 211, 212}: definitions['S'] = 'total inserted-word characters'
    if number == 494: definitions['S'] = 'total absolute input sum'
    if number == 875: return []
    if number == 981: definitions.update(m='versions for the queried key', N='total stored assignments')
    if number == 2013: definitions['N'] = 'stored point occurrences'
    if number == 230: definitions['k'] = 'requested order statistic'
    if number == 239: definitions['k'] = 'window length'
    if number == 787: definitions['k'] = 'maximum allowed stops'
    if number == 295: definitions['n'] = 'stored stream values'
    if number == 703: definitions['k'] = 'retained heap size'
    if number == 212: definitions['L'] = 'maximum word length'
    if number == 74: definitions.update(r='rows', c='columns')
    if number == 22: definitions['C_n'] = 'nth Catalan number'; definitions['n'] = 'parenthesis pairs'
    if number in {50, 7}: definitions['n' if number == 50 else 'x'] = 'exponent' if number == 50 else 'input integer'
    formulas = ' '.join(re.findall(r'\$([^$]+)\$', note['top'].split('## Complexity', 1)[1].strip().split('\n\n', 1)[0]))
    variables = set(re.findall(r'[A-Za-z](?:_n)?', re.sub(r'\\[a-zA-Z]+', ' ', formulas)))
    if '\\alpha' in formulas:
        variables.add('alpha')
    return [f'{symbol} = {meaning}' for symbol, meaning in definitions.items() if symbol in variables]


def wrap(draw, text, font, width):
    lines = []
    for paragraph in text.split('\n'):
        words = paragraph.split()
        line = ''
        for word in words:
            candidate = (line + ' ' + word).strip()
            if line and draw.textlength(candidate, font=font) > width:
                lines.append(line); line = word
            else:
                line = candidate
        lines.append(line)
    return lines


def render(note):
    overview, steps, complexity = details(note)
    pseudo = pseudocode(note)
    canvas = Image.new('RGB', (W, 14000), '#f6f8fc')
    draw = ImageDraw.Draw(canvas)
    y = PAD

    def box(title, lines, font='body', fill='#ffffff', line_height=49):
        nonlocal y
        top = y
        height = 100 + len(lines) * line_height + 34
        draw.rounded_rectangle((PAD, y, W-PAD, y+height), radius=22, fill=fill, outline='#d5e1ed', width=2)
        draw.text((PAD+30, y+25), title, fill=BLUE, font=FONTS['heading'])
        y += 98
        for line in lines:
            assert draw.textlength(line,font=FONTS[font]) <= W-2*PAD-68, (note['number'], title, line)
            draw.text((PAD+34, y), line, fill=NAVY, font=FONTS[font])
            y += line_height
        y = top + height + 24

    title_lines = wrap(draw, note['title'], FONTS['title'], W-2*PAD-60)
    header_lines = [f"LC {note['number']}  •  " + re.search(r'^difficulty:\s*(.+)$', note['header'], re.M).group(1).strip('"')]
    box(header_lines[0], title_lines, 'title', '#e8f1fc', 82)
    box('THE IDEA', wrap(draw, overview, FONTS['body'], W-2*PAD-70))
    logic = []
    for i, step in enumerate(steps, 1):
        wrapped = wrap(draw, f'{i}. {step}', FONTS['body'], W-2*PAD-80)
        logic.extend(wrapped)
    box('LOGIC', logic, fill='#ecf8f5')
    code_lines = []
    for line in pseudo.splitlines():
        indent = len(line) - len(line.lstrip())
        if len(line) <= 64:
            code_lines.append(line)
        else:
            parts = textwrap.wrap(line.lstrip(), width=max(22,60-indent), break_long_words=False, break_on_hyphens=False)
            code_lines.append(' '*indent + parts[0])
            code_lines.extend(' '*(indent+2) + '↪ ' + part for part in parts[1:])
    box('PSEUDOCODE  /  PYTHON-STYLE', code_lines, 'code', '#f0f4fb', 47)
    box('TIME & SPACE COMPLEXITY', wrap(draw, complexity, FONTS['body'], W-2*PAD-70), fill='#fff5e4')
    definitions = glossary(note, complexity)
    if definitions:
        box('SIZE VARIABLES', wrap(draw, ';  '.join(definitions), FONTS['small'], W-2*PAD-70), 'small', line_height=40)
    draw.text((PAD+6,y+5), 'Source implementation and detailed analysis remain below the overview.', fill='#5f7188',font=FONTS['small'])
    y += 65
    if y >= canvas.height:
        raise ValueError('Infographic exceeds render canvas')
    target = ROOT/note['image'];target.parent.mkdir(parents=True,exist_ok=True)
    canvas.crop((0,0,W,y)).save(target,optimize=True)
    return {'path':note['path'],'number':note['number'],'title':note['title'],'image':note['image'],
            'source_sha256':note['sha256'],'image_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
            'width':W,'height':y,'pseudocode':pseudo,'complexity':complexity,'size_variables':definitions}


if __name__ == '__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--numbers',nargs='*',type=int)
    parser.add_argument('--offset', type=int, default=0)
    parser.add_argument('--limit', type=int, default=150)
    parser.add_argument('--quiet', action='store_true')
    args=parser.parse_args();notes=tagged_notes()
    if args.numbers: notes=[note for note in notes if note['number'] in args.numbers]
    else: notes=notes[args.offset:args.offset+args.limit]
    for note in notes:
        result=render(note)
        if not args.quiet:
            print(json.dumps({key:result[key] for key in ['path','number','image','source_sha256','image_sha256','width','height']},ensure_ascii=False),flush=True)
    if args.quiet:
        print(json.dumps({'rendered':len(notes),'text_bounds':'all checked'}))
