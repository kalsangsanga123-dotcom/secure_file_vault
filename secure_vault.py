import os
import json
import shutil
from tkinter import *
from tkinter import filedialog, messagebox, simpledialog
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64

# ===== CORE SECURITY SETUP =====
VAULT_DIR = ".secure_vault"
METADATA_FILE = os.path.join(VAULT_DIR, "vault.dat")  # Encrypted metadata
VERIFY_FILE = os.path.join(VAULT_DIR, ".verify")      # Password verification
os.makedirs(VAULT_DIR, exist_ok=True)