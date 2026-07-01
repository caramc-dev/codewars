"""

==============================================================================
PRACTICE QUESTION: Employee Payroll System
==============================================================================

Build an employee payroll system using OOP.
This question focuses on class attributes vs instance attributes,
class methods vs static methods, encapsulation, and polymorphism
(via method overriding).

------------------------------------------------------------------------------
CLASS: Employee
------------------------------------------------------------------------------

CLASS ATTRIBUTES (shared across all instances):
    - company_name = "TechCorp"
    - _employee_count = 0   (private — tracks how many Employees exist in total)

__init__(self, name, base_salary)
    - Stores name as a private attribute (_name).
    - Validates base_salary using the static method is_valid_salary (below)
      BEFORE storing it. Raises a ValueError if invalid.
    - Stores base_salary as a private attribute (_base_salary).
    - Increments the CLASS attribute _employee_count by 1 every time a new
      Employee (or subclass) is created.

name (property — read only)

base_salary (property — read only)

@staticmethod
is_valid_salary(salary)
    - Returns True if salary is a number (int or float) and > 0.
    - Returns False otherwise.
    - This is static because it doesn't need access to any instance or
      class data — it's just a standalone validation rule.

@classmethod
get_employee_count(cls)
    - Returns the total number of employees created so far (across the
      WHOLE company, not just one instance).

calculate_annual_salary(self)
    - Returns base_salary * 12.

__str__(self)
    - Returns a string like: "Jamie Smith — TechCorp — £480.00/mo"

------------------------------------------------------------------------------
CLASS: Manager (inherits from Employee)
------------------------------------------------------------------------------

__init__(self, name, base_salary, bonus_percentage)
    - Calls the parent constructor using super() (so validation and the
      employee count still happen correctly).
    - Stores bonus_percentage as a private attribute (_bonus_percentage).

calculate_annual_salary(self)
    - OVERRIDES the parent method.
    - Formula: (base_salary * 12) * (1 + bonus_percentage / 100)
    - Return the result rounded to 2 decimal places.

------------------------------------------------------------------------------
CLASS: Department
------------------------------------------------------------------------------

__init__(self, name)
    - Stores the department name.
    - Initialises an empty private list _employees.

add_employee(self, employee)
    - Adds an Employee (or subclass) instance to the department.
    - Raises a TypeError if the argument is not an Employee instance.

total_payroll(self)
    - Returns the sum of calculate_annual_salary() for every employee
      in the department.
    - IMPORTANT: this must work correctly whether the employee is a plain
      Employee or a Manager, WITHOUT checking the type — this is the
      polymorphism part (think about *why* this works).

highest_paid(self)
    - Returns the Employee (or Manager) with the highest annual salary.
    - Returns None if the department is empty.

__str__(self)
    - Returns a string like: "Engineering — 4 employees"

==============================================================================
EXAMPLE USAGE
==============================================================================

emp1 = Employee("Jamie Smith", 4000)
mgr1 = Manager("Alex Chen", 6000, bonus_percentage=15)

print(emp1)
# Expected: Jamie Smith — TechCorp — £4000.00/mo

print(Employee.get_employee_count())
# Expected: 2   (emp1 and mgr1 both count — Manager IS an Employee)

dept = Department("Engineering")
dept.add_employee(emp1)
dept.add_employee(mgr1)

print(dept.total_payroll())
# Expected: 130800.0
# emp1: 4000*12 = 48000
# mgr1: (6000*12) * 1.15 = 82800
# total = 130800.0

print(str(dept.highest_paid()))
# Expected: Alex Chen — TechCorp — £6000.00/mo

print(Employee.is_valid_salary(5000))
# Expected: True
print(Employee.is_valid_salary(-100))
# Expected: False

"""
from string.templatelib import Template


class Employee:
    company_name = "TechCorp"
    _employee_count = 0

    def __init__(self, name, base_salary):
        self._name = name
        self.is_valid_salary(base_salary)  # uses the static method to check if the salary is valid
        self._base_salary = base_salary    # only assigns if is passes
        Employee._employee_count += 1      # increment the employees by 1 for each instantiation

    @property
    def name(self):
        return self._name

    @property
    def base_salary(self):
        return self._base_salary

    @staticmethod
    def is_valid_salary(salary):
        if not isinstance(salary, (int, float)) or salary <= 0:
            return False
        return True

    @classmethod
    def get_employee_count(cls):
        return cls._employee_count

    def calculate_annual_salary(self):
        return round(self._base_salary * 12, 2)

    def __str__(self):
        return f"{self.name.title()} - {self.company_name} - £{self.calculate_annual_salary() / 12:.2f}/mo"


class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percentage):
        super().__init__(name, base_salary)
        self._bonus_percentage = bonus_percentage

    def calculate_annual_salary(self):
        salary = (self._base_salary * 12) * (1 + self._bonus_percentage / 100)
        return round(salary, 2)


class Department:
    def __init__(self, name):
        self.name = name
        self._employees = []

    def add_employee(self, employee):
        if not isinstance(employee, Employee):
            raise TypeError("Invalid input - not an Employee object")
        self._employees.append(employee)

    def total_payroll(self):
        total = 0
        for employee in self._employees:
            total += employee.calculate_annual_salary()
        return total

    def highest_paid(self):
        if not self._employees:
            return None
        return max(self._employees, key=lambda v: v.calculate_annual_salary())

    def __str__(self):
        return f"{self.name} - {len(self._employees)} employees"


# ==============================================================================
# TEST CASES — run this file to check your solution
# ==============================================================================

emp1 = Employee("Jamie Smith", 4000)
emp2 = Employee("Priya Patel", 3500)
mgr1 = Manager("Alex Chen", 6000, bonus_percentage=15)

print(emp1)
# Expected: Jamie Smith — TechCorp — £4000.00/mo

print(Employee.get_employee_count())
# Expected: 3

print(emp1.get_employee_count())
# Expected: 3   (classmethods can be called via an instance too)

dept = Department("Engineering")
dept.add_employee(emp1)
dept.add_employee(emp2)
dept.add_employee(mgr1)

print(dept)
# Expected: Engineering — 3 employees

print(dept.total_payroll())
# Expected: 172800.0
# emp1: 48000, emp2: 42000, mgr1: 82800 -> total 172800.0

print(str(dept.highest_paid()))
# Expected: Alex Chen — TechCorp — £6000.00/mo

print(Employee.is_valid_salary(5000))
# Expected: True
print(Employee.is_valid_salary(-100))
# Expected: False
print(Manager.is_valid_salary(5000))
# Expected: True   (static methods are inherited too — accessible via subclass)

# Invalid salary raises ValueError
try:
    bad_emp = Employee("Bad Employee", -500)
except ValueError as e:
    print(f"Caught: {e}")
# Expected: Caught: <your validation message>

# Adding a non-Employee raises TypeError
try:
    dept.add_employee("not an employee")
except TypeError as e:
    print(f"Caught: {e}")
# Expected: Caught: <your validation message>

# Empty department
empty_dept = Department("Empty Dept")
print(empty_dept.highest_paid())
# Expected: None