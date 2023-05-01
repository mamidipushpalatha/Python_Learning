# Enumerated builtin function

m = ["a", "b", "c", "d"]
# for i, j in enumerate(m):
#     print(i, j)
#  adding items
m.append("akhitha")
# adding items with index
m.insert(0, "_")
m.insert(5, "raju")
# removing items with index- only 1 item at a time is removed
m.pop(0)
# removes items from list
m.remove("c")
# removes range of items with index
del m[0:2]
# removes all elements from list
m.clear()
print(m)
n = ["a", "b", "c"]
print(n.index("b"))
# counting of list items
print(n.count("a"))
l = [1, 4, 7, 2]
# Sort- sorting list in ascending order-modifies original list and reverse=true sorts in descending order
# l.sort(reverse=True)
# print(l)
# sorted- created new list after sorting
print(sorted(l, reverse=True))


k = ["a", "b", "k"]
if "a" in k:
    print(k.index("j"))
