try:
    age = int(input("enter age:"))
except ValueError:
    print("getting value error")
    print("execution contimues..")
else:
    print("No exceptions reported")  # only in case no exceptions raised
print("Execution contiues")
