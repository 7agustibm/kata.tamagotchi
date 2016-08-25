import unittest2 as unittest

from tamagochi.tamagochi import Tamagotchi

class MyTestCase(unittest.TestCase):
    def test_hungriness_default_is_5(self):
        tamagochi = Tamagotchi()
        self.assertEqual(5, tamagochi.hungriness)

    def test_fullness_default_is_5(self):
        tamagochi = Tamagotchi()
        self.assertEqual(5, tamagochi.fullness)

    def test_tamagochi_eat_update_state(self):
        tamagochi = Tamagotchi()
        tamagochi.eat()
        self.assertEqual(4, tamagochi.hungriness)
        self.assertEqual(6, tamagochi.fullness)

    def test_tamagochi_play_update_state(self):
        tamagochi = Tamagotchi()
        tamagochi.play()
        self.assertEqual(6, tamagochi.happiness)
        self.assertEqual(6, tamagochi.tiredness)

    def test_tamagochi_toBed_update_state(self):
        tamagochi = Tamagotchi()
        tamagochi.toBed()
        self.assertEqual(4, tamagochi.tiredness)

    def test_tamagochi_poop_update_state(self):
        tamagochi = Tamagotchi()
        tamagochi.poop()
        self.assertEqual(4, tamagochi.fullness)

    def test_tamagochi_time_passes_update_state(self):
        tamagochi = Tamagotchi()
        tamagochi.timePasses()
        self.assertEqual(6, tamagochi.hungriness)
        self.assertEqual(6, tamagochi.tiredness)
        self.assertEqual(4, tamagochi.happiness)

if __name__ == '__main__':
    unittest.main()
