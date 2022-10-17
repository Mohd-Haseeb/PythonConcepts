from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    def walk(self):
        print('Walking...')

    @abstractmethod
    def no_legs(self):
        pass



class Dog(Animal):
    def __init__(self, name) -> None:
        self.name = name

    def no_legs(self):
        return 4


class Monkey(Animal):
    def __init__(self, name) -> None:
        self.name = name

    def no_legs(self):
        return 2





# a = Animal() -> Error : We cannot create object of a class having abstract method
# a.walk()

dog = Dog('tom')

print(dog.no_legs())

monkey = Monkey('poiuy')
print(monkey.name)