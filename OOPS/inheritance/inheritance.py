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



class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first: str, last: str, pay: int, language:str) -> None:
        super().__init__(first, last, pay)
        self.language = language


class Manager(Employee):

    def __init__(self, first: str, last: str, pay: int, employees=None) -> None:
        super().__init__(first, last, pay)

        if employees is None:
            self.employess = []
        else:
            self.employess = employees

     
    def add_employee(self, emp : Employee):
        if emp not in self.employess:
            self.employess.append(emp)


    def remove_employee(self, emp : Employee):
        if emp  in self.employess:
            self.employess.remove(emp)

    def print_employess(self):
        for emp in self.employess:
            print("--> ", emp.fullname())

    

dev_1 = Developer('Adam', 'Warlock', 1000, 'C#')
dev_2 = Developer('Steve', 'Afflect', 1000, 'typescript')

manager_1 = Manager('Narueo', 'Uzumaki', 10000, [dev_1])


print(manager_1.email)

# print(manager_1.print_employess())

manager_1.add_employee(dev_2)

# print(manager_1.print_employess())

manager_1.remove_employee(dev_1)

# print(manager_1.print_employess())


# print(dev_1.email)
# print(dev_1.language)


# print(help(Developer)) # to visualise the `resolution order`


# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)


# print(dev_2.pay)
# dev_2.apply_raise()
# print(dev_2.pay)



# SPECIAL METHODS
print(isinstance(manager_1, Manager))
print(isinstance(manager_1, Employee))

print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))