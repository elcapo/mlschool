# Machine Learning School

This package is contains a version of [svpino/ml.school](https://github.com/svpino/ml.school) notebooks translated to standard Python files.

> [!NOTE]  
> The package will be updated as I complete each Code Walkthrough. For the moment, it only covers the first one.

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

## Configuration

The package will need the same Amazon Web Services (AWS) variables that are used in the notebooks. Use `env.example` as a reference to create your `.env` file with the values of your AWS configuration.

Before completing this you must follow the course [Setup Instructions](https://program.ml.school/setup.html) for [Configuring AWS](https://program.ml.school/setup.html#configuring-aws).

## Usage

To run the pipeline in local mode, first open a Poetry Shell and then run:

```bash
python pipeline_runner.py
```

To run it in remote mode, add the `--remote` option:

```bash
python pipeline_runner.py --remote
```

## Tests

A suite of tests lives with the code in order to facilitate refactors and also to provide some traceability of cases that have been found problematic during the development.

The test suite can be easily executed:

```bash
poetry run pytest -v
```
