import os

# Specify the directory path
directory_path = '/4th Semester'

try:
    # Get the list of entries in the directory
    contents = os.listdir(directory_path)  # This is the function that lists directory contents
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Error: Insufficient permissions to access '{directory_path}'.")
