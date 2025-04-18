def modify_content(text):
    #  converting content to uppercase
    return text.upper()

def read_and_modify_file():
    filename = input("Enter the filename to read from: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()  # Read the entire file
        
        modified_content = modify_content(content)  # Modify the content
        
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)  # Write modified content to new file
        
        print(f"Modified content written to '{new_filename}' successfully.")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Could not read or write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_modify_file()
