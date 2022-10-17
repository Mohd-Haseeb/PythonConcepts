
class Student:
    def __init__(self, name, school) -> None:
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, school, salary) -> None:
    
        super().__init__(name, school)
        self.salary = salary


    @property
    def weekly_salary(self):
        return self.salary * 20

haseeb = WorkingStudent('haseeb', 'lsts', 12 )

haseeb.marks.append(10)
haseeb.marks.append(14)
haseeb.marks.append(100)

print(haseeb.average())

print(haseeb.weekly_salary)
    