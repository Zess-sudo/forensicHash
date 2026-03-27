import hashlib
import sys
#Choose a Hashing Algorithm
def get_hash_object(choice):
    if choice == "1":
        return hashlib.sha256(), "SHA256"
    elif choice == "2":
        return hashlib.sha512(), "SHA512"
    elif choice == "3":
        return hashlib.md5(), "MD5"
    else:
        return None, None

while True:
    # Ask the user for the file path
    file_path = input("Enter the file path: ")

    while True:
        # Ask the user to choose a hashing algorithm
        print("\nSelect a hashing algorithm:")
        print("1. SHA256")
        print("2. SHA512")
        print("3. MD5")
        choice = input("Enter your choice (1/2/3): ")
        hash_obj, hash_name = get_hash_object(choice)
        if hash_obj is None:
            print("Invalid choice. Please select a valid hashing algorithm (1/2/3).")
        else:
            break

    try:
        # Create a hash object based on the user's choice
        with open(file_path, "rb") as f:
            # Read the file in chunks to avoid memory issues
            for byte_block in iter(lambda: f.read(4096), b""):
                hash_obj.update(byte_block)
        # Print the hash
        print(f"{hash_name.upper()}:", hash_obj.hexdigest())
        #ask the user if they want to hash another file
        save = input("\nDo you want to save the hash to a file? (y/n): ").lower()
        if save == "y":
            #create a file name based on user input to desktop
            output_file = input("Enter the output file name (without extension): ")
            output_path = f"{output_file}.txt"
            try:
                with open(output_path, "w") as f:
                    f.write(f"{hash_name.upper()}: {hash_obj.hexdigest()}\n")
                print(f"Hash saved to {output_path}")
            except Exception as e:
                print("An error occurred while saving the file:", str(e))
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print("An error occurred:", str(e))
    #Ask the user if they want to run the program again
    again = input("\nDo you want to hash another file? (y/n): ").lower()
    if again != "y":
    # close the program    
        print("Thank you for using the file hashing tool.")
        sys.exit(0)