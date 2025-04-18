def create_greeting():
    # Get user input
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    # Concatenate names
    full_name = f"{first_name} {last_name}"
    
    # Create and display greeting
    greeting = f"\nHello, {full_name}! Welcome to our program."
    print(greeting)

if __name__ == "__main__":
    print("Welcome to the Greeting Program!")
    create_greeting()