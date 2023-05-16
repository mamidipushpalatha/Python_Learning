class Magic:
    def __init__(self, x, y):
        print("init method")
        self.x = x
        self.y = y

    def _add__(self, othernum):
        return Magic(self.x+othernum.x, self.y + othernum.y)


magic = Magic(2, 3)
p = Magic(2, 3)
combined = magic + p
print("numeric arithmetic: ", combined.x)
