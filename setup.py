from setuptools import setup

setup(
    name="pipenv-lock-pre-commit-hook",
    license="MIT",
    version="0.4.0",
    python_requires=">=3.5",
    py_modules=["pipenv_lock_pre_commit"],
    entry_points={
        "console_scripts": [
            (
                "pipenv-lock-pre-commit-requirements = "
                "pipenv_lock_pre_commit:requirements"
            ),
            "pipenv-lock-pre-commit-verify = pipenv_lock_pre_commit:verify",
        ]
    },
)
