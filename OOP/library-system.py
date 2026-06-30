class Book:
    def __init__(self, title, author, pages):
        self._title = title     # this will never be changed from insertion so is indicated private by a single underscore
        self._author = author   # same as title
        self.pages = pages      # pages uses the setter so has no underscore, that happened in the setter method. The validation runs even during init diue to the setter
        self._available = True  # when a book is created, and added to the shelf it is automatically available

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Pages must be a positive integer")
        self._pages = value

    @property
    def is_available(self):
        if self._available:
            return True
        else:
            return False

    def checkout(self):
        if not self._available:
            raise ValueError("Book is not available")
        self._available = False

    def return_book(self):
        if self._available:
            raise ValueError("Book has not yet been checked out so cannot be returned")
        self._available = True

    def __str__(self):
        if self._available:
            status = "Available"
        else:
            status = "Checkout Out"

        return f"{self._title} by {self.author} ({self.pages}) [{status}]"


class Library:
    def __init__(self, name):
        self.name = name
        self._books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise ValueError("Invalid input")
        self._books.append(book)

    def find_by_title(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_by_author(self, author):
        return [book for book in self._books if book.author.lower() == book.author.lower()]

    def available_books(self):
        return [book for book in self._books if book.is_available]

    def checked_out_books(self):
        return [book for book in self._books if not book.is_available]

    def __str__(self):
        return f"{self.name} - {len(self._books)} books ({len(self.available_books())} available, {len(self.checked_out_books())} checked out)"


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("1984", "George Orwell", 328)
book3 = Book("Animal Farm", "George Orwell", 112)

lib = Library("City Library")
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)

print(lib)
# Expected: City Library — 3 books (3 available, 0 checked out)

book1.checkout()
print(book1.is_available)
# Expected: False

print(str(book1))
# Expected: The Great Gatsby by F. Scott Fitzgerald (180 pages) [Checked Out]

print(lib)
# Expected: City Library — 3 books (2 available, 1 checked out)

orwell_books = lib.find_by_author("george orwell")
print([str(b) for b in orwell_books])
# Expected: ['1984 by George Orwell (328 pages) [Available]',
#            'Animal Farm by George Orwell (112 pages) [Available]']

