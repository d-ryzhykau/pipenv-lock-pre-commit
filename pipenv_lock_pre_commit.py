#!/usr/bin/env python3
import subprocess
from argparse import ArgumentParser, FileType


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
    subprocess.run(["pipenv", "requirements", *extra_args], stdout=args.requirements_file)


def verify():
    subprocess.run(["pipenv", "verify"])
