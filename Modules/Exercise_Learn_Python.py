# count no.of words in senetence
sentence = input("type sentence: ")
res = sentence.count(' ')+1
print(res)
# the first digit is 8 or 9.
# The fourth digit is 8 or 9.
# The second and third digits are the same.
num1 = int(input("enter num1: "))
num2 = int(input("enter num2:"))
num3 = int(input("enter num3: "))
num4 = int(input("enter num4: "))
if ((num1 == 8 or num1 == 9) and (num4 == 8 or num4 == 9) and (num2 == num3)):
    print("ignore")
else:
    print('answer')


# if num1 == 8 or num1 == 9:
#     print("first digit", num1)

# elif num4 == 8 or num4 == 9:
#     print("forth digit", num4)
# else:
#     print("second and third", num2, num3)
