#!/usr/bin/env python3
"""Pull selected beamer frames verbatim out of a source deck.

Frames are addressed by their title text (substring match, case-insensitive)
so a re-cut deck can be rebuilt from its sources without hand-copying slides.
"""
import re
import sys


FRAME_RE = re.compile(r'^\\begin\{frame\}')


def frames(path):
    """Yield (title, [lines]) for every frame in the deck."""
    lines = open(path).readlines()
    out = []
    i = 0
    while i < len(lines):
        if FRAME_RE.match(lines[i]):
            depth = 0
            j = i
            while j < len(lines):
                depth += lines[j].count(r'\begin{frame}')
                depth -= lines[j].count(r'\end{frame}')
                if depth == 0 and j > i:
                    break
                j += 1
            block = lines[i:j + 1]
            m = re.match(r'^\\begin\{frame\}(?:\[[^\]]*\])?\{(.*?)\}\s*$', lines[i])
            title = m.group(1) if m else ''
            out.append((title, block))
            i = j + 1
        else:
            i += 1
    return out


def norm(s):
    s = re.sub(r'\\[a-zA-Z]+\{?|\}|\$|~|\\', ' ', s)
    return re.sub(r'[^a-z0-9 ]', ' ', s.lower())


def main():
    src, wanted_file = sys.argv[1], sys.argv[2]
    wanted = [w.strip() for w in open(wanted_file) if w.strip()
              and not w.startswith('#')]
    have = frames(src)
    for w in wanted:
        key = norm(w)
        hit = next((b for t, b in have if key in norm(t)), None)
        if hit is None:
            sys.stderr.write('MISSING: %s\n' % w)
            continue
        sys.stdout.writelines(hit)
        sys.stdout.write('\n')
        sys.stderr.write('ok: %s\n' % w)


if __name__ == '__main__':
    main()
