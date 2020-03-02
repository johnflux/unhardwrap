#!/usr/bin/env python3
import sys

def has_open_speechmark(line, currently_has_open):
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
currently_has_open_speechmark = False
for line in sys.stdin:
    line = line.strip()
    currently_has_open_speechmark = has_open_speechmark(line, currently_has_open_speechmark)
    if currently_has_open_speechmark:
        endparagraph = False
        startparagraph = False
    else:
        endparagraph = (not line) or ((not line[-1].isalpha()) and line[-1] != ',' and line[-1] != '-')
        startparagraph = line.startswith(' ') or line.startswith("“")

    if startparagraph and paragraph:
        # First make sure we end the previous paragraph
        data.append(' '.join(paragraph).replace('  ', ' '))
        paragraph = []
    paragraph.append(line)
    if endparagraph:
        data.append(' '.join(paragraph).replace('  ', ' '))
        paragraph = []

data.append(' '.join(paragraph).replace('  ', ' '))
print('\n'.join(data))
