def read_file(filename):
    try:
        print("Reading file content:")
        print("-" * 20)
        
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, 1):
                print(f"Line {line_number}: {line.strip()}")
                
        print("-" * 20)
        
    except FileNotFoundError:
        print("Error: no file")

if __name__ == "__main__":
    filename = "sample.txt"
    read_file(filename)