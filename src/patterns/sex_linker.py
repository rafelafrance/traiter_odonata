"""Link traits to the sex of the odonate."""

from spacy.language import Language

from ..pylib.consts import REPLACE, SEX_STEP

SKIPS = """ vernacular sci_name heading """.split()


@Language.component(SEX_STEP)
def sex_linker(doc):
    """Link traits to sex."""

    sex = 'both sexes'
    for ent in doc.ents:
        label = ent.label_

        if label in SKIPS:
            continue

        if label == 'sex':
            sex = ent._.data['sex']
            sex = REPLACE.get(sex, sex)
        else:
            ent._.data['sex'] = ent._.data.get('sex', sex)

    return doc