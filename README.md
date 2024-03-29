# Python Cookiecutter

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Build Status](https://travis-ci.org/kuwv/poetry-cookiecutter.svg?branch=master)](https://travis-ci.org/kuwv/poetry-cookiecutter)
[![codecov](https://codecov.io/gh/kuwv/poetry-cookiecutter/branch/master/graph/badge.svg)](https://codecov.io/gh/kuwv/poetry-cookiecutter)

## Overview

Python project template for instantiating a Poetry with various QA tools.

## Provision

`cookiecutter http://github.com/kuwv/poetry-cookiecutter.git`

## Package Managers

### Pep621

Use `pep621` when developing libraries and require more hands on control.

### Poetry

Use `poetry` when developing libraries that require flexible dependency management.

### Pipenv

Use `pipenv` when developing deployments that require deterministic builds.
