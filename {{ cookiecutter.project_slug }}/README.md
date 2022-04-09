# {{ cookiecutter.project_name }}

{%- if cookiecutter.license != 'unlicensed' %}
[![License](https://img.shields.io/badge/License-{{ cookiecutter.license | replace('-', '%20') }}-blue.svg)](https://spdx.org/licenses/{{ cookiecutter.license }})
{%- endif %}
{%- if cookiecutter.ci == 'travis' %}
[![Build Status](https://travis-ci.org/{{ cookiecutter.account }}/{{ cookiecutter.project_slug }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.account }}/{{ cookiecutter.project_slug }})
[![codecov](https://codecov.io/gh/{{ cookiecutter.account }}/{{ cookiecutter.project_slug }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.account }}/{{ cookiecutter.project_slug }})
{%- endif %}

## Overview

{{ cookiecutter.project_description }}

## Install

`pip install {{ cookiecutter.module_name }}`
