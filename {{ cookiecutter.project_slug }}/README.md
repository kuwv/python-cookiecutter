{% set section_separator = "=" * cookiecutter.project_slug | length -%}
{{ section_separator }}
{{ cookiecutter.project_slug }}
{{ section_separator }}

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Build Status](https://travis-ci.org/kuwv/python-compendium.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.author}}/{{ cookiecutter.project_slug }})
[![codecov](https://codecov.io/gh/kuwv/python-compendium/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.author}}/{{ cookiecutter.project_slug }})

* Overview

{{ cookiecutter.project_short_description}}
