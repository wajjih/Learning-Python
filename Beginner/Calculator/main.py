from art import logo


# operation functions
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Dictionary that maps operation
operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("Enter first number: "))
    for i in operation:
        print(i)
    should_continue = True
    while should_continue:

        operator = input("Enter operator: ")
        num2 = float(input("Enter next number: "))

        answer = operation[operator](num1, num2)

        print(f"{num1} {operator} {num2} = {answer}")
        ask = input(f"type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
        if ask == "n":
            should_continue = False
            calculator()
        else:
            num1 = answer


calculator()
