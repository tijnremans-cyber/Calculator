answer = None


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    if number2 == 0:
        raise ValueError("Division by zero is not possible.")
    return number1 / number2


def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


operations = {
    "*": multiply,
    "/": divide,
    "+": add,
    "-": subtract
}


def get_number(prompt):
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Invalid number.")


def get_operator():
    while True:
        operator = input("Enter the operator (+, -, *, /): ")
        if operator in operations:
            return operator
        print("Invalid operator.")


def main():
    answer = None

    while True:
        command = input("Type 'start' to begin or 'quit' to exit: ").lower()

        if command == "start":
            break
        elif command == "quit":
            return
        else:
            print("Invalid command.")

    while True:
        if answer is None:
            number1 = get_number("Enter the first number: ")
        else:
            number1 = answer
            print(f"Current answer: {answer}")

        operator = get_operator()
        number2 = get_number("Enter the second number: ")

        try:
            answer = operations[operator](number1, number2)
            print(f"Answer: {answer}")
        except ValueError as error:
            print(error)

        choice = input(
            "Press Enter to continue or type 'quit' to exit: ").lower()

        if choice == "quit":
            break


if __name__ == "__main__":
    main()
