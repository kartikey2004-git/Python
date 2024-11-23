
import os

# Function to print contents of a directory
def print_directory_contents(path):
    try:
        # List the files and directories in the given path
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")

# Provide the directory path (you can change this path)
directory_path = "/Windows"
print_directory_contents(directory_path)

