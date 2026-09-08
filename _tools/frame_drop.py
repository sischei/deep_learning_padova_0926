#!/usr/bin/env python3
"""Comment out named beamer frames in place, keeping them as provenance.

Companion to section_select.py for cuts finer than a \\section: each dropped
frame is left in the file with every line prefixed by "% ", under a marker,
so the deck stays diffable against its source and the cut can be reversed
by deleting the prefix.

usage: frame_drop.py DECK.tex 'Frame title one' 'Frame title two' ...
Titles match as case-insensitive substrings of the frame title.
"""
import re
import sys

FRAME_RE = re.compile(r'^\\begin\{frame\}(?:\[[^\]]*\])?\{(.*?)\}\s*$')


def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())


def main():
    path, wanted = sys.argv[1], [norm(w) for w in sys.argv[2:]]
    lines = open(path).readlines()
    out, i, dropped = [], 0, []
    while i < len(lines):
        m = FRAME_RE.match(lines[i])
        if m and any(w in norm(m.group(1)) for w in wanted):
            j = i
            while not lines[j].startswith(r'\end{frame}'):
                j += 1
            block = lines[i:j + 1]
            out.append('%% --- Padova cut: frame "%s" (%d lines) commented out ---\n'
                       % (m.group(1), len(block)))
            out.extend('% ' + l for l in block)
            dropped.append(m.group(1))
            i = j + 1
        else:
            out.append(lines[i])
            i += 1
    open(path, 'w').writelines(out)
    for t in dropped:
        print('dropped:', t)
    missing = [w for w in sys.argv[2:] if not any(w and norm(w) in norm(t) for t in dropped)]
    for w in missing:
        sys.stderr.write('NOT FOUND: %s\n' % w)


if __name__ == '__main__':
    main()
