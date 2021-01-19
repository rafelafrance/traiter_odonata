"""Link traits to body parts."""

import spacy

TRAITS = ['color', 'color_mod']

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
                    'RIGHT_ID': 'prep_link',
                    'RIGHT_ATTRS': {'DEP': 'prep'},
                },
                {
                    'LEFT_ID': 'prep_link',
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
                    'RIGHT_ID': 'prep_link',
                    'RIGHT_ATTRS': {'DEP': 'prep'},
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
                    'RIGHT_ATTRS': {'ENT_TYPE': {'IN': TRAITS}, 'OP': '?'},
                },
            ],
        ],
    },
]


@spacy.registry.misc(BODY_PART_LINKER[0]['on_match'])
def body_part_linker(_, doc, idx, matches):
    """Use an entity matcher for entity linking."""
    ents = {}
    for i in matches[idx][1]:
        for ent in doc.ents:
            if ent.start <= i <= ent.end - 1:
                ents[i] = ent
                break
    root, *others = ents.values()
    body_part = root._.data['body_part']
    for ent in others:
        ent._.data['body_part'] = body_part
