#!/usr/bin/env python3
import os
import subprocess
import sys
from argparse import ArgumentParser, FileType


def _get_env():
    env = os.environ.copy()
    env["PIPENV_IGNORE_VIRTUALENVS"] = "1"
    return env


def requirements():
    parser = ArgumentParser()
    parser.add_argument(
        "--requirements-file",
        type=FileType("w"),
        default="requirements.txt",
    )
    # fetch list of changed files passed by pre-commit
    parser.add_argument("changed_pipfiles", nargs="+")
    args, extra_args = parser.parse_known_args()
    out = subprocess.run(
        ["pipenv", "requirements", *extra_args],
        stdout=args.requirements_file,
        env=_get_env(),
    )
    return sys.exit(out.returncode)


def verify():
    out = subprocess.run(["pipenv", "verify"], env=_get_env())
    sys.exit(out.returncode)
