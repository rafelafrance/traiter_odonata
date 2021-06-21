"""Extract body part annotations."""

import re

from spacy import registry
from traiter.patterns.matcher_patterns import MatcherPatterns

from odonata.pylib.const import COMMON_PATTERNS, MISSING, REPLACE

SEG_SPLITTER = re.compile(
    r'(?P<name> [s]) (?P<low> \d+) \D+ (?P<high> \d+)', flags=re.VERBOSE)

DECODER = COMMON_PATTERNS | {
    'seg9': {'ENT_TYPE': {'IN': ['abdomen_seg', 'segments']}},
    'part': {'ENT_TYPE': {'IN': ['part', 'fly']}},
    'subpart': {'ENT_TYPE': 'subpart'},
    'part_loc': {'ENT_TYPE': 'part_loc'},
    'prep': {'POS': 'ADP'},
}

BODY_PART = MatcherPatterns(
    'body_part',
    on_match='odonata.body_part.v1',
    decoder=DECODER,
    patterns=[
        'missing? part',
        'part_loc prep? part',
        'part subpart',
    ])

BODY_SUBPART = MatcherPatterns(
    'body_subpart',
    on_match='odonata.body_subpart.v1',
    decoder=DECODER,
    patterns=[
        'subpart+',
        'part_loc+',
        'part_loc+ subpart+',
        'part_loc+ prep part_loc+',
    ],
)

BODY_SEGMENTS = MatcherPatterns(
    'body_segments',
    on_match='odonata.segment.v1',
    decoder=DECODER,
    patterns=[
        'seg9',
        'seg9 - seg9',
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

    if any(t for t in ent if t.lower_ in MISSING):
        data['missing'] = True

    lower = ent.text.lower()
    data['body_part'] = REPLACE.get(lower, lower)

    ent._.data = data


@registry.misc(BODY_SUBPART.on_match)
def body_subpart(ent):
    """Enrich the match."""
    lower = ent.text.lower()
    ent._.data = {'body_subpart': REPLACE.get(lower, lower)}
