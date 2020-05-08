import unittest
from string_permutation import is_string_permutation


class TestStringPermutation(unittest.TestCase):
    def test_exact_string(self):
        self.assertTrue(is_string_permutation("football", "football"))

    def test_caps(self):
        self.assertFalse(is_string_permutation("football", "FOOTBALL"))

    def test_diff_len(self):
        self.assertFalse(is_string_permutation("foobar", "fooba"))

    def test_same(self):
        self.assertTrue(is_string_permutation("foobar", "foobar"))

    def test_permutation(self):
        self.assertTrue(
            is_string_permutation(
                "ThreeOneTwotest",
                "testOneTwoThree"))


if __name__ == '__main__':
    unittest.main()
