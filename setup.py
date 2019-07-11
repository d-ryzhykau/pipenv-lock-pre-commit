from setuptools import setup

setup(
    name='pipenv-lock-pre-commit',
    description='Run `pipenv lock -r` as pre-commit hook',
    url='https://github.com/d-ryzhikov/pipenv-lock-pre-commit',
    version='0.1.0',
    author='Dmitry Ryzhikov',
    author_email='d.ryzhykau@gmail.com',
    install_requires=[
        'pipenv',
    ],
)
