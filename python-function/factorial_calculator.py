def factorial(n):
    # Base case for factorial
    if n == 0 or n == 1:
        return 1
    
    # Calculate factorial using recursion
    return n * factorial(n - 1)

def main():
    try:
        # Get input from user
        number = int(input("Enter a number to calculate its factorial: "))
        
        # Validate input
        if number < 0:
            print("Factorial cannot be calculated for negative numbers.")
            return
            
        # Calculate and display result
        result = factorial(number)
        print(f"\nThe factorial of {number} is: {result}")
        
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()