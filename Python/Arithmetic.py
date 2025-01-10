# Define the calculator function
def calculator():
    print("Welcome to the calculator!")
    print("\nChoose an operation:")   # Display operation options
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Input choice
    while True:   # Loop until a valid choice is entered
        try:
            choice = int(input("Enter the number corresponding to your choice (1-4): "))
            if choice not in [1, 2, 3, 4]:
                print("Invalid choice. Please select a number between 1 and 4.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Input two numbers with validation
    while True:   # Loop until a valid number is entered for the first input
        try:
            num1 = float(input("\nEnter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    while True:   # Loop until a valid number is entered for the second input
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    # Perform the chosen operation
    print("\nResult:")
    if choice == 1:    # Check if the operation is addition
        print(f"{num1} + {num2} = {num1 + num2}")

    elif choice == 2:    # Check if the operation is subtraction
        print(f"{num1} - {num2} = {num1 - num2}")

    elif choice == 3:    # Check if the operation is multiplication
        print(f"{num1} * {num2} = {num1 * num2}")

    elif choice == 4:    # Check if the operation is division
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Division by zero is not allowed.")    # Display error for division by zero

# Define the main function
def main():
    while True:    # Loop for repeated calculations
        calculator()
        # Ask the user if they want to perform another calculation
        repeat = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if repeat not in ['yes', 'y']:
            print("Thank you for using the calculator!\n")
            break

# Entry point
if __name__ == "__main__":
    main()