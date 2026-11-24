# Lab 5 – Software Engineering Lab

**Project:** Car Rental Management System  
**Course:** Software Engineering Laboratory  
**Repository:** SE_Lab1_PES1UG24AM907

## Lab 5: Static Code Analysis

### Objective

To analyze and improve the quality, security, readability, and maintainability of a Python-based Car Rental Management System using three static analysis tools: Pylint, Bandit, and Flake8.

### Project Description

The Car Rental Management System is a Python application that supports:

- Adding and managing rental cars
- Customer registration and searching
- Car rental booking and return processing
- Rental cost and additional kilometre charge calculations
- Promotional discounts
- Booking reference generation
- Driving licence hashing
- Administrator authentication
- Receipt generation

The application uses Python and SQLite for customer data management.

### Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Application development |
| SQLite | Customer information storage |
| Pylint | Code quality analysis |
| Bandit | Security vulnerability analysis |
| Flake8 | Python style and formatting analysis |
| Git and GitHub | Version control |
| VS Code | Development environment |

### Issues Identified and Resolved

**Pylint – Code Quality**

- Renamed functions to follow snake_case naming conventions.
- Added module and function docstrings.
- Removed unused imports.
- Replaced mutable default arguments.
- Improved file handling using context managers.
- Improved string formatting using f-strings.

**Bandit – Security**

- Replaced weak SHA-1 hashing with SHA-256.
- Replaced insecure random number generation with the `secrets` module.
- Removed hardcoded administrator passwords.
- Used environment variables for administrator authentication.
- Replaced unsafe assertions with explicit validation.
- Removed unsafe dynamic execution using `exec()`.

**Flake8 – Formatting**

- Corrected indentation errors.
- Removed trailing whitespace.
- Fixed excessive line lengths.
- Added appropriate blank lines between functions.
- Corrected spacing and PEP 8 style violations.

### Static Analysis Results

| Tool | Initial Result | Final Result |
|---|---|---|
| Pylint | 5.65/10 | 10.00/10 |
| Bandit | Security vulnerabilities detected | 0 findings |
| Flake8 | Multiple formatting violations | 0 violations |

All three tools passed their final static analysis checks.

### How to Run

**1. Open the project folder**

```powershell
cd "Lab 5 and 6"
```

**2. Create a virtual environment**

```powershell
python -m venv venv
```

**3. Activate the environment (Windows)**

```powershell
.\venv\Scripts\Activate.ps1
```

**4. Install required analysis tools**

```powershell
python -m pip install pylint bandit flake8
```

**5. Run the application**

```powershell
python car_rental.py
```

**6. Run static analysis**

```powershell
python -m pylint car_rental.py
python -m bandit -r car_rental.py
python -m flake8 car_rental.py
```

For the administrator demonstration, set the `CAR_RENTAL_ADMIN_PASSWORD` environment variable before running the program.

### Project Files

```text
Lab 5 and 6/
├── car_rental.py
├── README.md
├── report.md
├── pylint_report_after.txt
├── bandit_report_after.txt
├── flake8_report_after.txt
└── reports_before/
    ├── pylint_report.txt
    ├── bandit_report.txt
    └── flake8_report.txt
```

### Git Commit History

The original Car Rental repository contains three tool-specific code-fixing commits:

| Commit | Description |
|---|---|
| `007363e` | Fix Pylint code quality issues |
| `ee3f8ab` | Fix Bandit security vulnerabilities |
| `f80546e` | Fix Flake8 formatting issues |

Original project repository:  
https://github.com/preksha-26/L5_56_car-rental

### Known Limitations

The current demonstration allows invalid rental dates and negative daily rates, which can produce negative rental costs. Additional business-rule validation and functional tests are needed before production use.

The system uses an in-memory SQLite database, so customer data is not persisted between program runs.

### Conclusion

The static code analysis process successfully improved the maintainability, readability, security practices, and formatting of the Car Rental Management System.

Pylint achieved a score of 10/10, Bandit reported no remaining findings, and Flake8 completed without formatting errors.

The exercise demonstrates the importance of automated static analysis, secure programming practices, and version control in software development.

---

**Lab 6:** Documentation can be added to this folder when the Lab 6 deliverables are available.file. A perfect 10.00/10 is very good.

Be ready to explain the bugs you found and how you fixed them. You may be called on to present.
