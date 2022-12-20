# Python Object-oriented Programming
# a method is a function that associated with the class.
# a class is blue print for creating a instances.


class Employee:

    def __init__(self, first, last, pay):
        self.first = first # you can put it that way --> self.fname = first BUT we are keept things simple
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('Reza', 'Mehri', 500000)
emp_2 = Employee('Test', 'User', 600000)

# print(emp_1)
# print(emp_2)

# emp_1.first = 'Reza'
# emp_1.last = 'Mehri'
# emp_1.email = 'Reza.Mehri@company.com'
# emp_1.pay = 500000

# emp_2.first = 'ُTest'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 600000

# print(emp_1.email)
# print(emp_2.email)

# print(f'{emp_1.first} {emp_1.last}')
# print('{} {}'.format(emp_1.first, emp_1.last))

print(emp_1.fullname())
print(emp_2.fullname())
print(Employee.fullname(emp_1)) # in background this --> emp_1.fullname() transforms to this --> Employee.fullname(emp_1)