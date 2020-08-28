"""Custom sentence splitter."""

import regex

from ..matchers.shared import QUOTE

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
        if (token.text in '.?!)' and next_token.prefix_.isupper()
                and not ABBREVS.match(next_token.text)):
            next_token.is_sent_start = True
        elif (prev_token and prev_token.text == '.' and token.text in QUOTE
              and next_token.prefix_.isupper()):
            next_token.is_sent_start = True
        else:
            next_token.is_sent_start = False

    return doc
