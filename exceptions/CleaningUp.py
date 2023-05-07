try:
    file = open("CleaningUp.py")
    name = input("Name: ")
    age = int(input("Age: "))
    xfactor = 10 / age
    print("hi! ", name, ":  your age is ", age)
    file.close()

except (ValueError, ZeroDivisionError) as ex:
    print("entered invalid age. ", ex)
else:
    print("No exceptions reported")  # only in case no exceptions raised
finally:

    print("cleaned up the resources")
