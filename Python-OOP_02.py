# Python Object-oriented Programming

class Employee:

    num_of_emps = 0
    raise_amount = 1.04 # this is a class variable

    def __init__(self, first, last, pay):
        self.first = first # this is a instance variable
        self.last = last 
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1
    
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        #self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount) # we can access to class variables from instances


print(Employee.num_of_emps)

emp_1 = Employee('Reza', 'Mehri', 500000)
emp_2 = Employee('Test', 'User', 600000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(emp_1.__dict__)
# print(Employee.__dict__)

# Employee.raise_amount = 1.05
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_1.raise_amount = 1.06
# print(emp_1.__dict__)
# print(emp_1.raise_amount)

print(Employee.num_of_emps)