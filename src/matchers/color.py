"""Common color snippets."""

from ..pylib.util import DASH, MISSING, REPLACE, TRAIT_STEP

COLORS = ['color', 'color_modifier']
PARTS = ['part', 'part_location', 'fly']


def color(span):
    """Enrich a color match."""
    colors = {r: 1 for t in span if (r := REPLACE.get(t.lower_, t.lower_))}
    value = '-'.join(colors)
    value = REPLACE.get(value, value)
    return dict(color=value)


def color_phrase(span):
    """Enrich a phrase match."""
    data = []
    color_start, color_end, colors = -1, -1, []
    part_start, part_end, parts, locations = -1, -1, [], []
    missing, reverse = False, False

    for i, token in enumerate(span):
        label = token.ent_type_
        value = REPLACE.get(token.lower_, token.lower_)

        if label in COLORS:
            color_start = i if color_start < 0 else color_start
            color_end = i + 1
            colors.append(value)
        elif label in PARTS:
            part_start = i if part_start < 0 else part_start
            part_end = i + 1
            if label == 'part_location':
                locations.append(value)
            else:
                parts.append(value)
        elif token.lower_ in MISSING:
            missing = True
        elif token.pos_ in ('ADP',):
            reverse = True

    part = ' '.join(parts)
    location = ' '.join(locations)

    colors = reversed(colors) if reverse else colors
    color_data = {
        '_span': span[color_start:color_end],
        '_label': 'color',
        'color': '-'.join(colors),
    }
    if part:
        color_data['body_part'] = part
    if location:
        color_data['location'] = location
    if missing:
        color_data['missing'] = True
    data.append(color_data)

    if part:
        part_data = {
            '_span': span[part_start:part_end],
            '_label': 'body_part',
            'body_part': part,
        }
        if location:
            part_data['location'] = location
        data.append(part_data)

    return data


COLOR = {
    TRAIT_STEP: [
        {
            'label': 'color',
            'on_match': color,
            'patterns': [
                [
                    {'ENT_TYPE': {'IN': COLORS}, 'OP': '*'},
                    {'TEXT': {'IN': DASH}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': COLORS}, 'OP': '+'},
                    {'TEXT': {'IN': DASH}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': COLORS}, 'OP': '*'},
                ],
            ],
        },
        {
            'label': 'color',
            'on_match': color_phrase,
            'patterns': [
                [
                    {'ENT_TYPE': {'IN': COLORS}, 'OP': '+'},
                    {'POS': {'IN': ['ADP']}, 'OP': '?'},
                    {'ENT_TYPE': 'color', 'OP': '+'},
                ],
                [
                    {'LOWER': {'IN': MISSING}, 'OP': '?'},
                    {'POS': {'IN': ['ADJ']}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': PARTS}, 'OP': '+'},
                    {'ENT_TYPE': {'IN': COLORS}, 'OP': '+'},
                ],
                [
                    {'LOWER': {'IN': MISSING}, 'OP': '?'},
                    {'POS': {'IN': ['ADJ']}, 'OP': '?'},
                    {'ENT_TYPE': {'IN': COLORS}, 'OP': '+'},
                    {'ENT_TYPE': {'IN': PARTS}, 'OP': '+'},
                ],
            ],
        },
    ],
}
