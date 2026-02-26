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
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def verify_password(password: str) -> bool:
    if not os.path.exists(VERIFY_FILE):
        salt = os.urandom(16)
        token = Fernet(derive_key(password, salt)).encrypt(b"OK")
        with open(VERIFY_FILE, 'wb') as f:
            f.write(salt + token)
        return True
    with open(VERIFY_FILE, 'rb') as f:
        salt = f.read(16)
        token = f.read()
    try:
        Fernet(derive_key(password, salt)).decrypt(token)
        return True
    except InvalidToken:
        return False
    def save_metadata(metadata: dict, password: str):
    salt = os.urandom(16)
    data = Fernet(derive_key(password, salt)).encrypt(json.dumps(metadata).encode())
    with open(METADATA_FILE, 'wb') as f:
        f.write(salt + data)
