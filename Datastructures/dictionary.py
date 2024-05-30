dic = {"name": "Akhitha", "id": 22}
d = dict(x=1, y=2)
print(d["x"])
dic["mobile"] = 122348998
print(dic)
if "xyz" in dic:
    print(dic["xyz"])
else:
    print("not found key")
# forloop
for k, v in dic.items():
    print(k, v)
# dictionary comprehensive

d1 = [x*2 for x in range(8)]
for x in d1:
    print(x)


d2 = {x*2 for x in range(5)}
print(d2)
d3 = (x*2 for x in range(5))
print(d3)
n = []
for i in range(4):
    n.append(i*2)
print("even numbers: " + str(n))


for i in range(5):
    if (i % 2 == 0):
        print(i)
    else:
        print("odd")
