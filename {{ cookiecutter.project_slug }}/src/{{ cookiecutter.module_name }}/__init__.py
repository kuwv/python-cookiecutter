# SPDX-FileCopyrightText: © {% now 'utc', '%Y' %} {{ cookiecutter.author }} <{{ cookiecutter.email }}>
# SPDX-License-Identifier: {{ cookiecutter.license }}
"""Template '__init__' file."""

import logging
from typing import List

__author__ = '{{ cookiecutter.author }}'
__title__ = '{{ cookiecutter.module_name }}'
__version__ = '0.1.0a0'
{%- if cookiecutter.license != 'Unlicensed' %}
__license__ = '{{ cookiecutter.license }}'
{%- endif %}
__all__: List[str] = []

logging.getLogger(__name__).addHandler(logging.NullHandler())
