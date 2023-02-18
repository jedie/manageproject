import subprocess
from pathlib import Path

import tomli
from bx_py_utils.path import assert_is_file

from manageprojects import __version__
from manageprojects.cli.cli_app import PACKAGE_ROOT
from manageprojects.test_utils.click_cli_utils import subprocess_cli
from manageprojects.tests.base import BaseTestCase
from manageprojects.utilities import code_style


class ProjectSetupTestCase(BaseTestCase):
    def test_version(self):
        pyproject_toml_path = Path(PACKAGE_ROOT, 'pyproject.toml')
        assert_is_file(pyproject_toml_path)

        self.assertIsNotNone(__version__)

        pyproject_toml = tomli.loads(pyproject_toml_path.read_text(encoding='UTF-8'))
        pyproject_version = pyproject_toml['project']['version']

        self.assertEqual(__version__, pyproject_version)

        cli_bin = PACKAGE_ROOT / 'cli.py'
        assert_is_file(cli_bin)

    def test_code_style(self):
        cli_bin = PACKAGE_ROOT / 'cli.py'
        assert_is_file(cli_bin)

        try:
            output = subprocess_cli(
                cli_bin=cli_bin,
                args=('check-code-style',),
                exit_on_error=False,
            )
        except subprocess.CalledProcessError as err:
            self.assert_in_content(  # darker was called?
                got=err.stdout,
                parts=('.venv/bin/darker',),
            )
        else:
            if 'Code style: OK' in output:
                self.assert_in_content(  # darker was called?
                    got=output,
                    parts=('.venv/bin/darker',),
                )
                return  # Nothing to fix -> OK

        # Try to "auto" fix code style:

        try:
            output = subprocess_cli(
                cli_bin=cli_bin,
                args=('fix-code-style',),
                exit_on_error=False,
            )
        except subprocess.CalledProcessError as err:
            output = err.stdout

        self.assert_in_content(  # darker was called?
            got=output,
            parts=('.venv/bin/darker',),
        )

        # Check again and display the output:

        try:
            code_style.check(package_root=PACKAGE_ROOT)
        except SystemExit as err:
            self.assertEqual(err.code, 0, 'Code style error, see output above!')
