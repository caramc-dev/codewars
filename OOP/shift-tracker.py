class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self._shifts = {}

    def add_shift(self, date, hours):
        if not isinstance(hours, int) or hours < 0:            # checks if is an int and is less than 0
            raise ValueError("Hours must be a positive integer")   # if it's not, raise a value error
        self._shifts[date] = hours          # otherwise, add date and hours to a dict

    def get_average_hours(self):
        if not self._shifts:    # if shifts is empty, return 0
            return 0
        return sum(self._shifts.values()) / len(self._shifts) # sum the values in shifts and / by the len.

    def get_shifts(self):
        return self._shifts.copy()  # copy returned to protect private _shifts dictionary being mutated


def analyse_team(employees_list):   # takes a list of instantiated employee objects
    result = {}  # Create an empty dict
    for employee in employees_list: # loop through employees list
        result[employee.employee_id] = employee.get_average_hours()  # calling the method on each employee object in the loop
    return result


employee1 = Employee(1, "Alice")
employee2 = Employee(2, "Bob")
employee3 = Employee(3, "Charlie")
employee4 = Employee(4, "David")  # no shifts

employee1.add_shift("2024-01-01", 8)
employee1.add_shift("2024-01-02", 6)
employee1.add_shift("2024-01-03", 9)

employee2.add_shift("2024-01-01", 7)
employee2.add_shift("2024-01-02", 8)

employee3.add_shift("2024-01-01", 5)

employees = [employee1, employee2, employee3]

print(analyse_team(employees))
# Expected: {1: 7.666..., 2: 7.5, 3: 5.0} - I added rounding to 2 decimal places

print(analyse_team(employees + [employee4]))
# Expected: {1: 7.666..., 2: 7.5, 3: 5.0, 4: 0}

# Edge case: get_shifts returns a copy, not the internal dict
shifts = employee1.get_shifts()
shifts["2099-01-01"] = 999
print(employee1.get_shifts())
# Expected: still only 3 entries — external change didn't affect internal state

# Edge case: invalid hours raises ValueError
try:
    employee1.add_shift("2024-01-04", -5)
except ValueError as e:
    print(f"Caught error: {e}")
# Expected: Caught error: Hours must be a non-negative integer.
