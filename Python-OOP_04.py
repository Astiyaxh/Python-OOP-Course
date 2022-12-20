# Python Object-oriented Programming #
# Section 4 ---> Creating SubClasses #

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1
    
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    pass

emp_1 = Employee('Reza', 'Mehri', 500000)
emp_2 = Employee('Test', 'User', 600000)

dev_1 = Developer('Corey', 'Schafer', 500000)
dev_2 = Developer('Hello', 'World', 600000)

# print(help(Developer))

# print(dev_1.email)
# print(dev_2.email)