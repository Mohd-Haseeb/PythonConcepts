import datetime

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

    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


    @classmethod
    def create_new_employee(cls, emp_details:str):
        first_name, last_name, pay_amnt = emp_details.split('-')

        # return Employee(first_name, last_name, int(pay_amnt))
        return cls(first_name, last_name, int(pay_amnt))

    
    @staticmethod
    def is_weekday(day) -> bool:
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True
    
# Regular Methods in a class automaticlly take Instance as the first Argument. By converntion we call it `self` 
# Class Methods in a class automaticlly takes Class as the first Argument. By converntion we call it `Cls` 
#   -> Class Methods can be used as alternative constructors  
# Static Methods don't pass anything automatically like instance or classs methods



emp1 = Employee('Haseeb', 'Mohd', 1000)
emp2 =Employee('Shabrez', 'Mohd', 999)


print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

Employee.set_raise_amount(1.10)
# Employee.set_raise_amount(1.20)


# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

# CLASS METHOD AS AN ALTERNATE CONSTRUCTOR

emp_3_details = 'John-Doe-2000'
emp_4_details = 'Adam-Wick-1000'

# Method-1
first, last, pay = emp_3_details.split('-')
new_emp_3 = Employee(first, last, int(pay))

first, last, pay = emp_4_details.split('-')
new_emp_4 = Employee(first, last, int(pay))


print(new_emp_3.fullname())


# Method-2
emp_5_details = 'Tony-Stark-9999'

new_emp_5 = Employee.create_new_employee(emp_5_details)

print(new_emp_5.fullname())
print(new_emp_5.num_of_employee)
print(new_emp_5.pay)
new_emp_5.apply_raise()
print(new_emp_5.pay)


# Static Method use Case

my_date = datetime.datetime(2022, 12, 21)

print(Employee.is_weekday(my_date))
