# SecureVault

## Overview
A lightweight, Tkinter-based Python application designed to encrypt and manage sensitive files within a secure local directory. It provides a user-friendly interface for password-protected file storage and retrieval.

## Learning Objectives
- Learning cryptography encryption and decryption.
- Understanding GUI updates from user events.
- Applying secure authentication and protect sensitive data.
- Managing secure file handling and auto-generate filenames

## Key Features
- AES-256 Encryption.
- Dynamic UI States.
- Metadata Management.
- Secure Retrieval.
- Automated Cleanup.

## Project Structure
secure-vault-project/
├── .secure_vault/          # (HIDDEN) Local storage for encrypted files
│   ├── .verify             # Password verification token
│   ├── vault.dat           # Encrypted metadata manifest
│   └── example.txt.enc     # Encrypted file blobs
├── .gitignore              # Instructions for Git to ignore sensitive data
├── gui.py                  # Tkinter interface and UI logic
├── main.py                 # Application entry point
├── README.md               # Project documentation
├── requirements.txt        # List of Python dependencies
├── test.py                 # Automated unit tests
└── vault_logic.py          # Core cryptographic engine

# Installation

## Prerequisites
- Python 3.8+
- Windows, macOS or Linux

## Quick Start
```bash
#clone the repo
git clone https://github.com/kalsangsanga123-dotcom/secure_file_vault.git
cd secure-vault

#install requirement libarires and modules.
pip install -r requirement.txt

#run the application
python3 main.py
```

**Expected Output**

![image alt](https://github.com/kalsangsanga123-dotcom/secure_file_vault/blob/d8d0303575812c3bc467b6feeeb092bbf4d982e3/Screenshot%202026-02-27%20161502.png)


## Application testing
```bash
python3 test.secure_vault.py
```
## License
This project is open source and available for educational purpose.

## Author
- **Kalsang Sangay Lama**
