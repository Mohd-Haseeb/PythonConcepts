class Employee:
    


    raise_amount = 1.06 
    num_of_employee = 0


    def __init__(self, first:str, last:str, pay:int) -> None:
        self.first = first # instance variable / attribute
        self.last = last
        self.pay = pay
        # self.email = first+'.'+last+'@company.com'
        Employee.num_of_employee += 1

    @property
    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    # getter
    @property
    def email(self):
        return "{}.{}@email.in".format(self.first, self.last)

    # setter
    @fullname.setter
    def fullname(self, name):
        first, last  = name.split(' ')
        self.first = first
        self.last = last


    @fullname.deleter
    def fullname(self):
        print("Name deleted")
        self.first = self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

   

emp_1 = Employee('Mohd', 'Haseeb', 100)
emp_2 = Employee('Mohd', 'Shabrez', 100)

emp_1.first = 'test'

print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = 'Lufy D'

print(emp_1.fullname)
print(emp_1.email)

del emp_1.fullname