def write_and_append_file():
    filename = "output.txt"
    
    # Write initial content
    try:
        content = input("Enter text to write to file: ")
        with open(filename, 'w') as file:
            file.write(content + '\n')
        print("Content written successfully!")
        
        # Append additional content
        additional = input("Enter additional text to append: ")
        with open(filename, 'a') as file:
            file.write(additional + '\n')
        print("Content appended successfully!")
        
        # Read and display final content
        print("\nFinal content of the file:")
        print("-" * 20)
        with open(filename, 'r') as file:
            print(file.read())
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    write_and_append_file()