# Machine Learning School

This package is contains a version of [svpino/ml.school](https://github.com/svpino/ml.school) notebooks translated to standard Python files.

## Installation

To work with the package on your own, you'll need:

- Python ^3.9
- Poetry (^1.6 recommended)
- Git (^2.34 recommended)

In order to install this repository, first clone it (or manually download it):

```bash
git clone https://github.com/elcapo/mlschool.git
```

then install dependencies with **Poetry**:

```bash
cd mlschool
poetry install
```

and finally open a **Poetry** shell:

```bash
poetry shell

# now you can open a Python interpreter as usual
# and import stuff from mlschool
python
```

## Tests

A suite of tests lives with the code in order to facilitate refactors and also to provide some traceability of cases that have been found problematic during the development.

The test suite can be easily executed:

```bash
poetry run pytest -v
```
