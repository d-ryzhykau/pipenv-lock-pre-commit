#!/usr/bin/env python3
import os
import subprocess
import sys
from argparse import ArgumentParser
from pathlib import Path


def _get_env():
    env = os.environ.copy()
    env["PIPENV_IGNORE_VIRTUALENVS"] = "1"
    return env


def _get_root_dirs(changed_pipfiles):
    return set(
        Path(path).parent.resolve()
        for path in changed_pipfiles
    )


def requirements():
    parser = ArgumentParser(prog="pipenv_lock_pre_commit:requirements")
    parser.add_argument(
        "--requirements-file",
        help="output file path relative to Pipfile",
        default="requirements.txt",
    )
    # fetch list of changed files passed by pre-commit
    parser.add_argument("changed_pipfiles", nargs="+")
    args, extra_args = parser.parse_known_args()

    env = _get_env()
    return_code = 0
    for root_dir in _get_root_dirs(args.changed_pipfiles):
        with open(root_dir / args.requirements_file, "w") as stdout:
            print(
                "{root_dir}: pipenv requirements {extra_args}".format(
                    root_dir=root_dir,
                    extra_args=" ".join(extra_args),
                )
            )
            out = subprocess.run(
                ["pipenv", "requirements", *extra_args],
                stdout=stdout,
                cwd=root_dir,
                env=env,
            )
        return_code |= out.returncode
    sys.exit(return_code)


def verify():
    parser = ArgumentParser(prog="pipenv_lock_pre_commit:verify")
    # fetch list of changed files passed by pre-commit
    parser.add_argument("changed_pipfiles", nargs="+")
    args = parser.parse_args()

    env = _get_env()
    return_code = 0
    for root_dir in _get_root_dirs(args.changed_pipfiles):
        print("{0}: pipenv verify".format(root_dir))
        out = subprocess.run(["pipenv", "verify"], cwd=root_dir, env=env)
        return_code |= out.returncode
    sys.exit(return_code)
