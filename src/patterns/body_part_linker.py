"""Link traits to body parts."""

from collections import defaultdict

import spacy

TRAITS = ['color', 'color_mod']
LINKER = ['']

BODY_PART_LINKER = [
    {
        'label': 'body_part_linker',
        'on_match': 'body_part_linker.v1',
        'patterns': [
            # Body part is the parent of the trait
            [
                {
                    'RIGHT_ID': 'body_part',
                    'RIGHT_ATTRS': {'ENT_TYPE': 'body_part'},
                },
                {
                    'LEFT_ID': 'body_part',
                    'REL_OP': '>',
                    'RIGHT_ID': 'trait',
                    'RIGHT_ATTRS': {'ENT_TYPE': {'IN': TRAITS}},
                },
            ],
            # Body part is the child of the trait
            [
                {
                    'RIGHT_ID': 'body_part',
                    'RIGHT_ATTRS': {'ENT_TYPE': 'body_part'},
                },
                {
                    'LEFT_ID': 'body_part',
                    'REL_OP': '<',
                    'RIGHT_ID': 'trait',
                    'RIGHT_ATTRS': {'ENT_TYPE': {'IN': TRAITS}},
                },
            ],
            # Body part is the grandchild of the trait
            [
                {
                    'RIGHT_ID': 'body_part',
                    'RIGHT_ATTRS': {'ENT_TYPE': 'body_part'},
                },
                {
                    'LEFT_ID': 'body_part',
                    'REL_OP': '<',
                    'RIGHT_ID': 'linker',
                    'RIGHT_ATTRS': {'DEP': 'prep'},
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
                    'RIGHT_ATTRS': {'ENT_TYPE': {'IN': TRAITS}, 'OP': '?'},
                },
            ],
            # Body part is the grandparent of the trait
            [
                {
                    'RIGHT_ID': 'body_part',
                    'RIGHT_ATTRS': {'ENT_TYPE': 'body_part'},
                },
                {
                    'LEFT_ID': 'body_part',
                    'REL_OP': '>',
                    'RIGHT_ID': 'linker',
                    'RIGHT_ATTRS': {'DEP': 'prep'},
                },
                {
                    'LEFT_ID': 'linker',
                    'REL_OP': '>',
                    'RIGHT_ID': 'trait1',
                    'RIGHT_ATTRS': {'ENT_TYPE': {'IN': TRAITS}},
                },
                {
                    'LEFT_ID': 'trait1',
                    'REL_OP': '>',
                    'RIGHT_ID': 'trait2',
                    'RIGHT_ATTRS': {'ENT_TYPE': {'IN': TRAITS}, 'OP': '?'},
                },
            ],
        ],
    },
]


@spacy.registry.misc(BODY_PART_LINKER[0]['on_match'])
def body_part_linker(_, doc, idx, matches):
    """Use an entity matcher for entity linking."""
    match_ents = defaultdict(list)
    for ent in doc.ents:
        for k, i in enumerate(matches[idx][1]):
            if ent.start <= i < ent.end:
                match_ents[ent].append(k)
                break
    match_ents = dict(sorted(match_ents.items(), key=lambda x: min(x[1])))
    root, *others = match_ents.keys()
    body_part = root._.data['body_part']
    for ent in others:
        ent._.data['body_part'] = body_part
