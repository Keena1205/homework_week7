# import Person class

from library.person import Person

class Employee(Person):
    def __init__(self, firstname, lastname, email, employee_id, position):
        super().__init__(firstname, lastname, email)
        self.__employee_id = employee_id
        self.position = position

    def get_employee_id(self):
        return self.__employee_id

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position
