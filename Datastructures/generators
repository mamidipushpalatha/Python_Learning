from sys import getsizeof
d3 = (x*2 for x in range(10))
print(type(d3))
print("gen:", getsizeof(d3))  # size-208
# print(len(d3)) -object of type 'generator' has no len()
for x in d3:
    print(x)
# list allocates more memory than generator
d1 = [x*2 for x in range(20)]
print("list:", getsizeof(d1))  # size-248
print(d1)
