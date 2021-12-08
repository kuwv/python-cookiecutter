# -*- coding: utf-8 -*-
# copyright: Copyright (C) [2021] [{{ cookiecutter.author }}]
# license: {{ cookiecutter.license }}, see LICENSE for more details.

import logging
from typing import Tuple

__author__ = '{{ cookiecutter.author }}'
__title__ = '{{ cookiecutter.module_name }}'
__version__ = '0.1.0'
__license__ = '{{ cookiecutter.license }}'
__all__: Tuple[str, ...] = ()

logging.getLogger(__name__).addHandler(logging.NullHandler())
