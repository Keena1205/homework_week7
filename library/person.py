# create Person class

class Person:
    # this is the constructor
    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self._lastname = lastname
        self.__email = email

    # getters get the data
    # getter to call firstname
    def get_firstname(self):
        return self.firstname

    # getter to call lastname
    def get_lastname(self):
        return self._lastname

    # getter to call email
    def get_email(self):
        return self.__email

    # setters allow you to write data
    # setter to set lastname
    def set_lastname(self, lastname):
        if str(lastname).isalpha():
            self._lastname = lastname
        else:
            raise ValueError("Lastname must be alphabetic.")

    # setter to set email address
    def set_email(self, email):
        if "@" in str(email) and "." in str(email):
            self.__email = email
        else:
            raise ValueError("Your email address must contain @ and a domain. Please enter a valid email address.")
