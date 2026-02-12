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
def derive_key(password: str, salt: bytes) -> bytes:
    """Convert password to encryption key using PBKDF2"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))
def verify_password(password: str) -> bool:
    """Check password without decrypting files (critical UX/security feature)"""
    if not os.path.exists(VERIFY_FILE):
          # First-time setup: create verification token
        salt = os.urandom(16)
        token = Fernet(derive_key(password, salt)).encrypt(b"OK")
        with open(VERIFY_FILE, 'wb') as f:
            f.write(salt + token)
        return True
        # Verify existing password
    with open(VERIFY_FILE, 'rb') as f:
        salt = f.read(16)
        token = f.read()
    try:
        Fernet(derive_key(password, salt)).decrypt(token)
        return True
    except InvalidToken:
        return False
def save_metadata(metadata: dict, password: str):
     """Encrypt metadata (filenames/sizes) to prevent leakage"""
     salt = os.urandom(16)
     data = Fernet(derive_key(password, salt)).encrypt(json.dumps(metadata).encode())
     with open(METADATA_FILE, 'wb') as f:
        f.write(salt + data)  # Store salt + encrypted data