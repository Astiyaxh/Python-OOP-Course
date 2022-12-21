# Python Object-oriented Programming #
# Section 4 ---> Creating SubClasses #

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        Employee.num_of_emps += 1
    
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())


emp_1 = Employee('Reza', 'Mehri', 500000)
emp_2 = Employee('Test', 'User', 600000)

dev_1 = Developer('Corey', 'Schafer', 500000, 'Python')
dev_2 = Developer('Hello', 'World', 600000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# print(help(Developer))

# print(dev_1.email)
# print(dev_2.email)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.prog_lang)
# print(dev_2.prog_lang)

# print(mgr_1.email)

# mgr_1.remove_emp(dev_1)
# mgr_1.add_emp(dev_2)

# mgr_1.print_emps()


print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
