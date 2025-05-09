import unittest
from app.qkd_simulator import simulate_qkd

class TestQKD(unittest.TestCase):
    def test_key_generation_length(self):
        key = simulate_qkd()
        self.assertGreaterEqual(len(key), 30)  # Pastikan panjang minimal key

if __name__ == '__main__':
    unittest.main()
