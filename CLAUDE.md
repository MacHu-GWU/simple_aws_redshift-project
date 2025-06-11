# Code Structure Guide for simple_aws_redshift

This document provides a comprehensive guide to the codebase structure and architecture of the simple_aws_redshift project.

## Overview

## AWS Redshift Model Architecture

The AWS Redshift models follow a sophisticated lazy-loading architecture with three key design patterns:

### 1. Raw Data Storage Pattern

All models store the original API response data in a `_data` attribute, treating the AWS API response schema as potentially unstable. This raw data serves as the single source of truth for all model properties.

```python
@dataclasses.dataclass
class RedshiftServerlessNamespace(Base):
    _data: dict[str, T.Any] = dataclasses.field(default=REQ)
```

### 2. Property-Based Access Pattern (Lazy Loading)

All attributes are exposed through properties rather than direct instance attributes. This lazy loading approach provides several benefits:

- **Data validation**: Properties can validate and transform data on access
- **Type conversion**: Raw API data can be converted to appropriate Python types
- **Resilience**: Properties provide a stable interface even if the underlying API schema changes
- **Performance**: Data is only processed when accessed

Example implementation:

```python
@property
def admin_password_secret_arn(self) -> T.Optional[str]:
    return self._data.get("adminPasswordSecretArn")

@property  
def status(self) -> "NamespaceStatusType":
    return self._data["status"]
```

### 3. Core Data Extraction Pattern

Each model implements a `core_data` property that returns a standardized, minimal representation of the object. This provides:

- **Consistency**: A uniform way to access essential information across different model types
- **Serialization**: Easy conversion to dictionaries for logging, caching, or API responses
- **Testing**: Simplified comparison and assertion in unit tests

```python
@property
def core_data(self) -> T_KWARGS:
    """
    Returns a dictionary containing the essential data of the model.
    
    This property must be implemented by all subclasses to provide
    a consistent minimal representation of the model's core data.
    """
    raise NotImplementedError
```

### Benefits of This Architecture

1. **API Resilience**: By storing raw API data and accessing it through properties, the models remain stable even when AWS changes their API response structure
2. **Memory Efficiency**: Lazy loading means expensive computations or transformations only happen when needed
3. **Type Safety**: Properties provide explicit return types while allowing flexible internal data storage
4. **Maintainability**: Clear separation between raw data storage and processed data access makes the code easier to understand and modify

This pattern should be followed when implementing new AWS Redshift model classes to maintain consistency across the codebase.


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
