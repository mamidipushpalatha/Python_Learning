class Animal:  # parent class
    def __init__(self):
        self.x = 3

    def eat(self):
        print("eating")


class Dog(Animal):  # child class
    def walk(self):
        print("walking")


class Fish(Animal):
    def swim(self):
        print("swimming")


d = Animal()  # create object for parent class. Can access all the methods of parent class in child class
d.eat()  # eating
# d.walk()
# d.swim()
print("also access attribute in parent class", d.x)
