def read_and_write_file(input_file, output_file):
    try:
        # Open the input file and read its content
        with open(input_file, 'r') as file:
            content = file.read()

        # Modify the content (e.g., converting text to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"Content from {input_file} has been modified and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
read_and_write_file('input.txt', 'output.txt')
