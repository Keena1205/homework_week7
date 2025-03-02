# Nice to have: consider creating book profiles / library catalogue and updating that based on a user adding/removing a book

# import Person class

from library.person import Person

class Customer(Person):
    def __init__(self, firstname, lastname, email, member_id, borrowed_books):
        super().__init__(firstname, lastname, email)
        self.__member_id = member_id
        self.borrowed_books = borrowed_books

    def get_member_id(self):
        return self.__member_id

    def get_borrowed_books(self):
        return self.borrowed_books

    def set_member_id(self, member_id):
        self.__member_id = member_id

    def borrow_book(self, book_title):
        self.borrowed_books.append(book_title)

    def return_book(self, book_title):
        self.borrowed_books.remove(book_title)
        return book_title
