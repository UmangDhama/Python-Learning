from art import logo

def calc(fnum, snum, operand):
    if operand == "+":
        result = fnum + snum
        return result
    elif operand == "-":
        result = fnum - snum
        return result
    elif operand == "*":
        result = fnum * snum
        return result
    elif operand == "/":
        result = fnum / snum
        return result


def calculator():
    print(logo)
    # Take the first input number
    num1 = float(input("What's the first number?: "))

    # Flag to continue calculation
    ans = True

    while ans:
        # Show available operations
        print("+")
        print("-")
        print("*")
        print("/")

        # Take operation and next number
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        # Call calc function to compute result
        res = calc(num1, num2, operation)

        # Show result
        print(f"{num1} {operation} {num2} = {res}")

        # Ask user whether to continue
        cont = input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation: ")
        if cont == "y":
            num1 = res
        else:
            ans = False
            print("\n" * 20)
            calculator()

calculator()

