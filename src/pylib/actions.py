"""Common actions for enriching matches."""

from ..pylib.util import TERMS


def text_action(span):
    """Enrich term matches."""
    label = span.label_.split('.')[0]
    return {label: TERMS.replace.get(span.lower_, span.lower_)}


def hoist_action(span, keys=None):
    """Move data from tokens in span up to the current span."""
    data = {}

    for token in span:
        if not keys:
            data = {**data, **token._.data}
        else:
            update = {k: v for k, v in token._.data.items() if k in keys}
            data = {**data, **update}

    return data


def flag_action(span, flag='flag', value=True):
    """Flag each token in the span and don't group them."""
    for token in span:
        token._.data[flag] = value
    return {'_forget': True}
