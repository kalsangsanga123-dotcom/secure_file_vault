import os
import json
import base64
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

    vault_path = os.path.join(VAULT_DIR, meta[filename]["vault_path"])
    with open(vault_path, 'rb') as f:
        salt = f.read(16)
        encrypted = f.read()
    
    try:
        data = Fernet(derive_key(password, salt)).decrypt(encrypted)
    except InvalidToken:
        raise ValueError("Wrong password or corrupted file!")
    
    with open(output_path, 'wb') as f:
        f.write(data)