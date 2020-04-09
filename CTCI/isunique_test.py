
import unittest
from isunique import is_unique


class TestIsUnique(unittest.TestCase):
    def test_dup_character(self):
        self.assertFalse(is_unique("zeftta"))

    def test_dup_start_character(self):
        self.assertFalse(is_unique("zzefta"))

    def test_dup_end_character(self):
        self.assertFalse(is_unique("zeftaa"))

    def test_unique(self):
        self.assertTrue(is_unique("zefta"))

    def test_empty_string(self):
        self.assertTrue(is_unique(""))


if __name__ == '__main__':
    unittest.main()
