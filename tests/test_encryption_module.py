import unittest
from app.encryption_module import encrypt_message, decrypt_message

class TestEncryption(unittest.TestCase):
    def test_encryption_decryption(self):
        key = bytes([0]*16)  # Kunci dummy
        message = "Tes Pesan"
        encrypted = encrypt_message(message, key)
        decrypted = decrypt_message(encrypted, key)
        self.assertEqual(message, decrypted)

if __name__ == '__main__':
    unittest.main()

