from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
# named tuple is immutable so if we want to change value create another object
p1 = Point(x=10, y=2)
print("x is: ", p1.x)
print(p1 == p2)
