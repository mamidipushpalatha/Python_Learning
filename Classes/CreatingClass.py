# Creating class
class Point:
    def add(self):
        print("draw")


p = Point()
print(type(p))
print(isinstance(p, Point))  # true
print(isinstance(p, int))  # false

# constrictors


# self variable is a must in creating a constructor by using __init__

class Cons:
    def __init__(self, x, y):
        self. x = x
        self .y = y

    def draw(self):
        print(f"Cons ({self.x},{self.y})")


# point1 = Cons()
point1 = Cons(1, 2)
# print(point1.x, point1.y)  # 1 2
point1.draw()  # drawing....from  1  to  2
