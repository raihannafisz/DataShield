# Modul enkripsi AES untuk data simulasi
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt_message(message: str, key: bytes):
    cipher = AES.new(key[:16], AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ct_bytes).decode()

def decrypt_message(ciphertext: str, key: bytes):
    raw = base64.b64decode(ciphertext)
    cipher = AES.new(key[:16], AES.MODE_CBC, iv=raw[:16])
    pt = unpad(cipher.decrypt(raw[16:]), AES.block_size)
    return pt.decode()