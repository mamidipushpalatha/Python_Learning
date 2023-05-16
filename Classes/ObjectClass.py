
# By default Object is base class in python
class Animal(object):  # parent class

    def eat(self):
        print("eating")


class Dog(Animal):  # child class
    def walk(self):
        print("walking")


d = Dog()
print(isinstance(d, Dog))  # True- d is instance(object) of class Dog
print(issubclass(Dog, Animal))  # True- Dog is subclass of Animal
print("Object is base class in python:", issubclass(Animal, object))
