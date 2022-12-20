# Python Object-oriented Programming

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