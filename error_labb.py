def handle_file_error():
    filename = input("Enter the filename: ")

    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print("File content read successfully!")
            print(content)

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
handle_file_error()
