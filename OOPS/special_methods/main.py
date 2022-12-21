class Employee:
    


    raise_amount = 1.06 
    num_of_employee = 0


    def __init__(self, first:str, last:str, pay:int) -> None:
        self.first = first # instance variable / attribute
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        Employee.num_of_employee += 1

    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    # meant for the umambigious representration of the object
    def __repr__(self) -> str:
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    
    # meant for the readable representration of the object
    def __str__(self) -> str:
        return "{} -> {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Mohd', 'Haseeb', 100)
emp_2 = Employee('Mohd', 'Shabrez', 100)

print(emp_1)

# our custom __add__ dunder will return sum of the pay
print(emp_1 + emp_2)
print(emp_1.__add__(emp_2))

print(len(emp_1))
print(emp_1.__len__())



print(repr(emp_1))
print(str(emp_1))
print('------------------------')
print(emp_1.__repr__())
print(emp_1.__str__())


print('------------------------')

print(1+2)
print(int.__add__(1,2))


print(str.__add__('a', 'b'))

print('------------------------')

print(len('testing'))
print('testing'.__len__())