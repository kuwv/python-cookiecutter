'''{{ cookiecutter.project_short_description }}'''
# -*- coding: utf-8 -*-

__author__ = '{{ cookiecutter.author }}'
__title__ = '{{ cookiecutter.module_name }}'
__version__ = '0.1.0'
__license__ = 'Apache-2.0'

__all__ = []

import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())
