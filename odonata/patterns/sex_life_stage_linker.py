from spacy.language import Language

from odonata.pylib.const import REPLACE

SEX_LIFE_STAGE_LINKER = 'odonata.sex_life_stage_linker.v1'

SKIPS = """ vernacular sci_name heading total_length hind_wing_length """.split()


@Language.component(SEX_LIFE_STAGE_LINKER)
def sex_life_stage_linker(doc):
    """Link traits to sex and life stage."""

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
