"""Extract body part annotations."""

import spacy
from traiter.const import DASH_RE

from odonata.pylib.const import MISSING, REPLACE
from odonata.pylib.token import COMPILE

PART = ['part', 'fly']
ANY_PART_ = PART + ['part_loc']
AS_PART_ = PART + ['abdomen_seg', 'segments']

PART_MOD = """ fine thick broad thin narrow irregular moderate unmarked """.split()
BOTH = """ both either """.split()

MAP = {
    'adp': {'POS': 'ADP'},
    'any_part+': {'ENT_TYPE': {'IN': ANY_PART_}, 'OP': '+'},
    'any_part*': {'ENT_TYPE': {'IN': ANY_PART_}, 'OP': '*'},
    'both': {'LOWER': {'IN': BOTH}},
    'both?': {'LOWER': {'IN': BOTH}, 'OP': '?'},
    'cconj': {'POS': {'IN': ['ADP', 'CCONJ']}},
    'n-seg': {'ENT_TYPE': {'IN': ['abdomen_seg', 'stripe', 'segments']}},
    'part+': {'ENT_TYPE': {'IN': PART}, 'OP': '+'},
    'part_mod': {'LOWER': {'IN': PART_MOD}},
    'part_mod?': {'LOWER': {'IN': PART_MOD}, 'OP': '?'},
    'segments': {'LOWER': {'REGEX': fr'^s\d+{DASH_RE}\d+$'}},
}

SEGMENTS = [
    {
        'label': 'segments',
        'patterns': COMPILE.to_patterns(MAP, 'segments')
    }
]

BODY_PART = [
    {
        'label': 'body_part',
        'on_match': 'body_part.v1',
        'patterns': COMPILE.to_patterns(
            MAP,
            'both? any_part+ cconj any_part+ cconj any_part+',
            'both? any_part+ cconj any_part+ cconj any_part*',
            'both? any_part+ cconj any_part+',
            'a-z+ - any_part+',
            'missing? any_part+',
            'missing? any_part* part_mod? part+',
            'missing? both any_part+ adp part+',
            'missing? both part+ adp any_part+',
            'missing? part_mod ,? part_mod part+',
            'missing? part_mod part+ , any_part+',
            'missing? part_mod part+',
            'n-seg - 0-9+',
            'n-seg - n-seg',
            'part_mod? n-seg',
        ),
    },
]


@spacy.registry.misc(BODY_PART[0]['on_match'])
def body_part(ent):
    """Enrich the match."""
    data = {}

    if any(t for t in ent if t.lower_ in MISSING):
        data['missing'] = True

    label = 'body_part'
    if not any(t for t in ent if t._.cached_label in AS_PART_):
        label = 'body_part_loc'
        ent._.new_label = label

    lower = ent.text.lower()
    data[label] = REPLACE.get(lower, lower)

    ent._.data = data
