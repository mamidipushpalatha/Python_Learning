# Sorting list of tuples with lamda function
item = [("prod5", 10), ("prod2", 50), ("prod3", 15)]
item.sort(key=lambda item: item[1])
print(item)
# map
prices = list(map(lambda i: i[1], item))
print(prices)
# filter- u can filter items
# filterted = list(filter(lambda i: i[1] > 30, item))

filterted = [i for i in item if i[1] > 10]
print(filterted)
# list comprehensive
p1 = [i[1] for i in item]
print(p1)
# zip
l1 = [1, 2, 3]
l2 = [5, 6, 7, 9]
print("Zipping 2 lists: " + str(list(zip(l1, 'ab', l2))))
