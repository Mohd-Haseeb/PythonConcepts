class Employee:



    def __init__(self, first:str, last:str, pay:int) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

    def fullname(self) -> str:
        return f"{self.first} {self.last}"



emp1 = Employee('Haseeb', 'Mohd', 1000)
emp2 =Employee('Shabrez', 'Mohd', 999)

print(emp1.fullname())
print(emp2.fullname())




