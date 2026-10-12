import os
import sys

print("Python Version:", sys.version)
print("Operating System Platform:", sys.platform)

current_dir = os.getcwd()
print("Current Directory:", current_dir)

new_folder = "test_folder"
if not os.path.exists(new_folder):
    os.mkdir(new_folder)
    print(f"Directory '{new_folder}' created successfully.")
else:
    print(f"Directory '{new_folder}' already exists.")

print("Contents of current directory:")
print(os.listdir("."))
