import os
import shutil

with open("source.txt", "w") as f:
    f.write("Hello, World!")
print("Sample file 'source.txt' created.")

shutil.copy("source.txt", "backup.txt")
print("File copied successfully to 'backup.txt'")

shutil.move("backup.txt", "destination.txt")
print("File moved/renamed successfully to 'destination.txt'")

os.remove("source.txt")
os.remove("destination.txt")
print("Files cleaned up and deleted successfully.")
