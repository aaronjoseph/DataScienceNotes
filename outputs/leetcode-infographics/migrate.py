"""Prepare apply_patch diffs or validate the migration; no note writes."""
import argparse
import difflib
import hashlib
import json
import re
from pathlib import Path
from prepare import ROOT


def records():
    originals = ROOT/'outputs/leetcode-infographics/.originals'
    result=[]
    for source in originals.rglob('*.md'):
        old=source.read_text();path=source.relative_to(originals)
        if not re.search(r'^\s*-\s*[\"\']?leetcode[\"\']?\s*$',old.split('---',2)[1],re.M):continue
        number=int(re.search(r'^problem_number:\s*(\d+)',old,re.M).group(1))
        t=old.index('\n## Template');o=old.index('\n## Overview',t);r=old.index('\n## References & Useful Links',o)
        image=f'Attachements/LeetCode/LC{number:04d} - {source.stem}.png'
        new=old[:t]+'\n## Algorithm at a glance\n\n![[ '+image+'|700]]\n'+old[o:r]+old[t:o]+old[r:]
        new=new.replace('![[ Attachements/','![[Attachements/')
        if number == 704:
            new = new.replace('**Three Templates → 1. Exact Match in a Sorted Array** above.', '**Three Templates → 1. Exact Match in a Sorted Array** below.')
        result.append({'path':path.as_posix(),'number':number,'old':old,'new':new,'image':image})
    return sorted(result,key=lambda row:row['number'])


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--offset',type=int,default=0)
    parser.add_argument('--limit',type=int,default=10);parser.add_argument('--validate',action='store_true')
    args=parser.parse_args();rows=records()
    if args.validate:
        count=0
        for row in rows:
            current=(ROOT/row['path']).read_text();assert current==row['new'],row['path']
            assert (ROOT/row['image']).is_file(),row['image']
            assert current.split('---',2)[1]==row['old'].split('---',2)[1]
            for heading in re.findall(r'^#{2,6} .+$',row['old'],re.M):assert heading in current
            assert current.count('```')==row['old'].count('```')
            assert current.count('\n$$\n')==row['old'].count('\n$$\n')
            assert current.rfind('\n## ')==current.index('\n## References & Useful Links')
            count+=1
        print(json.dumps({'validated_notes':count,'preserved':'original content, metadata, headings, code, math, links, and references'}))
    else:
        patch='*** Begin Patch\n';changed=[]
        for row in rows[args.offset:args.offset+args.limit]:
            current=(ROOT/row['path']).read_text()
            if current==row['new']:continue
            assert current==row['old'],f"Concurrent edit detected: {row['path']}"
            assert (ROOT/row['image']).is_file(),row['image']
            diff=list(difflib.unified_diff(row['old'].splitlines(),row['new'].splitlines(),n=3,lineterm=''))[2:]
            patch+='*** Update File: '+str(ROOT/row['path'])+'\n'
            patch+='\n'.join('@@' if line.startswith('@@ ') else line for line in diff)+'\n'
            changed.append(row['path'])
        patch+='*** End Patch'
        print(json.dumps({'patch':patch,'changed':changed}))
