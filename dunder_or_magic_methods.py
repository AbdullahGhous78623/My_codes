class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"
    def __call__(self):
        print("Hey i am good.")

# Creating an instance of the Book class
book = Book("1984", "George Orwell", 1949)

# Using str() or print() calls __str__
print(str(book))  # Output: '1984' by George Orwell (1949)
print(book)       # Output: '1984' by George Orwell (1949)

# Using repr() or typing the object name in the interpreter calls __repr__
print(repr(book)) # Output: Book(title='1984', author='George Orwell', year=1949)
           # Output: Book(title='1984', author='George Orwell', year=1949)

book()

