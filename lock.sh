#!/usr/bin/env sh
pipenv lock -r > requirements.txt
pipenv lock -r --dev > requirements-dev.txt
git add requirements.txt
git add requirements-dev.txt
