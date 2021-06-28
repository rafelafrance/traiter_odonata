"""Extract body part annotations."""

import re

from spacy import registry
from traiter.patterns.matcher_patterns import MatcherPatterns
from traiter.util import squash

from odonata.pylib.const import COMMON_PATTERNS, MISSING, REPLACE

SEG_SPLITTER = re.compile(
    r'(?P<name> [s])\w* \s? (?P<low> \d+) \D+ (?P<high> \d+)', flags=re.VERBOSE)
PARTS = ['part', 'fly']
AND = ['and', '&']

DECODER = COMMON_PATTERNS | {
    'seg9': {'ENT_TYPE': {'IN': ['abdomen_seg', 'segments']}},
    'part': {'ENT_TYPE': {'IN': PARTS}},
    'subpart': {'ENT_TYPE': 'subpart'},
    'loc': {'ENT_TYPE': 'part_loc'},
    'prep': {'POS': 'ADP'},
    'seg_word': {'LOWER': {'IN': ['segment', 'segments']}},
    '9-9': {'ENT_TYPE': 'range'},
    'and': {'LOWER': {'IN': AND}},
}

BODY_PART = MatcherPatterns(
    'body_part',
    on_match='odonata.body_part.v1',
    decoder=DECODER,
    patterns=[
        'missing? part',
        'loc prep? part',
        'part subpart',
        'loc? prep? subpart? part and part subpart?',
    ])

BODY_SUBPART = MatcherPatterns(
    'body_subpart',
    on_match='odonata.body_subpart.v1',
    decoder=DECODER,
    patterns=[
        'subpart+',
        'loc+',
        'loc+ subpart+',
        'loc+ prep loc+',
    ],
)

BODY_SEGMENTS = MatcherPatterns(
    'body_segments',
    on_match='odonata.segment.v1',
    decoder=DECODER,
    patterns=[
        'seg9',
        'seg9 - seg9',
        'seg_word 99',
        'seg_word 9-9',
    ])


@registry.misc(BODY_SEGMENTS.on_match)
def segment(ent):
    """Enrich the match."""
    data = {}
    ent._.new_label = 'body_part'
    lower = ent.text.lower()
    if match := re.match(SEG_SPLITTER, lower):
        low, high = int(match.group('low')), int(match.group(3))
        low, high = (low, high) if high > low else (high, low)
        data['body_part'] = [f'{match.group("name")}{i}' for i in range(low, high + 1)]
    else:
        data['body_part'] = lower
    ent._.data = data


@registry.misc(BODY_PART.on_match)
def body_part(ent):
    """Enrich the match."""
    data = {}

    parts = []
    part = []
    for token in ent:
        label = token._.cached_label
        lower = REPLACE.get(token.lower_, token.lower_)
        if label in PARTS:
            part.insert(0, lower)
        elif label == 'subpart':
            part.append(lower)
        elif label == 'part_loc':
            part.append(lower)
        elif lower in MISSING:
            part.append('missing')
            data['missing'] = True
        elif lower in AND:
            parts.append(' '.join(part))
            part = []

    parts.append(' '.join(part))
    data['body_part'] = squash(parts)

    ent._.data = data


@registry.misc(BODY_SUBPART.on_match)
def body_subpart(ent):
    """Enrich the match."""
    lower = ent.text.lower()
    ent._.data = {'body_subpart': REPLACE.get(lower, lower)}
