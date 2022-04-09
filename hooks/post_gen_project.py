"""Run cookiecutter post script."""
import os
import shutil

def remove(filepath: str) -> None:
    """Remove selected directory / files."""
    if os.path.isdir(filepath):
        shutil.rmtree(filepath)
    if os.path.isfile(filepath):
        os.remove(filepath)

if '{{ cookiecutter.package_manager }}' != 'pipenv':
    remove('Pipfile')
    remove('setup.cfg')

if '{{ cookiecutter.ci }}' != 'travis':
    remove('.travis.yml')

licenses = ['Apache-2.0', 'MIT', 'MPL-2.0', 'AGPL-3.0', 'GPL-3.0', 'LGPL-3.0']
for lic in licenses:
    if lic != '{{ cookiecutter.license }}':
        remove(lic)
    elif os.path.isfile(lic):
        os.rename(lic, 'LICENSE.md')
