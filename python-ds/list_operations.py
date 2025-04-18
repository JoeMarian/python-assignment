def demonstrate_list_slicing():
    # Create list of numbers 1 to 10
    numbers = list(range(1, 11))
    print("Original list:", numbers)
    
    # Extract first five elements
    first_five = numbers[:5]
    print("\nFirst five elements:", first_five)
    
    # Reverse the extracted elements
    reversed_five = first_five[::-1]
    print("Reversed first five elements:", reversed_five)
    
    # Additional demonstrations
    print("\nAdditional slicing examples:")
    print("Last five elements:", numbers[-5:])
    print("Every second element:", numbers[::2])
    print("Original list in reverse:", numbers[::-1])

if __name__ == "__main__":
    print("List Slicing Demonstration")
    demonstrate_list_slicing()