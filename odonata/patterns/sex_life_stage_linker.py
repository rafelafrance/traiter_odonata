"""Link traits to the sex of the odonate."""

from odonata.pylib.const import REPLACE

SKIPS = """ vernacular sci_name heading """.split()


def sex_linker(doc):
    """Link traits to sex."""

    sex, life_stage = '', ''

    for ent in doc.ents:
        label = ent.label_

        if label in SKIPS:
            continue

        if label == 'sex':
            sex = ent._.data['sex']
            sex = REPLACE.get(sex, sex)
            life_stage = ''
        elif label == 'life_stage':
            life_stage = ent._.data['life_stage']
            life_stage = REPLACE.get(life_stage, life_stage)
            sex = ''
        elif sex:
            ent._.data['sex'] = ent._.data.get('sex', sex)
        elif life_stage:
            ent._.data['life_stage'] = ent._.data.get('life_stage', life_stage)

    return doc
