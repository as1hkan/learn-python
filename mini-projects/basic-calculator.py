try:
    num1 = int(input("Enter your number 1: "))
    num2 = int(input("Enter your number 2: "))
    op = input("Enter your operation: ")

    if op == "+":
        print(num1 + num2)

    elif op == "-":
        print(num1 - num2)

    elif op == "*":
        print(num1 * num2)

    elif op == "/":
        if num2 == 0:
            print("I can't divide by zero")
        else:
            print(num1 / num2)

    else:
        print("Enter a valid operation")

except ValueError:
    print("Please enter valid numbers")
