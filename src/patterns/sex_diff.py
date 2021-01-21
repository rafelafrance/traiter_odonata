"""Sex terms."""

from collections import defaultdict

import spacy
from traiter.pipes.entity_data import text_action

from ..pylib.consts import REPLACE

SIMILAR = """ like similar as than """.split()
TRAITS = ['color', 'color_mod', 'body_part', 'body_part_loc']
LINKERS = ['prep', 'conj', 'cc']

SEX_DIFF = [
    {
        'label': 'sex_diff',
        'on_match': 'sex_diff.v1',
        'patterns': [
            [
                {'LOWER': {'IN': SIMILAR}},
                {'POS': {'IN': ['ADP']}, 'OP': '?'},
                {'ENT_TYPE': 'sex'},
                {'POS': {'IN': ['CCONJ']}, 'OP': '?'},
            ],
            [
                {'POS': {'IN': ['SCONJ', 'ADP']}},
                {'POS': {'IN': ['DET']}, 'OP': '?'},
                {'POS': {'IN': ['ADP']}},
                {'ENT_TYPE': 'sex'},
            ],
        ],
    },
]

SEX_DIFF_LINKER = [
    {
        'label': 'sex_diff_linker',
        'on_match': 'sex_diff_linker.v1',
        'patterns': [
            # Sex diff is next to the trait
            [
                {
                    'RIGHT_ID': 'sex_diff',
                    'RIGHT_ATTRS': {'ENT_TYPE': 'sex_diff'},
                },
                {
                    'LEFT_ID': 'sex_diff',
                    'REL_OP': '.',
                    'RIGHT_ID': 'trait1',
                    'RIGHT_ATTRS': {'ENT_TYPE': {'IN': TRAITS}},
                },
            ],
            [
                {
                    'RIGHT_ID': 'sex_diff',
                    'RIGHT_ATTRS': {'ENT_TYPE': 'sex_diff'},
                },
                {
                    'LEFT_ID': 'sex_diff',
                    'REL_OP': '.',
                    'RIGHT_ID': 'trait1',
                    'RIGHT_ATTRS': {'ENT_TYPE': {'IN': TRAITS}},
                },
                {
                    'LEFT_ID': 'trait1',
                    'REL_OP': '>',
                    'RIGHT_ID': 'trait2',
                    'RIGHT_ATTRS': {'ENT_TYPE': {'IN': TRAITS}},
                },
            ],
            # Sex diff is the parent of the trait
            [
                {
                    'RIGHT_ID': 'sex_diff',
                    'RIGHT_ATTRS': {'ENT_TYPE': 'sex_diff'},
                },
                {
                    'LEFT_ID': 'sex_diff',
                    'REL_OP': '>',
                    'RIGHT_ID': 'trait',
                    'RIGHT_ATTRS': {'ENT_TYPE': {'IN': TRAITS}},
                },
            ],
            # Sex diff is the child of the trait
            [
                {
                    'RIGHT_ID': 'sex_diff',
                    'RIGHT_ATTRS': {'ENT_TYPE': 'sex_diff'},
                },
                {
                    'LEFT_ID': 'sex_diff',
                    'REL_OP': '<',
                    'RIGHT_ID': 'trait',
                    'RIGHT_ATTRS': {'ENT_TYPE': {'IN': TRAITS}},
                },
            ],
            # Sex diff is the grandchild of the trait
            [
                {
                    'RIGHT_ID': 'sex_diff',
                    'RIGHT_ATTRS': {'ENT_TYPE': 'sex_diff'},
                },
                {
                    'LEFT_ID': 'sex_diff',
                    'REL_OP': '<',
                    'RIGHT_ID': 'linker',
                    'RIGHT_ATTRS': {'DEP': {'IN': LINKERS}},
                },
                {
                    'LEFT_ID': 'linker',
                    'REL_OP': '<',
                    'RIGHT_ID': 'trait1',
                    'RIGHT_ATTRS': {'ENT_TYPE': {'IN': TRAITS}},
                },
            ],
            [
                {
                    'RIGHT_ID': 'sex_diff',
                    'RIGHT_ATTRS': {'ENT_TYPE': 'sex_diff'},
                },
                {
                    'LEFT_ID': 'sex_diff',
                    'REL_OP': '<',
                    'RIGHT_ID': 'linker',
                    'RIGHT_ATTRS': {'DEP': {'IN': LINKERS}},
                },
                {
                    'LEFT_ID': 'linker',
                    'REL_OP': '<',
                    'RIGHT_ID': 'trait1',
                    'RIGHT_ATTRS': {'ENT_TYPE': {'IN': TRAITS}},
                },
                {
                    'LEFT_ID': 'trait1',
                    'REL_OP': '<',
                    'RIGHT_ID': 'trait2',
                    'RIGHT_ATTRS': {'ENT_TYPE': {'IN': TRAITS}},
                },
            ],
            # Sex diff is the grandparent of the trait
            [
                {
                    'RIGHT_ID': 'sex_diff',
                    'RIGHT_ATTRS': {'ENT_TYPE': 'sex_diff'},
                },
                {
                    'LEFT_ID': 'sex_diff',
                    'REL_OP': '>',
                    'RIGHT_ID': 'prep_link',
                    'RIGHT_ATTRS': {'DEP': {'IN': LINKERS}},
                },
                {
                    'LEFT_ID': 'prep_link',
                    'REL_OP': '>',
                    'RIGHT_ID': 'trait1',
                    'RIGHT_ATTRS': {'ENT_TYPE': {'IN': TRAITS}},
                },
            ],
            [
                {
                    'RIGHT_ID': 'sex_diff',
                    'RIGHT_ATTRS': {'ENT_TYPE': 'sex_diff'},
                },
                {
                    'LEFT_ID': 'sex_diff',
                    'REL_OP': '>',
                    'RIGHT_ID': 'prep_link',
                    'RIGHT_ATTRS': {'DEP': {'IN': LINKERS}},
                },
                {
                    'LEFT_ID': 'prep_link',
                    'REL_OP': '>',
                    'RIGHT_ID': 'trait1',
                    'RIGHT_ATTRS': {'ENT_TYPE': {'IN': TRAITS}},
                },
                {
                    'LEFT_ID': 'trait1',
                    'REL_OP': '>',
                    'RIGHT_ID': 'trait2',
                    'RIGHT_ATTRS': {'ENT_TYPE': {'IN': TRAITS}},
                },
            ],
        ]
    },
]


@spacy.registry.misc(SEX_DIFF[0]['on_match'])
def sex_diff(ent):
    """Enrich the match."""
    text_action(ent, REPLACE)


@spacy.registry.misc(SEX_DIFF_LINKER[0]['on_match'])
def sex_diff_linker(_, doc, idx, matches):
    """Link traits to the sex diff trait."""
    match_ents = defaultdict(list)
    for ent in doc.ents:
        for k, i in enumerate(matches[idx][1]):
            if ent.start <= i < ent.end:
                match_ents[ent].append(k)
                break
    match_ents = dict(sorted(match_ents.items(), key=lambda x: min(x[1])))
    root, *others = match_ents.keys()
    body_part = root._.data['sex_diff']
    for ent in others:
        ent._.data['sex_diff'] = body_part
