import unittest

from player import Player

class TestJump(unittest.TestCase):
	def setUp(self):
		pass	
	
	def test_jumping(self):
		player=Player((100,100))
		player.jump()
		self.assertEqual(player.jump_height,-18)
