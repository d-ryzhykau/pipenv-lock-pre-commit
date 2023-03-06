# Pipenv lock pre-commit hooks

Freeze Pipenv dependency versions with pre-commit hooks.

## Installation

Install [Pipenv](https://pipenv.pypa.io/) and [pre-commit](https://pre-commit.com):
```shell
pip install pipenv pre-commit
```

Add a pre-commit configuration:
```yaml
-   repo: https://github.com/d-ryzhykau/pipenv-lock-pre-commit
    rev: 0.5.0
    hooks:
    - id: pipenv-lock              # generate a Pipfile.lock
    - id: pipenv-verify            # verify the hash in Pipfile.lock
    - id: pipenv-requirements      # generate a requirements.txt
    - id: pipenv-requirements-dev  # generate a requirements-dev.txt
```

To pass additional parameters to Pipenv commands, overwrite `args` property of the hook.
**Note**: overwriting `args` property removes default arguments passed to the hook script.
```yaml
-   repo: https://github.com/d-ryzhykau/pipenv-lock-pre-commit
    rev: 0.5.0
    hooks:
    - id: pipenv-requirements-dev
      # pass new --hash param and preserve default --requirements-file option
      args: [--hash, --requirements-file=requirements-dev.txt]
```
