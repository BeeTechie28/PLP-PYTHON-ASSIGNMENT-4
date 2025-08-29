# Python File Handling Challenges 🐍📂

Welcome to the **Python File Handling Challenges** repository!  
This repository contains beginner-to-intermediate Python programs designed to help you practice **file reading, writing, and error handling** in a structured way.

---

## 📁 Projects Included

### 1. File Read & Write Challenge 🖋️
**Objective:**  
Create a program that reads a file and writes a modified version to a new file.  

**Features:**  
- Reads content from an existing text file.  
- Modifies the content (e.g., converts text to uppercase, replaces words, or formats text).  
- Writes the modified content to a new file.  
- Ensures the original file remains unchanged.  

**Example Usage:**
```python
# Read content from the original file
with open("original.txt", "r") as infile:
    content = infile.read()

# Modify the content
modified_content = content.upper()  # Converts all text to uppercase

# Write modified content to a new file
with open("modified.txt", "w") as outfile:
    outfile.write(modified_content)

## 2. Error Handling Lab 🧪

**Objective:**  
Ask the user for a filename and handle errors if the file does not exist or cannot be read.

**Features:**  
- Prompts the user to enter a filename.  
- Uses `try-except` blocks to catch errors like `FileNotFoundError` or `IOError`.  
- Provides informative error messages to guide the user.  
- Ensures the program doesn’t crash if the file is missing or unreadable.  

**Example Usage:**
```python
filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again.")
except IOError:
    print("Error: Cannot read the file. Please check permissions.")

### 🚀 How to Run
1. Clone the repository:  
```bash
git clone https://github.com/BeeTechie28/PLP-PYTHON-ASSIGNMENT-4.git

🛠️ Skills Practiced

File reading and writing (open, read, write)

String manipulation

Writing modular, reusable Python code

🤝 Contribution

Contributions are welcome! If you have ideas to enhance these exercises or want to add new file handling challenges, feel free to submit a pull request.
