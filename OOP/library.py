class Book:  # Encapsulation. The data (attributes) and behaviour) methods are grouped together in one parent class
    """
    Build a simple library system using OOP.
    Part 1 — Parent class: Book
    Attributes: title, author, year, available (default True)
    Method get_info() that returns a string in the format: "Title by Author (Year)"
    Method checkout() that sets available to False if the book is available, or prints "Book is not available" if it isn't
    Method return_book() that sets available back to True
    """
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def __str__(self):
        return self.get_info()

    def get_info(self):
        return f"{self.title} by {self.author} ({self.year})"

    def checkout(self):
        if self.available:
            self.available = False
            return f"{self.title} successfully checked out"
        else:
            return "Book is not available"

    def return_book(self):
        if not self.available:
            self.available = True


class EBook(Book):  # Inheritance - Ebook inherits all the attributes and methods for Books
    """
    Part 2 — Child class: EBook
    Inherits from Book
    Additional attribute: file_size_mb
    Override get_info() to return: "Title by Author (Year) - Digital (X MB)"
    Add method download() that prints "Downloading Title..." if available, or "Book is not available" if not
    """
    def __init__(self, title, author, year, file_size_mb, available=True):
        super().__init__(title, author, year, available)  # Super calls parent __init__ to initialise shared attributes
        self.file_size_mb = file_size_mb  # Child adds a new attribute

    def get_info(self):  # Polymorphism - same method but different behaviour
        return f"{self.title} by {self.author} ({self.year}) - Digital ({self.file_size_mb} MB)"

    def download(self):
        if self.available:
            return f"Downloading Title {self.title}..."

        return "Book is not available"


"""
Part 3 — Use it
Create one Book and one EBook
Call get_info() on both
Checkout the book, try to check it out again
Download the EBook
"""

the_owl_killers = Book("The Owl Killers", "Karen Maitland", 2009)
the_remains_of_the_day = EBook("The remains of the day", "Kazuo Ishiguro", 2009, 1.8)

print(the_owl_killers.get_info())
print(the_remains_of_the_day.get_info())

print(the_owl_killers.checkout())
print(the_owl_killers.checkout())

print(the_remains_of_the_day.checkout())
print(the_remains_of_the_day.checkout())
print(the_remains_of_the_day.download())
the_remains_of_the_day.return_book()
print(the_remains_of_the_day.download())



