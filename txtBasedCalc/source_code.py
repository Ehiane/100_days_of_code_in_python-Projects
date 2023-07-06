from dependecies import logo, operations, clear_screen;


def calculator():
    print(logo)
    num1 = float(input("Enter the first number: "))
    should_continue = True


    while should_continue:

        print("Available operations:")

        for symbol in operations:
            print(symbol)
        
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Enter the next number: "))

        calculation_function = operations.get(operation_symbol)

        if calculation_function:

            answer = calculation_function(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")

            prompt = input(f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation, or q to quit the application: ")

            if prompt == "y":
                num1 = answer
            elif prompt == "n":
                clear_screen()
                calculator()
            else:
                should_continue = False

calculator();