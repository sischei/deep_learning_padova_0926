#!/usr/bin/env python3
"""Replace LaTeX em-dashes (---) with commas in prose and colons in titles.

En-dashes (--) are left alone: they are correct in name compounds such as
Brock--Mirman and in ranges such as 1471--1525.  Comment lines are skipped,
so the "% --- Slide 5 ---" separators survive untouched.

usage: dedash.py FILE.tex [FILE.tex ...]
"""
import re
import sys

TITLE_LINE = re.compile(r'^\s*\\(?:begin\{(?:frame|block|alertblock|exampleblock)\}|section\{|subtitle\{)')
# after an em-dash, these words read better with a comma than a colon
CONJ = re.compile(r'\s*(and|or|but|not|so|yet|then|with|without|no\b)\b', re.I)


def fix_line(line):
    if line.lstrip().startswith('%'):          # comment / separator line
        return line, 0
    n = line.count('---')
    if not n:
        return line, 0
    sep = ': ' if (TITLE_LINE.match(line) and not CONJ.match(line.split('---', 1)[1])) else ', '

    def sub(m):
        tail = m.group(2)
        s = sep
        if TITLE_LINE.match(line) and CONJ.match(tail):
            s = ', '
        return s.rstrip() + (' ' if tail.startswith(' ') or not tail else '') + tail.lstrip(' ')

    # " --- ", "---", " ---" and "--- " all collapse to one separator
    line = re.sub(r'[ \t]*---[ \t]*(\n?)$', lambda m: sep.rstrip() + m.group(1), line)   # end of line
    line = re.sub(r'()[ \t]*---[ \t]*()', lambda m: sep, line)
    line = line.replace(',,', ',').replace(', ,', ',').replace(': ,', ': ').replace(',:', ':')
    return line, n


def main():
    for path in sys.argv[1:]:
        out, total = [], 0
        for line in open(path):
            new, n = fix_line(line)
            out.append(new)
            total += n
        if total:
            open(path, 'w').writelines(out)
            print('%-46s %4d em-dashes replaced' % (path.split('/')[-1], total))


if __name__ == '__main__':
    main()
