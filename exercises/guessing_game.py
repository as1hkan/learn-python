import random

number = random.randint(1, 100)

for attempt in range(3):
    guess = int(input("Enter your guess: "))

    if guess <   number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("Correct 🎉")
        break
else:
    print(f"You lost! The number was {number}")