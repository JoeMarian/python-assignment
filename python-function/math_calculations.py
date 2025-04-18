import math

def calculate_math_functions():
    try:
        # Get input from user
        number = float(input("Enter a positive number: "))
        
        # Validate input
        if number <= 0:
            print("Please enter a positive number.")
            return
            
        # Calculate mathematical functions
        square_root = math.sqrt(number)
        natural_log = math.log(number)
        sine = math.sin(number)
        
        # Display results
        print("\nResults:")
        print(f"Square root of {number}: {square_root:.4f}")
        print(f"Natural logarithm of {number}: {natural_log:.4f}")
        print(f"Sine of {number} radians: {sine:.4f}")
        
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    print("Welcome to Math Calculator!")
    calculate_math_functions()