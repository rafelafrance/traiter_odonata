"""Utilities and constants."""

from pathlib import Path

NAME = 'odonata'

DATA_DIR = Path('.') / 'data'
DOC_DIR = DATA_DIR
PDF_DIR = DOC_DIR / 'pdf'
TXT_DIR = DOC_DIR / 'txt'
VOCAB_DIR = Path('.') / 'src' / 'vocabulary'

GROUP_STEP = 'group'
TRAIT_STEP = 'traits'
HEADER_STEP = 'header'
LINK_STEP = 'link'
