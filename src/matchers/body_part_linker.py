"""Link traits to body parts."""

from ..pylib.consts import LINK_STEP

BODY_PARTS = """ body_part body_part_loc sex_diff """.split()
COLORS = """ color color_mod """.split()
FILLER_POS = """ CCONJ VERB AUX """.split()


def linker(span):
    """Link body parts to traits."""
    part = [t for t in span if t.ent_type_ in BODY_PARTS][0]
    for token in span:
        if token.ent_type_ and token.ent_type_ not in BODY_PARTS:
            token._.data = {**token._.data, **part._.data}
    return


BODY_PART_LINKER = {
    LINK_STEP: [
        {
            'label': 'body_part_linker',
            'on_match': linker,
            'patterns': [
                [
                    {'ENT_TYPE': {'IN': COLORS}, 'OP': '+'},
                    {'POS': {'IN': FILLER_POS}, 'OP': '?'},
                    {'POS': {'IN': FILLER_POS}, 'OP': '?'},
                    {'POS': {'IN': FILLER_POS}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': BODY_PARTS}},
                ],
                [
                    {'ENT_TYPE': {'IN': BODY_PARTS}},
                    {'POS': {'IN': FILLER_POS}, 'OP': '?'},
                    {'POS': {'IN': FILLER_POS}, 'OP': '?'},
                    {'POS': {'IN': FILLER_POS}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': COLORS}, 'OP': '+'},
                ],
                [
                    {'ENT_TYPE': {'IN': BODY_PARTS}},
                    {'ENT_TYPE': {'IN': COLORS}, 'OP': '+'},
                    {'POS': {'IN': FILLER_POS}, 'OP': '?'},
                    {'POS': {'IN': FILLER_POS}, 'OP': '?'},
                    {'POS': {'IN': FILLER_POS}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': COLORS}, 'OP': '+'},
                ],
            ],
        },
    ],
}
