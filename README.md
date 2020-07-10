# The Odonata Traits Database Project [![Build Status](https://travis-ci.org/rafelafrance/traiter_odonata.svg?branch=master)](https://travis-ci.org/rafelafrance/traiter_odonata)

Extract traits and locations from scientific literature about dragon and damsel flies (Odonata).


To remove spaces from file names
```shell script
for f in *\ *; do mv "$f" "${f// /_}"; done
```
