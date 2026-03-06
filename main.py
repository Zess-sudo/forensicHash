import hashlib
import os
import sys
import time

# Ask the user for the file path
file_path = input("Enter the file path: ")
# Check if the file exists
try:
    #Create a SHA256 hash object
    sha256_hash = hashlib.sha256()
    #Open the file in binary mode
    with open(file_path, "rb") as f:
        #Read the file in chunks to avoid memory issues
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    #Print the SHA256 hash
    print("SHA256:", sha256_hash.hexdigest())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("An error occurred:", str(e))
    sys.exit(1)