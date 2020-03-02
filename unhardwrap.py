#!/usr/bin/env python3
import sys

def has_open_speachmark(line, currently_has_open):
    index_open = line.rfind("“")
    index_close = line.rfind("”")
    if index_open == -1:
        if index_close == -1:
            return currently_has_open
        return False
    if index_open > index_close:
        return True
    return False

data = []
paragraph = []
currently_has_open_speachmark = False
for line in sys.stdin:
    line = line.strip()
    currently_has_open_speachmark = has_open_speachmark(line, currently_has_open_speachmark)
    if currently_has_open_speachmark:
        endparagraph = False
        startparagraph = False
    else:
        endparagraph = (not line) or (not line[-1].isalpha() and line[-1] != ',' and line[-1] != '-')
        startparagraph = line.startswith(' ') or line.startswith("“")

    if not startparagraph:
        paragraph.append(line)
    if endparagraph or startparagraph:
        data.append(' '.join(paragraph).replace('  ', ' '))
        paragraph = []
    if startparagraph:
        paragraph.append(line)

print('\n'.join(data))
