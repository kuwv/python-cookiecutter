# -*- coding: utf-8 -*-
# copyright: (c) 2021 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
'''Test Task-Runner.'''

from os import PathLike
from typing import Optional

from invoke import Context, task


@task
def autoformat(ctx, check=True):  # type: (Context, bool) -> None
    '''Format project source code to PEP-8 standard.'''
    args = ['--skip-string-normalization']
    if check:
        args.append('--check')
    ctx.run('isort --atomic **/*.py')
    ctx.run("black **/*.py {}".format(' '.join(args)))


@task
def lint(ctx):  # type: (Context) -> None
    '''Check project source code for linting errors.'''
    ctx.run('flake8')


@task
def type_check(ctx, path='.'):  # type: (Context, PathLike) -> None
    '''Check project source types.'''
    ctx.run("mypy {}".format(path))


@task
def unit_test(ctx, capture=None):  # type: (Context, Optional[str]) -> None
    '''Perform unit tests.'''
    args = []
    if capture:
        args.append('--capture=' + capture)
    ctx.run("pytest {}".format(' '.join(args)))


@task
def static_analysis(ctx):  # type: (Context) -> None
    '''Perform static code analysis on imports.'''
    ctx.run('safety check')
    ctx.run('bandit -r {{ cookiecutter.module_name }}')


@task
def coverage(ctx, report=None):  # type: (Context, Optional[str]) -> None
    '''Perform coverage checks for tests.'''
    args = ['--cov={{ cookiecutter.module_name }}']
    if report:
        args.append('--cov-report={}'.format(report))
    ctx.run("pytest {} ./tests/".format(' '.join(args)))


@task(pre=[autoformat, lint, unit_test, static_analysis, coverage])
def test(ctx):  # type: (Context) -> None
    '''Run all tests.'''
    pass
