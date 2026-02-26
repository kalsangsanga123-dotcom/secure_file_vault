import os
import json
import base64
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

VAULT_DIR = ".secure_vault"
METADATA_FILE = os.path.join(VAULT_DIR, "vault.dat")
VERIFY_FILE = os.path.join(VAULT_DIR, ".verify")
os.makedirs(VAULT_DIR, exist_ok=True)

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )