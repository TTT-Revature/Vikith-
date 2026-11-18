

# Python Packages and Package Structure

## 1. What is a Package?

A package is a way of organizing related Python modules into directories.

- **Module:** A single Python `.py` file.
- **Package:** A directory that organizes related modules and subpackages.
- **Subpackage:** A package inside another package.

## 2. Module vs Package

| Module | Package |
|---|---|
| A single `.py` file | A directory containing modules or subpackages |
| Contains functions, classes and variables | Organizes related modules |
| Example: `student.py` | Example: `school/` |

## 3. Basic Package Structure

```text
my_project/
│
├── school/
│   ├── __init__.py
│   ├── student.py
│   └── teacher.py
│
└── main.py
```

Here:
- `school` is the package.
- `student.py` and `teacher.py` are modules.
- `__init__.py` is the package initialization file.
- `main.py` is the application entry point.

## 4. Creating Modules Inside a Package

**File: `school/student.py`**

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
```

**File: `school/teacher.py`**

```python
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def display(self):
        print(f"Teacher: {self.name}")
        print(f"Subject: {self.subject}")
```

**File: `school/__init__.py`**

```python
print("School package initialized")
```

## 5. Importing Modules from a Package

### Method 1: Import the complete module

```python
import school.student

s1 = school.student.Student("Vikith", 24)

s1.display()
```

### Method 2: Using `from ... import`

```python
from school.student import Student

s1 = Student("Vikith", 24)

s1.display()
```

### Method 3: Import multiple modules

```python
from school import student, teacher

s1 = student.Student("Vikith", 24)
t1 = teacher.Teacher("Rahul", "Python")

s1.display()
t1.display()
```

## 6. What is `__init__.py`?

`__init__.py` is a special file associated with regular Python packages.

It executes when the package is first imported.

```python
# school/__init__.py

print("Initializing school package")

school_name = "ABC School"
```

Now:

```python
import school

print(school.school_name)
```

**Output:**

```text
Initializing school package
ABC School
```

Important points:

- It can initialize package-level variables.
- It can import selected classes or functions.
- It can define `__all__`.
- It runs when the package is first imported, not every time the same package is imported.
- Modern Python also supports namespace packages without `__init__.py`.

## 7. Importing Directly from a Package

You can expose selected classes from the package using `__init__.py`.

**File: `school/__init__.py`**

```python
from .student import Student
from .teacher import Teacher
```

Now you can import directly:

```python
from school import Student, Teacher

s1 = Student("Vikith", 24)
t1 = Teacher("Rahul", "Python")

s1.display()
t1.display()
```

The dot (`.`) means a relative import from the current package.

## 8. What Are Subpackages?

A subpackage is a package inside another package.

```text
company/
│
├── __init__.py
│
├── employees/
│   ├── __init__.py
│   ├── manager.py
│   └── developer.py
│
├── accounts/
│   ├── __init__.py
│   ├── salary.py
│   └── payments.py
│
└── main.py
```

Here:
- `company` is the main package.
- `employees` is a subpackage.
- `accounts` is another subpackage.
- `manager.py`, `developer.py`, `salary.py` and `payments.py` are modules.

### Importing from a subpackage

```python
from company.employees.manager import Manager
from company.accounts.salary import calculate_salary
```

## 9. Absolute Imports vs Relative Imports

### Absolute Import

Uses the complete package path.

```python
from school.student import Student
```

### Relative Import

Uses dots to refer to the current package or its parent packages.

```python
from .student import Student
```

For a sibling module:

```python
from .teacher import Teacher
```

For a module in the parent package:

```python
from ..common import helper
```

| Import | Meaning |
|---|---|
| `from school.student import Student` | Absolute import |
| `from .student import Student` | Current package |
| `from ..common import helper` | Parent package's module |

Relative imports are normally used inside packages and generally require the module to be executed as part of a package.

## 10. Understanding `__all__`

`__all__` defines which names are imported when someone uses `from package import *`.

**File: `school/__init__.py`**

```python
from .student import Student
from .teacher import Teacher

__all__ = ["Student"]
```

Now:

```python
from school import *

s1 = Student("Vikith", 24)
s1.display()
```

The wildcard import imports `Student` because it is listed in `__all__`.

`Teacher` is not imported through that wildcard import.

**Note:** `__all__` does not restrict normal explicit imports.

## 11. Important Package Commands

| Syntax | Purpose |
|---|---|
| `import package` | Import a package |
| `import package.module` | Import a module inside a package |
| `from package import module` | Import a module from a package |
| `from package.module import Class` | Import a specific class |
| `from . import module` | Relative import |
| `from .. import module` | Import from parent package |

## 12. Real-World Use Cases

- **E-commerce applications:** Separate products, customers, orders and payments.
- **Employee management:** Separate employee records, salaries and attendance.
- **Web development:** Organize routes, models, controllers and services.
- **Machine learning:** Separate preprocessing, training, evaluation and prediction modules.
- **Large projects:** Make code reusable, maintainable and easier to understand.

## 13. Final Revision

| Concept | Meaning |
|---|---|
| Module | One Python file |
| Package | Organizes related modules |
| Subpackage | Package inside another package |
| `__init__.py` | Package initialization file for regular packages |
| `__all__` | Controls wildcard imports |

### Package Hierarchy

```text
Project
  └── Package
        ├── __init__.py
        ├── Module 1.py
        ├── Module 2.py
        └── Subpackage
              ├── __init__.py
              └── Module 3.py
```

