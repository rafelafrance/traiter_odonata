"""Custom sentence splitter."""

import regex

ABBREVS = '|'.join("""
    Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
    mm cm m
    """.split())
ABBREVS = regex.compile(fr'(?: {ABBREVS} ) $', flags=regex.VERBOSE)


def sentencizer(doc):
    """Break the text into sentences."""
    for i, token in enumerate(doc[:-1]):
        prev_token = doc[i - 1] if i > 0 else None
        next_token = doc[i + 1]
        if (token.text == '.' and regex.match(r'[A-Z]', next_token.prefix_)
                and not ABBREVS.match(next_token.text)
                and len(next_token) > 2 and len(prev_token) > 2):
            next_token.is_sent_start = True
        else:
            next_token.is_sent_start = False

    return doc
