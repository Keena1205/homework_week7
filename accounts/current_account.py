from mmap import ACCESS_COPY


class CurrentAccount:
    def __init__(self, balance, firstname, lastname, account_number):
        self.__balance = balance
        self.firstname = firstname
        self._lastname = lastname
        self.__account_number = account_number

    def get_balance(self):
        # dunder means completely private
        return self.__balance

    def get_firstname(self):
        # no underscore is completely public
        return self.firstname

    def get_lastname(self):
        # single underscore means semi private
        return self._lastname

    def get_account_number(self):
        # dunder means completely private
        return self.__account_number

    def set_lastname(self, lastname):
        # ValueError is a builtin exception and it's ideal here; we don't like the value of lastname if it's not alphabetical
        if str(lastname).isalpha():
            self._lastname = lastname
        else:
            raise ValueError("Lastname must be alphabetic")

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def deposit(self, amount):
        self.__balance += amount


    def withdraw(self, amount):
        self.__balance -= amount

    def __str__(self):
        return f"Bank account holder: {self.firstname} {self._lastname}\nHas balance: {self.__balance}"