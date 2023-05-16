# refer this link for python magic methods- https://rszalski.github.io/magicmethods/
class Magic:
    def __init__(self, x, y):
        print("init method")
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def add(self, x, y):
        return x+y
    # comparing objects

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    # Normal arithmetic operators

    def _add__(self, othernum):
        return Magic(self.x+othernum.x, self.y + othernum.y)  # not working


magic = Magic(2, 3)
point = Magic(2, 3)
# objects refer to different reference address in the memory. so both are not same
# returns false before adding _eq method
print("before adding methode:", magic == point)
# use comparative magic methods to compare 2 objects
print("after adding campartive method:", magic == point)
combined = magic + point
print("numeric arithmetic: ", combined.x)
print(str(magic))
print(type(str(magic)))  # class-str
print(type((magic)))  # class-main-Magic

# output
''' 
init method
(2, 3)
<class 'str'>
'''
