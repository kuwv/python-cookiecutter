'''Run cookiecutter post script.'''
import os
import shutil

def remove(filepath):
    '''Remove selected directory / files.'''
    if os.path.isdir(filepath):
        shutil.rmtree(filepath)
    if os.path.isfile(filepath):
        os.remove(filepath)

if "{{ cookiecutter.package_manager }}" != 'poetry':
    remove('Pipfile')

if "{{ cookiecutter.package_manager }}" != 'pipenv':
    remove('pyproject.toml')
