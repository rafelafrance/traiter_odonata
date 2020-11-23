"""Get scientific names."""

from ..pylib.util import REPLACE, SLASH, TRAIT_STEP


def sci_name(span):
    """Enrich the match."""
    return {
        'sci_name': REPLACE.get(span.lower_, span.lower_.capitalize()),
        'group': span[0].ent_type_,
    }


def double_sci_name(span):
    """Handle a double scientific name."""
    data = {}
    names, genus = [], ''
    for token in span:
        if token.ent_type_ == 'odonata':
            name = REPLACE.get(token.lower_, token.lower_.capitalize())
            names.append(name)
            genus = name.split()[0]
            data['group'] = token.ent_type_
        elif token.is_alpha:
            name = REPLACE.get(token.lower_, token.lower_) + ' ' + genus
            names.append(name.capitalize())
    data['sci_name'] = names
    return data


SCI_NAME = {
    TRAIT_STEP: [
        {
            'label': 'sci_name',
            'on_match': sci_name,
            'patterns': [
                [
                    {'ENT_TYPE': 'odonata'},
                ],
            ],
        },
        {
            'label': 'sci_name',
            'on_match': double_sci_name,
            'patterns': [
                [
                    {'ENT_TYPE': 'odonata'},
                    {'TEXT': {'IN': SLASH}},
                    {'IS_ALPHA': True},
                ],
            ],
        },
    ],
}
