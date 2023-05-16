# multi level inheritance- 1 base class, 2 sub classes
class Animal:
    def eat(self):
        print("eating")


class Bird(Animal):
    def fly(self):
        print("flying")


class Chicken(Bird):
    pass


b = Chicken()  # chicken is inheriting from bird
b.fly()

# Mutiple inhertiance

# 2 base classes with 1 sub class


class Employe:
    def id(self):
        print("id")


class Person:
    def id(self):
        print("id is")


class Manager(Person, Employe):
    pass


# when obj is created for manager and calls both base classes. base class which is called first in sub class is executed first.
emp = Manager()
emp.id()
