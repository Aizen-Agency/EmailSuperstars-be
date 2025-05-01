from cryptography.fernet import Fernet
import os

# Ideally, store this key securely (e.g., in environment variables)
FERNET_KEY = os.getenv("FERNET_KEY")
fernet = Fernet(FERNET_KEY)

def decrypt_data(token: str) -> dict:
    decrypted_bytes = fernet.decrypt(token.encode())
    decrypted_str = decrypted_bytes.decode()
    import json
    return json.loads(decrypted_str)

def encrypt_data(data: dict) -> str:
    import json
    plaintext = json.dumps(data).encode()
    return fernet.encrypt(plaintext).decode()
