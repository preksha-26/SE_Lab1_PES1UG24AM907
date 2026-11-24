# Lab 5: Static Code Analysis

## 1. Objective

To improve the code quality, security, readability, and maintainability of a Python-based Car Rental Management System using Pylint, Bandit, and Flake8.

## 2. Tools Used

- **Pylint:** Identifies code-quality issues and programming errors.
- **Bandit:** Detects potential security vulnerabilities.
- **Flake8:** Checks Python coding style and formatting against PEP 8 conventions.
- **Git and GitHub:** Track and document changes through version control.
- **VS Code:** Edit, execute, and analyze the source code.

## 3. Project Description

The Car Rental Management System is a Python application supporting customer registration, car rental bookings, vehicle returns, promotional discounts, licence hashing, administrator authentication, and receipt generation.

## 4. Issues Identified and Fixes

| Issue | Tool | Description | Fix Applied |
|---|---|---|---|
| Invalid function naming | Pylint | Functions used camelCase instead of snake_case | Renamed functions following Python naming conventions |
| Missing docstrings | Pylint | Functions lacked documentation | Added descriptive docstrings |
| Mutable default argument | Pylint | A shared list was used as a default parameter | Replaced the default list with None |
| Weak SHA-1 hashing | Bandit | SHA-1 is unsuitable for security-sensitive hashing | Replaced SHA-1 with SHA-256 |
| Insecure random numbers | Bandit | Predictable booking identifiers | Replaced random with secrets |
| Hardcoded admin password | Bandit | Password stored directly in source code | Used an environment variable |
| Assert-based validation | Bandit | Assertions can be disabled in optimized Python | Replaced assert with explicit validation |
| Incorrect indentation | Flake8 | Continuation lines were misaligned | Corrected indentation |
| Missing blank lines | Flake8 | Functions were not separated according to PEP 8 | Added required blank lines |
| Trailing whitespace | Flake8 | Unnecessary spaces appeared at line endings | Removed extra spaces |

## 5. Results

| Analysis Tool | Before | After |
|---|---|---|
| Pylint | 5.65/10 | 10.00/10 initially achieved |
| Bandit | Security vulnerabilities detected | Final report generated; confirm zero findings |
| Flake8 | Multiple formatting issues | Zero violations in final check |

## 6. Reflection

**Q1. How did static analysis improve the code?**

Static analysis helped identify problems without executing the application. Pylint improved maintainability and coding practices, Bandit highlighted security vulnerabilities, and Flake8 improved consistency and readability.

**Q2. Which tool was most useful?**

Each tool served a different purpose. Bandit was particularly valuable for identifying security weaknesses that may not be obvious during normal program execution.

**Q3. What challenges were encountered?**

The main challenges were correcting indentation, updating renamed function references, removing hardcoded credentials, and ensuring the program continued to run after changes.

**Q4. Why are multiple static analysis tools useful?**

Different tools identify different categories of problems. Using them together provides broader coverage than relying on a single tool.

## 7. Conclusion

This lab demonstrated how Pylint, Bandit, and Flake8 improve Python code quality and security. The source code was refactored, security-sensitive operations were improved, and formatting violations were corrected.

Git was used to maintain separate commits for each analysis stage, providing a clear history of the changes.

Static analysis is useful but does not replace functional testing, security testing, or code review.