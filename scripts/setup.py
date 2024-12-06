#!/usr/bin/env python3
"""Setup script for development environment"""
import subprocess
import sys


def run_command(command, error_message):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {error_message}")
        print(f"Command failed with exit code {e.returncode}")
        sys.exit(1)


def main():
    # Install dependencies
    print("Installing dependencies...")
    run_command(["pipenv", "install"], "Failed to install dependencies")

    # Install pre-commit hooks
    print("Installing pre-commit hooks...")
    run_command(
        ["pipenv", "run", "pre-commit", "install"], "Failed to install pre-commit hooks"
    )

    print("\nSetup completed successfully!")
    print("\nReminder: Activate your virtual environment with 'pipenv shell'")


if __name__ == "__main__":
    main()
