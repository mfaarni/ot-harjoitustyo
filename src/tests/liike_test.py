import unittest
from player import Player
from levels import Level
from controls import Controls
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, level_map


class TestMoving(unittest.TestCase):
    def setUp(self):
        self.controls = Controls()

    def test_jumping(self):
        input = self.controls.jump_control()
        self.assertEqual(input, self.controls.jump_height)

    def test_jumping_fail(self):
        self.controls.jump_count = 1
        input = self.controls.jump_control()
        self.assertEqual(input, 0)

    def test_walk_left(self):
        input = self.controls.keypress("left")
        self.assertEqual(input, -1)

    def test_walk_right(self):
        input = self.controls.keypress("right")
        self.assertEqual(input, 1)

    def test_fall_to_death(self):
        pass
