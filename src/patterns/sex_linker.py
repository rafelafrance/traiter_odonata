"""Link traits to the sex of the odonate."""

from ..pylib.consts import REPLACE


SKIPS = """ vernacular sci_name heading """.split()


def sex_linker(doc):
    """Link traits to sex."""

    sex = 'both sexes'
    for token in doc:
        label = token.ent_type_

        if label in SKIPS:
            continue

        if label == 'sex':
            sex = token._.data['sex']
            sex = REPLACE.get(sex, sex)
        elif label:
            token._.data['sex'] = sex

    return doc
