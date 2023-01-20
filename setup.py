from setuptools import find_packages, setup

setup(
    name="pipenv-lock-pre-commit-hook",
    license="MIT",
    version="0.2.0",
    python_requires=">=3.5",
    py_modules=["pipenv_lock_pre_commit_hook"],
    entry_points={
        "console_scripts": [
            "pipenv-lock-pre-commit-hook = pipenv_lock_pre_commit_hook:main",
        ]
    },
)
