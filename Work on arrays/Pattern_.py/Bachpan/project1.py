class Library:
    def __init__(self, list_of_books):
        self.available_books = list_of_books

    def display_books(self):
        print("\nBooks available in the library:")
        for book in self.available_books:
            print(f"- {book}")
    
    def lend_book(self, requested_book):
        if requested_book in self.available_books:
            print(f"\nYou have borrowed '{requested_book}'")
            self.available_books.remove(requested_book)
        else:
            print(f"\nSorry, the book '{requested_book}' is currently not available.")
    
    def add_book(self, returned_book):
        self.available_books.append(returned_book)
        print(f"\nThank you for returning '{returned_book}'.")

class User:
    def request_book(self):
        print("\nEnter the name of the book you'd like to borrow:")
        self.book = input()
        return self.book

    def return_book(self):
        print("\nEnter the name of the book you'd like to return:")
        self.book = input()
        return self.book

if __name__ == "__main__":
    library = Library(['Python Programming', 'Data Structures and Algorithms', 'Machine Learning', 'Artificial Intelligence'])
    user = User()

    while True:
        print("\n\n==== Library Menu ====")
        print("1. Display all available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")
        
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            library.display_books()

        elif choice == 2:
            requested_book = user.request_book()
            library.lend_book(requested_book)

        elif choice == 3:
            returned_book = user.return_book()
            library.add_book(returned_book)

        elif choice == 4:
            print("\nThank you for using the library management system. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.")



# Project Summary: Library Management System
# The Library Management System is a simple Python-based program designed to simulate basic library operations like displaying available books, lending books, and returning books. The system has two main components: the Library class and the User class.

# Library Class:

# Attributes:
# available_books: A list containing the books available in the library.
# Methods:
# display_books(): Prints a list of all available books.
# lend_book(requested_book): Allows a user to borrow a book if it's available. If not, it informs the user that the book is currently not available.
# add_book(returned_book): Adds a returned book back to the available books list and thanks the user for returning it.
# User Class:

# Methods:
# request_book(): Prompts the user to enter the name of the book they wish to borrow and returns it.
# return_book(): Prompts the user to enter the name of the book they wish to return and returns it.
# Main Program:

# A menu-driven interface is provided to the user with four options:
# Display all available books: Shows the list of books currently available in the library.
# Borrow a book: The user can request a book to borrow, and the system checks if it is available.
# Return a book: The user can return a borrowed book, and it is added back to the library.
# Exit: Exits the program.
# Looping Structure: The program runs in a loop, continuously showing the menu and processing the user's input until they choose to exit.

# This project demonstrates core object-oriented programming principles like abstraction (the user interacts with the library system without knowing its internal workings), encapsulation (data is managed within classes), and the use of methods to handle operations.


