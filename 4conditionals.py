first_name = input("What is your name? ")
print("Hello", first_name)
if first_name == "Craig":
    print(first_name, "is learning Python")
elif first_name == "Rodrigo":
    print(first_name, "is learning with fellow students in the community! Me too!")
else:
    age = int(input("How old are you? "))
    if age <= 6:
        print("Wow you're {}! If you are confident with your reading already...".format(age))
    print("You should totaly learn Python, {}".format(first_name))
print(f"Have a great day {first_name}")