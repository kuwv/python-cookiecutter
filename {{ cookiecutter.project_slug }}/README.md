# {{ cookiecutter.project_name }}

{%- if cookiecutter.license != 'unlicensed' %}
[![License](https://img.shields.io/badge/License-{{ cookiecutter.license | replace('-', '%20') }}-blue.svg)](https://spdx.org/licenses/{{ cookiecutter.license }})
{%- endif %}
{%- if cookiecutter.ci == 'travis' %}
[![Build Status](https://travis-ci.org/{{ cookiecutter.account }}/{{ cookiecutter.project_slug }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.account }}/{{ cookiecutter.project_slug }})
{%- elif cookiecutter.ci == 'github' %}
![Build Status](https://github.com/{{ cookiecutter.account }}/{{ cookiecutter.project_slug }}/actions/workflows/main.yml/badge.svg?branch=master)
{%- endif %}
[![codecov](https://codecov.io/gh/{{ cookiecutter.account }}/{{ cookiecutter.project_slug }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.account }}/{{ cookiecutter.project_slug }})

## Overview

{{ cookiecutter.project_description }}

## Install

```
pip install {{ cookiecutter.module_name }}
```

## Development
{% if cookiecutter.package_manager == 'pep621' %}
```
pip install --user virtualenv
virtualenv .env
source .env/bin/activate
pip install '.[build,test,sca,style]'
```
{% elif cookiecutter.package_manager == 'poetry' %}
```
pip install --user poetry
poetry shell
poetry install
```
{% elif cookiecutter.package_manager == 'pipenv' %}
```
pip install --user pipenv 
pipenv shell
pipenv install --dev
```
{% endif %}
