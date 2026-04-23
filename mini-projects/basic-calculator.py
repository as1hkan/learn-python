from colorama import Fore, Style, init

init()

try:
    num1 = float(input(Fore.CYAN+"Enter first number: "+Style.RESET_ALL))
    num2 = float(input(Fore.CYAN+"Enter second number: "+Style.RESET_ALL))
    op = input(Fore.YELLOW+"Enter your operation: "+Style.RESET_ALL)
    match op:
        case "+":
            print(f"Result: {num1 + num2}")
        case "-":
            print(f"Result: {num1 - num2}")
        case "*":
            print(f"Result: {num1 * num2}")
        case "/":
            if num2 == 0:
                print(Fore.RED + "You can't divide by zero!"+Style.RESET_ALL)
            else:
                print(f"Result: {num1 / num2}")
        case _:
            print(Fore.RED + "Enter a valid operation!"+Style.RESET_ALL)
except ValueError:
    print(Fore.RED + "Please enter valid numbers"+Style.RESET_ALL)
