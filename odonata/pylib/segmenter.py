"""Clean the PDF file."""

import regex
from collections import Counter

FLAGS = regex.MULTILINE | regex.VERBOSE


def clean_pdf(text):
    """Remove headers & footers and join hyphenated words etc."""
    # Clean up chars
    # text = text.translate(TRANS)

    # Search for headers and footers
    lines = []
    for ln in text.split('\n'):
        ln = regex.sub(r'^\s*\d+|\d+\s*$', ' ', ln)
        ln = ' '.join(ln.split())
        if len(ln) > 3:
            lines.append(ln)
    counts = Counter(lines)

    pages = text.count('\f')
    remove = []
    for ln, n in counts.most_common(4):
        if n >= pages / 2:
            pattern = regex.sub(r'\s+', r'\s*', ln)
            pattern = fr'^ [\s\d]* {pattern} [\s\d]* $'
            remove.append(pattern)

    # Remove headers and footers
    for pattern in remove:
        text = regex.sub(pattern, '', text, flags=FLAGS)

    lines = []
    for ln in text.split('\n'):
        ln = ' '.join(ln.split())
        if len(ln):
            lines.append(ln)

    lines = '\n'.join(lines)

    return lines

    # # Remove figure notations
    # text = re.sub(r'^ \s* Fig\. .+ $', '', text, flags=FLAGS)
    #
    # # Joining hyphens has to happen after the removal of headers & footers
    # text = re.sub(r' [–-] \n ([a-z]) ', r'\1', text, flags=FLAGS)
    #
    # Space normalize text
    # return ' '.join(text.split())
    # return text
