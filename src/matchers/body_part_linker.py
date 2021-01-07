"""Link traits to body parts."""

from ..pylib.consts import LINK_STEP

PARTS = """ """.split()


COLORS = """ color color_mod """.split()


def linker(span):
    """Link body parts to traits."""
    part = [t for t in span if t.ent_type_ == 'body_part'][0]
    for token in span:
        if token.ent_type_ and token.ent_type_ != 'body_part':
            token._.data = {**part._.data, **token._.data}

    return {'_forget': True}


BODY_PART_LINKER = {
    LINK_STEP: [
        {
            'label': 'linker',
            'on_match': linker,
            'patterns': [
                [
                    {'ENT_TYPE': {'IN': COLORS}, 'OP': '+'},
                    {'ENT_TYPE': 'body_part'},
                ],
                [
                    {'ENT_TYPE': 'body_part'},
                    {'ENT_TYPE': {'IN': COLORS}, 'OP': '+'},
                ],
            ],
        },
    ],
}
