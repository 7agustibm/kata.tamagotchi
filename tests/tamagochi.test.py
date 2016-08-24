import unittest2 as unittest

from tamagochi.tamagochi import Tamagotchi

class MyTestCase(unittest.TestCase):
    def test_hungriness_default_is_5(self):
        tamagochi = Tamagotchi()
        self.assertEqual(5, tamagochi.hungriness)

    def test_fullness_default_is_5(self):
        tamagochi = Tamagotchi()
        self.assertEqual(5, tamagochi.fullness)


if __name__ == '__main__':
    unittest.main()
