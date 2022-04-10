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

`pip install {{ cookiecutter.module_name }}`
