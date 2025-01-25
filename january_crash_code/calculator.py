def calculator():
    print("Welcome to the Python Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Get user input for operation
    operation = input("Enter the operation (1/2/3/4): ")
    
    if operation not in ["1", "2", "3", "4"]:
        print("Invalid operation. Please try again.")
        return calculator()
    
    try:
        # Get user input for numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return calculator()

    # Perform the selected operation
    if operation == "1":
        result = num1 + num2
        print(f"The result of addition: {num1} + {num2} = {result}")
    elif operation == "2":
        result = num1 - num2
        print(f"The result of subtraction: {num1} - {num2} = {result}")
    elif operation == "3":
        result = num1 * num2
        print(f"The result of multiplication: {num1} * {num2} = {result}")
    elif operation == "4":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of division: {num1} / {num2} = {result}")
    else:
        print("Something went wrong. Please try again.")

    # Ask if the user wants to perform another calculation
    another = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if another == "yes":
        calculator()
    else:
        print("Thank you for using the calculator! Goodbye.")

# Run the calculator
calculator()
