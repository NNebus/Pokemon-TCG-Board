from .pokemon import Pokemon


class Player(object):
    _pokemon: Pokemon = []

    def __init__(self, pokemon: Pokemon = None, active=None):
        if pokemon is None:
            self._pokemon: Pokemon = []
        else:
            self._pokemon = pokemon
        self.active = None

    def __delitem__(self, key: int):
        del (self._pokemon, key)
        if self.active == key:
            self.active = None

    def append(self, item: Pokemon):
        self._pokemon.extend(item)

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)
