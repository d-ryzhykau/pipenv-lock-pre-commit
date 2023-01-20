# Pipenv lock pre-commit hook

Freeze your dependency versions to `requirements{-dev,}.txt`
using `pipenv requirements`.

## Installation

```shell
pip install pre-commit pipenv
```

Add following to your `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/d-ryzhikov/pipenv-lock-pre-commit
    rev: 0.2.0
    hooks:
    - id: pipenv-lock
```
