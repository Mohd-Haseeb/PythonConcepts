class Employee:
    
    # Instance Varibales are unique to all the instances of a Class
    # Class Varibles are shared acroess all the instances of the Class

    raise_amount = 1.06 # Class Variable
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

    



emp1 = Employee('Haseeb', 'Mohd', 1000)
emp2 =Employee('Shabrez', 'Mohd', 999)

print(emp1.fullname())
print(emp2.fullname())

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)


# print(emp1.raise_amount)
# emp1.raise_amount = 1.04
# Employee.raise_amount = 1.04
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# print(Employee.raise_amount)


