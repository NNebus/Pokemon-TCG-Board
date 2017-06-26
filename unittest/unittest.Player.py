import unittest
from player import Player


class TestPlayerClass(object):

    def test_instantiate_empty(self):
        player = Player()
        self.assertTrue(isinstance(player.__getattribute__('_pokemon')), Player)
