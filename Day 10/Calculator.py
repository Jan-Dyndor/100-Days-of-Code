from art import logo

# Functions


def add(a, b):
    """Adding two numbers and returns a result"""
    return a + b


def subtract(a, b):
    """Subtracting two numbers and returns a result"""
    return a - b


def multiply(a, b):
    """Multiplication of two numbers and returns a result"""
    return a * b


def divide(a, b):
    """Dividing two numbers and returns a result"""
    return a / b


# Storing function in dictionary
# later we will be able to just pass 2 numbers
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def my_calc():
    again = True
    num1 = float(input("What is a first number? "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from line above: ")
    num2 = float(input("What is a second number? "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{answer} {operation_symbol} {num2} = {answer}")
    while again:
        next_calculation = input(
            f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: "
        )
        if next_calculation == "n":
            again = False
            my_calc()
        num3 = float(input("What is a next number? "))
        operation_symbol = input("Pick an operation from line above: ")
        calculation_function = operations[operation_symbol]
        next_answer = calculation_function(answer, num3)
        print(f"{answer} {operation_symbol} {num3} = {next_answer}")
        answer = next_answer


# Angelas code
def calculator():
    print(logo)
    num1 = float(input("What is a first number?: "))
    for operation in operations:
        print(operation)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?:"))
        calc_operation = operations[operation_symbol]
        result = calc_operation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        if (
            input(
                f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: "
            )
            == "y"
        ):
            num1 = result
        else:
            should_continue = False
            calculator()


# # We define calculator function so the user can choos if he wont to start a new calculator wit different numbers. It is RECURSION
calculator()
# my_calc()
