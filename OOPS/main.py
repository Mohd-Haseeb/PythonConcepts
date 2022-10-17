

class Subject:
    def __init__(self, name, marks:list) -> None:
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks)/len(self.marks)


science = Subject('science', [12,24,13])

# print(science.average())

# print(Subject.average(science))


def average(stu:Subject):
    return sum(stu.marks)/len(stu.marks)


# print(average(science))


names = ['a', 'b', 'c', 'd']
# print(names.__class__)


class MyList:
    def __init__(self) -> None:
        self.list = []

    def addToMyList(self, num):
        self.list.append(num)

    ## magic methods
    def __len__(self):
        count = 0
        for _ in self.list:
            count += 1
        return count

    def __getitem__(self, i):
        return self.list[i]

    # __repr__ is used when we are debugging
    def __repr__(self):
        return f"<MyList {self.list}>"

    # __str__ returns somethiing a user wants to read
    def __str__(self):
        return f"MyList having {len(self)} elements in it"


scores = MyList()
scores.addToMyList(10)
scores.addToMyList(64)
scores.addToMyList(53)
scores.addToMyList(104)
scores.addToMyList(23)

print(scores.list)

#
print( len(scores))

# get item -> to access its individual values
print(scores[3])


# ONCE WE HAVE THESE TWO METHODS(__len__ & __getitem__) defined, we can iterate through the object
# for i in scores:
#     print(i)

print(scores)
# MyList having 5 elements in it



