# SPDX-FileCopyrightText: © {% now 'utc', '%Y' %} {{ cookiecutter.author }} <{{ cookiecutter.email }}>
# SPDX-License-Identifier: {{ cookiecutter.license }}
"""Provide versioning sanity check."""

from {{ cookiecutter.module_name }} import __version__


def test_version():
    assert __version__ == '0.1.0'
