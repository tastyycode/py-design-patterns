"""
Prototype Factory"""

import copy


class Address:
    def __init__(self, street, suite, city):
        self.street = street
        self.suite = suite
        self.city = city

    def __str__(self):
        return f'{self.street}, Suite #{self.suite}, {self.city}'

class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} works at {self.address}'

class EmployeeFactory:

    main_office_employee = Employee('', Address('123 East Drive', 0, 'London'))
    aux_office_employee = Employee('', Address('123B East Drive', 0, 'London'))

    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name, suite):
        """Create a main office employee.

        Args:
            name (str): Employee's name
            suite (int): Suite where the employee works at
        """
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name,
            suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name,
            suite
        )


john = EmployeeFactory.new_main_office_employee('John', 101)
bart = EmployeeFactory.new_aux_office_employee('Bart', 200)

print(john)
print(bart)