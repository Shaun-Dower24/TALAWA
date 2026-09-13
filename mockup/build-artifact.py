#!/usr/bin/env python3
"""Inline every assets/ file as a data URI - photographs and webfonts alike.

Artifacts are published as a single file and their CSP blocks external images,
so the published copy needs its assets embedded. index.html keeps normal
assets/... references, which is what a real deploy should ship.

The fonts are inlined by the same rule that catches the photos: url('assets/...')
matches the pattern, and mimetypes already knows .woff2 is font/woff2. Worth
stating because the fonts matter more than they look - they are served from this
site rather than Google precisely so that what gets tested is what gets shipped.
"""
import base64, mimetypes, os, re, sys

here = os.path.dirname(os.path.abspath(__file__))
html = open(os.path.join(here, 'index.html'), encoding='utf-8').read()

def inline(match):
    quote, path = match.group(1), match.group(2)
    full = os.path.join(here, path)
    mime = mimetypes.guess_type(full)[0] or 'image/jpeg'
    with open(full, 'rb') as fh:
        data = base64.b64encode(fh.read()).decode('ascii')
    return '%s%sdata:%s;base64,%s' % (match.group(0)[:match.start(1)-match.start(0)], quote, mime, data)

out = re.sub(r'(["\'(])(assets/[^"\')]+)', inline, html)
assert 'assets/' not in out, 'an asset reference was left un-inlined'

dest = os.path.join(here, 'artifact.html')
open(dest, 'w', encoding='utf-8').write(out)
print('artifact.html %d KB (index.html %d KB)' % (len(out.encode()) // 1024, len(html.encode()) // 1024))
