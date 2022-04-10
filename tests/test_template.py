"""Test template deployment."""
import pytest


@pytest.fixture
def custom_template(tmpdir):
    """Configure template fixture."""
    template = tmpdir.ensure('cookiecutter-template', dir=True)
    template.join('cookiecutter.json').write("""\
        {
            'author': 'test',
            'email': 'test@localhost',
            'account': 'test',
            'project_name': 'example-project'
        }
    """)

    repo_dir = template.ensure('{{ cookiecutter.project_name }}', dir=True)
    repo_dir.join('README.md').write('{{ cookiecutter.project_name }}')

    return template


def test_bake_custom_project(cookies, custom_template):
    """Test for cookiecutter-template."""
    result = cookies.bake(template=str(custom_template))

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'example-project'
    assert result.project.isdir()
