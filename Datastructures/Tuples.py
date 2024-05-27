point = 1, 3 * 2
p = (1, 3) * 3
print(p)
print(point)
n = ("hai", "bye")
print(n)
l = tuple(["akhitha", "raju"])
print(l)
m = tuple("hello")
print(m)
list1 = [1, "hai"]
tupleFromAList = tuple(list1)
print(type(tupleFromAList))  # <lass 'tuple'>
print(tupleFromAList)  # (1, 2)
# reversing tuple
t = (2, 3, 4, 5)
print(type(t))
print(t[1])
print(t[::-1])
t2 = [(1, 2), (3, 4)]
print(type(t2))
print(t2[0])
print(t2[::-1])
# swapping variables
x = 1
y = 2
print(x, y)

z = x
x = y
y = z
print(x, y)
i, j = 10, 20
i, j = (j, i)  # by using the concept of unpacking tuple
print(i, j)  # 10 20
