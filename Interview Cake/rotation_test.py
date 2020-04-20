import rotation
import unittest


class RotationTest(unittest.TestCase):
    def test_rotation_at_middle(self):
        words = [
            'ptolemaic',
            'retrograde',
            'supplant',
            'undulate',
            'xenoepist',
            'asymptote',  # <-- rotates here!
            'babka',
            'banoffee',
            'engender',
            'karpatka',
            'othellolagkage'
        ]
        self.assertEqual(5, rotation.get_rotation_point(words))

    def test_rotation_at_start(self):
        words = [
            'xenoepist',
            'asymptote',  # <-- rotates here!
            'babka',
            'banoffee',
            'engender',
            'karpatka',
            'othellolagkage',
            'ptolemaic',
            'retrograde',
            'supplant',
            'undulate'
        ]
        self.assertEqual(1, rotation.get_rotation_point(words))

    def test_rotation_at_end(self):
        words = [
            'babka',
            'banoffee',
            'engender',
            'karpatka',
            'othellolagkage',
            'ptolemaic',
            'retrograde',
            'supplant',
            'undulate',
            'xenoepist',
            'asymptote',  # <-- rotates here!
        ]
        self.assertEqual(len(words) - 1, rotation.get_rotation_point(words))

    def test_no_rotation(self):
        words = [
            'asymptote',  # <-- no rotation, expected to return 0
            'babka',
            'banoffee',
            'engender',
            'karpatka',
            'othellolagkage'
            'ptolemaic',
            'retrograde',
            'supplant',
            'undulate',
            'xenoepist'
        ]
        self.assertEqual(0, rotation.get_rotation_point(words))

    def test_words_start_at_e(self):
        words = [
            'ptolemaic',
            'retrograde',
            'supplant',
            'undulate',
            'xenoepist',
            'engender',
            'karpatka',
            'othellolagkage'
        ]
        self.assertEqual(5, rotation.get_rotation_point(words))

    # TODO: figure out how to assert expected error
    # def test_single_word_list(self):
    #     words = ["test"]
    #     self.assertRaises (
    #         ValueError,
    #         rotation.get_rotation_point(words))

    def test_two_word_list(self):
        words = ["undulate", "engender"]
        self.assertEqual(1, rotation.get_rotation_point(words))


if __name__ == '__main__':
    unittest.main()
