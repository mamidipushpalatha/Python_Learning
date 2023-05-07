try:
    with open("withStatement.py") as file1:
        name = input("Name: ")
    age = int(input("Age: "))
    xfactor = 10 / age

    print("hi! ", name, ":  your age is ", age)
except (ValueError, ZeroDivisionError) as ex:
    print("invalid age", ex)
else:
    print("execution continues..")
