# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def introduce(self):
#         print(f"Привет, меня зовут {self.name} и мне {self.age} лет.")
#
#
# class Employee:
#     def __init__(self, employee_id, salary):
#         self.employee_id = employee_id
#         self.salary = salary
#
#     def display_employee_info(self):
#         print(f"ID сотрудника: {self.employee_id}, Зарплата: {self.salary}")
#
#
# class Manager(Person, Employee):
#     def __init__(self, name, age, employee_id, salary, department):
#         Person.__init__(self, name, age)
#         Employee.__init__(self, employee_id, salary)
#         self.department = department
#
#     def manage_team(self):
#         print(f"{self.name} управляет отделом {self.department}.")
#
#
#     def introduce(self):
#         print(f"Привет, меня зовут {self.name}, мне {self.age} лет, и я руковожу отделом {self.department}.")
#

#
# manager = Manager(name="John", age=35, employee_id="E123", salary=60000, department="IT")
# manager.introduce()  # Вызывает переопределенный метод introduce
# manager.display_employee_info()  # Метод из класса Employee
# manager.manage_team()  # Метод из класса Manager

import random

class NumberEncryptor:
    def __init__(self, number):
        self._number = number

    def _perform_random_operation(self):
        operation = random.choice(['+', '-', '*', '/'])
        operand = random.randint(1, 10)

        if operation == '+':
            self._number += operand
        elif operation == '-':
            self._number -= operand
        elif operation == '*':
            self._number *= operand
        elif operation == '/':
            if operand != 0:
                self._number /= operand

    def __str__(self):
        self._perform_random_operation()
        return str(self._number)



encryptor = NumberEncryptor(10)
print(encryptor)
print(encryptor)


