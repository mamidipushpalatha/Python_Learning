from pprint import pprint
sentence = "this is common interview question"
repeated_char = {}
for i in sentence:
    if i in repeated_char:
        repeated_char[i] += 1
    else:
        repeated_char[i] = 1
# pprint(repeated_char)
newlist = sorted(list(repeated_char.items()), key=lambda i: i[1], reverse=True)
pprint(newlist)
c = newlist[0][0]
print("most repeated char is: ", c)
