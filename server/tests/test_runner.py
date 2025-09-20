#!/usr/bin/env python3
"""
Test runner script for AgroTech AI project.
Provides convenient commands to run different test suites.
"""

import subprocess
import sys
from pathlib import Path


def run_command(command, description):
    """Run a command and return the result."""
    print(f"\n{'='*50}")
    print(f"Running: {description}")
    print(f"Command: {command}")
    print(f"{'='*50}")

    result = subprocess.run(command, shell=True, capture_output=False)
    return result.returncode == 0


def main():
    """Main test runner function."""
    if len(sys.argv) < 2:
        print("Usage: python test_runner.py [unit|integration|all|coverage|lint]")
        sys.exit(1)

    test_type = sys.argv[1]
    server_root = Path(__file__).parent.parent

    # Change to server root
    import os

    os.chdir(server_root)

    success = True

    if test_type == "unit":
        success = run_command("pytest tests/unit/ -v --tb=short", "Unit Tests")

    elif test_type == "integration":
        success = run_command(
            "pytest tests/integration/ -v --tb=short -m 'not ollama'",
            "Integration Tests (without Ollama)",
        )

    elif test_type == "ollama":
        success = run_command(
            "pytest tests/integration/ -v --tb=short -m 'ollama'",
            "Integration Tests (with Ollama)",
        )

    elif test_type == "all":
        commands = [
            ("pytest tests/unit/ -v", "Unit Tests"),
            ("pytest tests/integration/ -v -m 'not ollama'", "Integration Tests"),
        ]

        for cmd, desc in commands:
            if not run_command(cmd, desc):
                success = False

    elif test_type == "coverage":
        success = run_command(
            "pytest tests/ --cov=.",
            "Test Coverage Report",
        )
        if success:
            print("\nCoverage report generated:")

    elif test_type == "lint":
        commands = [
            ("black --check agrotech_ai/ tests/", "Code Formatting Check"),
            ("isort --check-only agrotech_ai/ tests/", "Import Sorting Check"),
            ("flake8 agrotech_ai/ --output-file 'flake8-report.txt'", "Code Linting"),
        ]

        for cmd, desc in commands:
            if not run_command(cmd, desc):
                print(f'Fail run linter "{desc}"\n')
                success = False

    elif test_type == "format":
        commands = [
            ("black agrotech_ai/ tests/", "Format Code"),
            ("isort agrotech_ai/ tests/", "Sort Imports"),
        ]

        for cmd, desc in commands:
            run_command(cmd, desc)

        print("\nCode formatting completed!")

    else:
        print(f"Unknown test type: {test_type}")
        print(
            "Available options: unit, integration, ollama, all, coverage, lint, format"
        )
        sys.exit(1)

    if success:
        print(f"\n✅ {test_type.title()} completed successfully!")
        sys.exit(0)
    else:
        print(f"\n❌ {test_type.title()} failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
