from array import array
numbers = array("i", [1, 2, 3, 4, 5])
print(numbers)  # array('i', [1, 2, 3, 4, 5])
print(type(numbers))

print(numbers[1])
numbers[0] = 20
numbers.append(100)
numbers.remove(5)
print(numbers)
# sets
li = [1, 2, 3, 4, 4, 4, 5, 6, 5]
print("list is: " + str(li))
s = set(li)
print("set is: " + str(s))
s1 = set([11, 22, 33, 11, 11, 44, 11])
print(s1)
