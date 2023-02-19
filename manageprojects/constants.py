INITIAL_REVISION = 'initial_revision'
INITIAL_DATE = 'initial_date'
APPLIED_MIGRATIONS = 'applied_migrations'
COOKIECUTTER_TEMPLATE = 'cookiecutter_template'
COOKIECUTTER_DIRECTORY = 'cookiecutter_directory'
COOKIECUTTER_CONTEXT = 'cookiecutter_context'

CLI_EPILOG = 'Project Homepage: https://github.com/jedie/manageprojects'

FORMAT_PY_FILE_DARKER_PRE_FIXES = ','.join(
    sorted(
        [
            'E302',  # expected 2 blank lines
            'E303',  # too many blank lines
            'W391',  # blank line at end of file
        ]
    )
)
FORMAT_PY_FILE_DEFAULT_MIN_PYTON_VERSION = '3.9'
FORMAT_PY_FILE_DEFAULT_MAX_LINE_LENGTH = 119
