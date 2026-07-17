# calculator.v4
answer = None


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    if number2 == 0:
        return print("divison by zero is not possible")
    return number1 / number2


def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


operations = {"*": multiply,
              "/": divide,
              "+": add,
              "-": subtract
              }
# get user information
command = input("Type start to begin or quit to exit:")
if command == "start":

    choice = input("Type quit to stop or enter to continue:")

    while choice != "quit":
        if answer is None:
            while True:
                try:
                    number1 = float(
                        input("enter the first number").replace(",", "."))
                    break
                except ValueError:
                    print("invalid number")
            operator = input("enter the operator")
            while operator not in operations:
                print("invalid operator")
                operator = input("enter the operator")
            while True:
                try:
                    number2 = float(
                        input("enter the second number").replace(",", "."))
                    break
                except ValueError:
                    print("invalid number")
            answer = operations[operator](number1, number2)
            print(answer)
        else:
            operator = input("enter the operator")
            while operator not in operations:
                print("invalid operator")
                operator = input("enter the operator")
            while True:
                try:
                    number2 = float(
                        input("enter the second number").replace(",", "."))
                    break
                except ValueError:
                    print("invalid number")
            answer = operations[operator](answer, number2)
            print(answer)
        choice = input("Type quit to stop or enter to continue:")
