# SPDX-FileCopyrightText: © 2020-2022 Jesse Johnson <jpj6652@gmail.com>
# SPDX-License-Identifier: Apache-2.0
"""Run cookiecutter post script."""

import os
import shutil


def remove(filepath: str) -> None:
    """Remove selected directory / files."""
    if os.path.isdir(filepath):
        shutil.rmtree(filepath)
    if os.path.isfile(filepath):
        os.remove(filepath)


if '{{ cookiecutter.package_manager }}' != 'poetry':
    remove('MANIFEST.in')
    if '{{ cookiecutter.package_manager }}' == 'pep621':
        remove('setup.cfg')
        remove('Pipfile')

if '{{ cookiecutter.ci }}' != 'travis':
    remove('.travis.yml')

licenses = ['Apache-2.0', 'MIT', 'MPL-2.0', 'AGPL-3.0', 'GPL-3.0', 'LGPL-3.0']
for lic in licenses:
    if lic != '{{ cookiecutter.license }}':
        remove(lic)
    elif os.path.isfile(lic):
        os.rename(lic, 'LICENSE.md')
