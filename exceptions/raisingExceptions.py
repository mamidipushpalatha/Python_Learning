def cal_age(age):
    if age <= 0:
        raise ValueError("age cannot be 0 or less than 0")
    return 10/age


try:
    print(cal_age(-1))
except ValueError as err:
    print("error", err)
