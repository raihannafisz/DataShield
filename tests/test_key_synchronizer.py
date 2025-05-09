import unittest
from app.key_synchronizer import synchronize_keys

class TestSynchronizer(unittest.TestCase):
    def test_sync_keys(self):
        a = [1, 0, 1, 1, 0]
        b = [1, 0, 1]
        synced_a, synced_b = synchronize_keys(a, b)
        self.assertEqual(synced_a, [1, 0, 1])
        self.assertEqual(synced_b, [1, 0, 1])

if __name__ == '__main__':
    unittest.main()
