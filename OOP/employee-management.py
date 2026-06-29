#    CFGDegree Student Management System challenge
import uuid
from collections import defaultdict


class CFGStudent:
    """
    Part 1 — Parent class: CFGStudent
    Attributes: name, surname, age, email, student_id (optional — if not passed, auto-generate one using uuid.uuid4())
    Class attribute: total_students that increments each time a new student is created
    Method get_full_name() that returns "Name Surname"
    Method get_student_id() that returns the student ID
    Class method get_total_students() that returns "Total students: X"
    __str__ that returns "Name Surname (ID: student_id)"
    """
    def __init__(self, name, surname, age, email, student_id=None):  # Encapsulation. The attributes and methods are grouped together in one parent class, with student_ID having a default None
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = student_id if student_id else uuid.uuid4()  # adds the student ID if provided, otherwise defaults to a UUID - part of python modules
        CFGStudent.total_students += 1  # Auto increments total_students each time a new instance is created

    total_students = 0  # class attribute to track the number of students. Initialised at 0

    def get_full_name(self):  # displays full name in a string
        return f"{self.name.title()} {self.surname.title()}"

    def get_student_id(self):
        return self.student_id  # returns the student ID

    @classmethod
    def get_total_students(cls):  # class method used - used as needs access to the whole class to get access to total_students
        return f"Total students: {cls.total_students}"

    def __str__(self):
        return f"{self.get_full_name()} (ID: {self.student_id})"


class SpecialisationStudent(CFGStudent):
    """
    Part 2 — Child class: SpecialisationStudent
    Inherits from CFGStudent
    Additional attributes: specialisation, course_grades (default empty dict)
    Override get_student_id() to return the ID with "CFG-" prefix
    Method add_grade(course, grade) that adds to course_grades
    Method get_average_grade() that returns the average of all grades, or "No grades yet" if empty
    """
    def __init__(self, name, surname, age, email, specialisation, student_id=None, course_grades=None):  # Inheritance - inherits all the attributes and methods from CFGStudents
        super().__init__(name, surname, age, email, student_id)
        self.specialisation = specialisation
        self.course_grades = course_grades if course_grades else defaultdict(list)  # sets up dict as a default dict specifying keys are lists to allow for more than 1 grade to be added

    def get_student_id(self):  # Polymorphism - takes original method and modifies it
        return f"CFG - {self.student_id}"

    def add_grade(self, course, grade):  # Method to add a grade. This will append either a new course and grade if none; nd add a grade to the list if there is already one there
        self.course_grades[course].append(int(grade))

    def get_average_grade(self, course):  # Returns average by summing the grades and / by len
        if course in self.course_grades:
            return sum(self.course_grades[course]) / float(len(self.course_grades[course]))
        else:
            return "No grades yet"


"""
Part 3 — Use it

Create two CFGStudent instances — one with a manual ID, one auto-generated
Create one SpecialisationStudent
Print full names, IDs, total students
Add some grades and print the average
"""

student_sarah = CFGStudent("sarah", "smith", 22, "sarah@email.com", 1)
student_greg = CFGStudent("greg", "hogg", 33, "greg@email.com")

print(student_sarah.get_full_name(), "ID:", student_sarah.get_student_id())
print(student_greg.get_full_name(), "ID:", student_greg.get_student_id())

specialisation_student_helen = SpecialisationStudent("helen", "rogers", 40, 'helen@email.com', "software")

print(CFGStudent.total_students)

specialisation_student_helen.add_grade("java", 100)
specialisation_student_helen.add_grade("java", 78)
specialisation_student_helen.add_grade("postgres", 88)
specialisation_student_helen.add_grade("java", 95)

print(specialisation_student_helen.get_average_grade("java"))
print(specialisation_student_helen.get_average_grade("python"))

print(student_sarah)