import unittest
from levels_2 import Level
from settings import SCREEN_WIDTH


class Test_levels(unittest.TestCase):
    def setUp(self):
        self.level = Level("testi")

    def test_scroll_x_left(self):
        self.level.scroll_x(-100, -1)
        self.assertEqual(self.level.world_shift, 6)

    def test_scroll_x_right(self):
        self.level.scroll_x(1200, 1)
        self.assertEqual(self.level.world_shift, -6)

    def test_scroll_x_left_speed(self):
        self.level.scroll_x(-100, -1)
        self.assertEqual(self.level.controls.speed, 0)

    def test_scroll_x_right_speed(self):
        self.level.scroll_x(1200, 1)
        self.assertEqual(self.level.controls.speed, 0)
