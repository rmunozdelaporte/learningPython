import math


def split_bill(total, number_of_people):
    if number_of_people < 1:
        raise ValueError("More than 1 person is required to split the check")
    return math.ceil(total / number_of_people)


try:
    total_bill = float(input("What is the total of the bill? "))
    persons = int(input("How many people were having dinner? "))
    each_person = split_bill(total_bill, persons)
except ValueError as err:
    print("Oh no! That's not a valid value. Try again...")
    print("{}".format(err))
else:
    print(f"Each person should pay {each_person}")

