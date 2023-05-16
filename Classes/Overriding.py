class Animal:  # parent class
    def __init__(self):
        print("Animal constructor")
        self.age = 3

    def eat(self):
        print("eating")
        self.food = "veg"

# Overriding a method- acessing base class methods in sub class and modift method accordingly


class Dog(Animal):  # child class
    def __init__(self):
        print("dog constructor")
        super().__init__()

        self.weight = 25

    def walk(self):
        print("walking")

    def eat(self):
        # self.item = "nonveg"
        self.food = "non"
        print("eating")


a = Dog()
a.eat()
print(a.age)
print(a.weight)
print(a.food)
