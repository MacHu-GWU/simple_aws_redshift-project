# Code Structure Guide for mcp_ohmy_sql

This document provides a comprehensive guide to the codebase structure and architecture of the simple_aws_redshift project.

## Overview

## Virtual Environment Setup

We create the Python virtual environment in the `.venv` directory at the project root. Key tools include:

- `.venv/bin/python`: Virtual environment Python interpreter, used 99% of the time
- `.venv/bin/pip`: pip package manager for installing ad-hoc Python packages. For predefined packages in `pyproject.toml`, we primarily use the global `poetry` 2.x command
- `.venv/bin/pytest`: pytest test runner for executing unit tests

## Test Strategy

### Unit Test File Organization

Each Python file in `mcp_ohmy_sql/` has a corresponding unit test file in the `tests/` directory. For example, source code at `mcp_ohmy_sql/my_package/my_subpackage/my_module.py` has its test file at `tests/my_package/my_subpackage/test_my_package_my_subpackage_my_module.py`. The test file name includes the full relative path to prevent naming collisions.

### Package Test Directory Structure

Each Python package (directory containing `__init__.py`) has a corresponding test directory in `tests/`. For example, the package at `mcp_ohmy_sql/my_package/my_subpackage/` has its test directory at `tests/my_package/my_subpackage/`. Each test directory contains an `all.py` file that runs code coverage tests for all modules in that package.

### Running Code Coverage Tests for Individual Files

Each test file can be run directly to generate a coverage report:

```bash
.venv/bin/python tests/my_package/my_subpackage/test_my_package_my_subpackage_my_module.py
```

This will:

1. Run all unit tests for the specific module
2. Generate a code coverage HTML report at `htmlcov/${random_hash}_my_module_py.html`
3. Show covered and uncovered lines in the HTML report

This is the most important workflow since 90% of development involves editing a single source file and running its corresponding test to meet coverage goals.

### Running Code Coverage Tests for All Files

Each source code directory has a corresponding `all.py` test script. Running `tests/all.py` executes code coverage tests for the entire Python package:

```bash
.venv/bin/python tests/all.py
```

You can also run coverage tests for a specific package:

```bash
.venv/bin/python tests/my_package/all.py
```

### Code Coverage Configuration

The `.coveragerc` file in the root directory configures the coverage tool, specifying which files to exclude from coverage reports in the `omit` section.

### Viewing Coverage Reports

After running tests, open the generated HTML file to see:

- Green lines: Code executed during tests
- Red lines: Code not covered by tests  
- Line-by-line coverage details

### Coverage Goals

- Target 95%+ code coverage for all implementation files
- Use `# pragma: no cover` for untestable code (e.g., platform-specific code when testing on different platforms)

## Public API and Testing

The package always includes a `mcp_ohmy_sql/api.py` file that exposes all public APIs for package users. Each line in this file defines a Python class, function, or variable.

We follow this pattern:

```python
from .my_module import my_func_1
from .my_module import my_func_2
```

We avoid this pattern:

```python
from .my_module import my_func_1, my_func_2
```

The corresponding test file is located at `tests/test_api.py`. This test file imports all public API objects from `mcp_ohmy_sql/api.py` to establish a test baseline, ensuring that any changes to the public API in `api.py` are caught by unit tests.
