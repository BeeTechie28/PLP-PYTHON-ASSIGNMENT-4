filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again.")
except IOError:
    print("Error: Cannot read the file.")
