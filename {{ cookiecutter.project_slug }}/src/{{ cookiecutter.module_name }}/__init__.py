# -*- coding: utf-8 -*-
# copyright: Copyright (C) [{% now 'utc', '%Y' %}] [{{ cookiecutter.author }}]
# license: {{ cookiecutter.license }}, see LICENSE.md for more details.

import logging
from typing import List

__author__ = '{{ cookiecutter.author }}'
__title__ = '{{ cookiecutter.module_name }}'
__version__ = '0.1.0'
{%- if cookiecutter.license == 'MPL-2.0' %}
__license__ = '{{ cookiecutter.license }}'
{%- endif %}
__all__: List[str] = []

logging.getLogger(__name__).addHandler(logging.NullHandler())
