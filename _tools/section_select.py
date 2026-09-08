#!/usr/bin/env python3
"""Produce a re-cut beamer deck by keeping a chosen subset of top-level \section blocks.

Content is never rewritten: the preamble, front matter and the selected section
blocks are copied verbatim, and the dropped blocks are emitted as commented-out
provenance so the result stays diffable against the source deck.
"""
import re
import sys


def split_sections(lines):
    """Return (head, [(title, block), ...], tail)."""
    sec_idx = [i for i, l in enumerate(lines)
               if re.match(r'^\\section\{', l)]
    if not sec_idx:
        raise SystemExit('no top-level \\section found')
    end_idx = next(i for i, l in enumerate(lines)
                   if l.startswith(r'\end{document}'))
    head = lines[:sec_idx[0]]
    tail = lines[end_idx:]
    bounds = sec_idx + [end_idx]
    blocks = []
    for a, b in zip(bounds, bounds[1:]):
        title = re.match(r'^\\section\{(.*)\}\s*$', lines[a]).group(1)
        blocks.append((title, lines[a:b]))
    return head, blocks, tail


def main():
    src, dst, keep_spec = sys.argv[1], sys.argv[2], sys.argv[3]
    keep = {int(k) for k in keep_spec.split(',')}
    with open(src) as fh:
        lines = fh.readlines()
    head, blocks, tail = split_sections(lines)

    out = list(head)
    for n, (title, block) in enumerate(blocks, start=1):
        if n in keep:
            out.extend(block)
        else:
            out.append('%% --- Padova cut: section %d "%s" (%d lines) dropped ---\n'
                       % (n, title, len(block)))
    out.extend(tail)
    with open(dst, 'w') as fh:
        fh.writelines(out)

    for n, (title, block) in enumerate(blocks, start=1):
        print('%s %d  %-45s %4d lines' %
              ('KEEP' if n in keep else 'drop', n, title[:45], len(block)))


if __name__ == '__main__':
    main()
