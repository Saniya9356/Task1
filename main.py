def calculator():
    try:

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ValueError("Error: Cannot divide by zero.")
            result = num1 / num2
        else:
            raise ValueError("Error: Invalid operation entered.")

        print(f"The result of {num1} {operation} {num2} = {result}")

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")


calculator()
