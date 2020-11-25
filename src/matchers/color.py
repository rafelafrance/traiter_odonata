"""Common color snippets."""

from ..pylib.util import DASH, MISSING, REPLACE, TRAIT_STEP


def color(span):
    """Enrich a color match."""
    colors = {r: 1 for t in span if (r := REPLACE.get(t.lower_, t.lower_))}
    value = '-'.join(colors)
    value = REPLACE.get(value, value)
    return dict(color=value)


def color_phrase(span):
    """Enrich a phrase match."""
    data = {}
    colors, parts, reverse = [], [], False

    for token in span:
        label = token.ent_type_
        if label in ('color', 'color_modifier'):
            colors.append(REPLACE.get(token.lower_, token.lower_))
        elif label in ['part', 'part_location']:
            parts.append(REPLACE.get(token.lower_, token.lower_))
        elif token.lower_ in MISSING:
            data['missing'] = True
        elif token.pos_ in ('ADP',):
            reverse = True

    colors = reversed(colors) if reverse else colors
    data['color'] = '-'.join(colors)

    if parts:
        data['part'] = ' '.join(parts)

    return data


COLOR = {
    TRAIT_STEP: [
        {
            'label': 'color',
            'on_match': color,
            'patterns': [
                [
                    {'ENT_TYPE': {'IN': ['color', 'color_modifier']}, 'OP': '*'},
                    {'TEXT': {'IN': DASH}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': ['color', 'color_modifier']}, 'OP': '+'},
                    {'TEXT': {'IN': DASH}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': ['color', 'color_modifier']}, 'OP': '*'},
                ],
            ],
        },
        {
            'label': 'color',
            'on_match': color_phrase,
            'patterns': [
                [
                    {'ENT_TYPE': {'IN': ['color', 'color_modifier']}, 'OP': '+'},
                    {'POS': {'IN': ['ADP']}, 'OP': '?'},
                    {'ENT_TYPE': 'color', 'OP': '+'},
                ],
                [
                    {'LOWER': {'IN': MISSING}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': ['part', 'part_location']}, 'OP': '+'},
                    {'ENT_TYPE': {'IN': ['color', 'color_modifier']}, 'OP': '+'},
                ],
                [
                    {'LOWER': {'IN': MISSING}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': ['color', 'color_modifier']}, 'OP': '+'},
                    {'ENT_TYPE': {'IN': ['part', 'part_location']}, 'OP': '+'},
                ],
            ],
        },
    ],
}
