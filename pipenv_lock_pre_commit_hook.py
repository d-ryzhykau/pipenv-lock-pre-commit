#!/usr/bin/env python3
import subprocess


def main():
    with open("requirements.txt", "w") as requirements_file:
        subprocess.run(["pipenv", "requirements"], stdout=requirements_file)
    with open("requirements-dev.txt", "w") as requirements_dev_file:
        subprocess.run(
            ["pipenv", "requirements", "--dev-only"], stdout=requirements_dev_file
        )


if __name__ == "__main__":
    main()
