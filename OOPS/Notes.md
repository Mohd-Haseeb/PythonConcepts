In Python classes, Functions which start with __ and end with __ are called __DUNDER__ functions.

OBJECT ORIENT PROGRAMMING is used to conceptualise the interactions between objects


## Classes and Objects :

- Objects are conceptualization of entities in our programme. They represent things we want to interact with.

- ***Class*** is definition of the object

- When we call a class, we create an empty object and that particular object is referred as 'self'(not mandatory) and it is always first parameter of any method in the class.

- When we define a variable inside a class, it is called as ***Property***.

- When we define a function inside a class, we call it ***Method***

- When we use an object to call function of a class, it automatically populates 'self' as the object that called the function.

- Dunder __init__ method is called automatically whenever we create an Object.

```python
    class Subject:
        def __init__(self, name, marks:list) -> None:
            self.name = name
            self.marks = marks

        def average(self):
            return sum(self.marks)/len(self.marks)


    science = Subject('science', [12,24,13])

    print(science.average())

    # THIS IS WHAT ACTUALLY HAPPENS WHEN WE CALL A METHOD USING OBJECT. 
    print(Subject.average(science))


    def average(stu:Subject):
        return sum(stu.marks)/len(stu.marks)


    print(average(science))


```


## Magic Methods


- Every thing is pretty much an object in Python

```python

names = ['a', 'b', 'c', 'd']

print(names.__class__)
# o/p : <class 'list'>


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
for i in scores: # no error
    print(i)

print(scores)
# o/p : MyList having 5 elements in it


```

- What does it mean for a list to be an object ?

    - Lets create our very own list Class and see!


## Inheritance

- We use inheritance to avoid duplication or repetition of code.

- super() represents the Parent class


- If a method doesn't perfoem any action rather just calculates a value, we can consider it as  a property by using __@property__ decorator. We can only do this if the method doesn't take any argument other than __self__.


## Methods in Python Class:

- Instance Method
    - Takes the callers object as the first argument i.e self

- Class Method
    - Takes callers CLASS as the first argument

- Static Method
    Takes nothing as the argument