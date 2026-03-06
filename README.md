# FORENSICHASH
File Hashing Utility for Digital Forensics

## Table of Contents
- [Purpose](#purpose)
- [Features](#features)
- [Contents](#contents)
- [Usage](#usage)
- [Academic Statement](#academic-statement)

### Purpose
This project demonstrates the use of cryptographic hashing algorithms for verifying file integrity in a digital forensics context. Hash values act as digital fingerprints of files, allowing investigators to confirm that evidence has not been altered during acquisition, analysis, or transfer.

The program allows a user to select a file and generate a hash using commonly used forensic algorithms such as SHA256, SHA512, and MD5. The tool is designed as a simple command-line utility to illustrate how hashing works and how it supports evidence integrity verification.

### Features
- Supports multiple hashing algorithms:
  - SHA256
  - SHA512
  - MD5
- Reads files in memory-safe chunks to support large files
- Interactive command-line interface
- Input validation for algorithm selection
- Allows repeated hashing operations without restarting the program

### Contents
- 'main.py': Main Python script that performs the hashing operations.
- 'README.md': Project description and documentation.

### Pre-requisites
- Python 3.x installed on the system.

The program uses only Python's built-in standard libraries:
- hashlib
- sys

No third-party packages are required.

### Usage
Run the program from the command line:

python main.py

The program will prompt the user to:
1. Enter the file path
2. Select a hashing algorithm
3. Display the resulting hash value

The user may then choose to hash another file or exit the program.

### Future Improvements (Possible for larger projects)
- Add hash verification mode
- Add graphical user interface
- Support hashing entire directories
- Export hash results to a report file

### Academic Statement
This project was developed as part of coursework for a digital forensics course. It is intended solely for educational and demonstration purposes. The tool demonstrates fundamental concepts of cryptographic hashing and file integrity verification used in digital forensic investigations.