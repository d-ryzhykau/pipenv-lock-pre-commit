# Pipenv lock pre-commit hook

Freeze your dependency versions to `requirements{-dev,}.txt`
using `pipenv requirements`.

## Installation

Install [Pipenv](https://pipenv.pypa.io/) and [pre-commit](https://pre-commit.com):
```shell
pip install pipenv pre-commit
```

Add a pre-commit configuration:
```yaml
-   repo: https://github.com/d-ryzhykau/pipenv-lock-pre-commit
    rev: 0.4.1
    hooks:
    - id: pipenv-requirements      # generate a requirements.txt
    - id: pipenv-requirements-dev  # generate a requirements-dev.txt
    - id: pipenv-verify            # verify the hash in Pipfile.lock
```

To pass additional parameters to Pipenv commands, overwrite `args` property of the hook.
**Note**: overwriting `args` property removes default arguments passed to the hook script.
```yaml
-   repo: https://github.com/d-ryzhykau/pipenv-lock-pre-commit
    rev: 0.4.1
    hooks:
    - id: pipenv-requirements-dev
      # pass new --hash param and preserve default --requirements-file option
      args: [--hash, --requirements-file=requirements-dev.txt]
```
