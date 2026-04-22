name = input("Enter your name: ")

try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Age cannot be negative.")

    elif age > 100:
        print("Bro, are you texting me from the graveyard?")

    elif age == 50:
        print(f"{name}, you are exactly 50 years old!")

    elif age < 50:
        years_left = 50 - age
        print(f"{name}, you will be 50 in {years_left} years.")

    else:
        years_passed = age - 50
        print(f"{name}, you passed 50 by {years_passed} years.")

except ValueError:
    print("Please enter a valid number for age.")