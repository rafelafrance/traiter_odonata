"""Link traits to body parts."""

import spacy

BODY_PART_LINKER = {
    'label': 'body_part_linker',
    'on_match': 'body_part_linker.v1',
    'patterns': [
        [
            {
                'RIGHT_ID': 'body_part',
                'RIGHT_ATTRS': {'ENT_TYPE': 'body_part'},
            },
            {
                'LEFT_ID': 'body_part',
                'REL_OP': '>',
                'RIGHT_ID': 'trait',
                'RIGHT_ATTRS': {'ENT_TYPE': 'color'},
            },
        ],
    ],
}


@spacy.registry.misc(BODY_PART_LINKER['on_match'])
def body_part_linker(_, doc, idx, matches):
    """Use an entity matcher for entity linking."""
    print(doc)
    print(idx)
    print(matches)

# BODY_PARTS = """ body_part body_part_loc sex_diff """.split()
# COLORS = """ color color_mod """.split()
# FILLER_POS = """ CCONJ VERB AUX """.split()
# LINKER = """ often sometimes normally usually """.split()


# BODY_PART_LINKER = [
#     {
#         'label': 'body_part_linker',
#         'action': linker,
#         'patterns': [
#             [
#                 {'ENT_TYPE': {'IN': COLORS}, 'OP': '+'},
#                 {'POS': {'IN': FILLER_POS}, 'OP': '?'},
#                 {'POS': {'IN': FILLER_POS}, 'OP': '?'},
#                 {'POS': {'IN': FILLER_POS}, 'OP': '?'},
#                 {'ENT_TYPE': {'IN': BODY_PARTS}},
#             ],
#             [
#                 {'ENT_TYPE': {'IN': BODY_PARTS}},
#                 {'POS': {'IN': FILLER_POS}, 'OP': '?'},
#                 {'POS': {'IN': FILLER_POS}, 'OP': '?'},
#                 {'POS': {'IN': FILLER_POS}, 'OP': '?'},
#                 {'ENT_TYPE': {'IN': COLORS}, 'OP': '+'},
#             ],
#             [
#                 {'ENT_TYPE': {'IN': BODY_PARTS}},
#                 {'ENT_TYPE': {'IN': COLORS}, 'OP': '+'},
#                 {'POS': {'IN': FILLER_POS}, 'OP': '?'},
#                 {'POS': {'IN': FILLER_POS}, 'OP': '?'},
#                 {'POS': {'IN': FILLER_POS}, 'OP': '?'},
#                 {'ENT_TYPE': {'IN': COLORS}, 'OP': '+'},
#             ],
#             [
#                 {'ENT_TYPE': {'IN': COLORS}, 'OP': '+'},
#                 {'POS': {'IN': ['ADP']}},
#                 {'ENT_TYPE': {'IN': BODY_PARTS}},
#             ],
#             [
#                 {'POS': {'IN': ['ADP']}},
#                 {'ENT_TYPE': {'IN': COLORS}, 'OP': '+'},
#                 {'ENT_TYPE': {'IN': BODY_PARTS}},
#             ],
#             [
#                 {'ENT_TYPE': {'IN': BODY_PARTS}},
#                 {'LOWER': {'IN': LINKER}},
#                 {'ENT_TYPE': {'IN': COLORS}, 'OP': '+'},
#             ],
#         ],
#     },
# ]


# def linker(span):
#     """Link body parts to traits."""
#     part = [t for t in span if t.ent_type_ in BODY_PARTS][0]
#     for token in span:
#         if token.ent_type_ and token.ent_type_ not in BODY_PARTS:
#             token._.data = {**token._.data, **part._.data}
#     return
