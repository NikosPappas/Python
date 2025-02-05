import datetime

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

    def mark_as_borrowed(self):
      self.is_borrowed = True

    def mark_as_returned(self):
      self.is_borrowed = False

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}"

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)


class Loan:
    def __init__(self, book, member, borrow_date, due_date):
        self.book = book
        self.member = member
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = None

    def record_return(self, return_date):
        self.return_date = return_date

    def is_overdue(self):
        return self.return_date is None and datetime.date.today() > self.due_date

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member_by_id(self, member_id):
         for member in self.members:
            if member.member_id == member_id:
                return member
         return None

    def borrow_book(self, isbn, member_id, due_date):
        book = self.find_book_by_isbn(isbn)
        member = self.find_member_by_id(member_id)

        if book is None or member is None:
            return False  # Book or member not found

        if book.is_borrowed:
            return False # Book is already borrowed

        loan = Loan(book, member, datetime.date.today(), due_date)
        self.loans.append(loan)

        book.mark_as_borrowed()
        member.borrow_book(book)
        return True

    def return_book(self, isbn, member_id, return_date):
        book = self.find_book_by_isbn(isbn)
        member = self.find_member_by_id(member_id)

        if book is None or member is None:
            return False  # Book or member not found

        # Find the relevant loan
        loan = next((loan for loan in self.loans if loan.book == book and loan.member == member and loan.return_date is None), None)

        if loan is None:
            return False #Loan not found

        loan.record_return(return_date)
        book.mark_as_returned()
        member.return_book(book)
        return True

    def display_available_books(self):
        available_books = [book for book in self.books if not book.is_borrowed]
        if available_books:
            print("Available Books:")
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")

    def display_overdue_books(self):
        overdue_books = [loan.book for loan in self.loans if loan.is_overdue()]
        if overdue_books:
            print("Overdue Books:")
            for book in overdue_books:
                print(book)
        else:
            print("No books are overdue.")

# Example Usage
library = Library()

book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", "9780618260222")
book2 = Book("Pride and Prejudice", "Jane Austen", "9780141439518")
library.add_book(book1)
library.add_book(book2)

member1 = Member("M123", "Alice Smith")
member2 = Member("M456", "Bob Johnson")
library.add_member(member1)
library.add_member(member2)

#Borrow a book
library.borrow_book("9780618260222", "M123", datetime.date(2024, 2, 15))

library.display_available_books() # Pride and Prejudice should only be available
library.display_overdue_books() # Nothing should show

#Simulate making it overdue
library.loans[0].due_date = datetime.date(2023,1,1)
library.display_overdue_books() #Lord of the Rings should show