def perform_math_operations():
    # Get input from user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Perform operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    
    # Handle division by zero
    try:
        division = num1 / num2
        division_result = f"Division: {num1} / {num2} = {division}"
    except ZeroDivisionError:
        division_result = "Division: Cannot divide by zero"
    
    # Display results
    print("\nResults:")
    print(f"Addition: {num1} + {num2} = {addition}")
    print(f"Subtraction: {num1} - {num2} = {subtraction}")
    print(f"Multiplication: {num1} * {num2} = {multiplication}")
    print(division_result)

if __name__ == "__main__":
    print("Welcome to Basic Calculator!")
    perform_math_operations()