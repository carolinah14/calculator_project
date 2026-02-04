from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
 }

def calculate():
    print(logo)
    calculation = True

    initial_number = float(input("What's the first number?:  "))

    while calculation:

        for key in operations:
            print(key)

        operation_chosen = input("Pick an operation:  ")

        secondary_number = float(input("What's the next number?:  "))

        initial_result = (operations[operation_chosen](initial_number,
                                                       secondary_number))

        print(f"{initial_number} {operation_chosen} {secondary_number}"
              f" = {initial_result}")

        keep_calculating = input(f"Type 'y' to continue calculating with {initial_result}"
                                 f", or type 'n' to start a new calculation: ")

        if keep_calculating == "y":
            initial_number = initial_result

        elif keep_calculating == "n":
            calculation = False
            print("\n" * 20)
            calculate()

calculate()
