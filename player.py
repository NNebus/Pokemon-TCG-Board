class Player:
    def __init__(self, pokemon=None, active=None):
        if pokemon is None:
            pokemon = []
        else:
            pokemon = pokemon
        self.pokemon = pokemon
        self.active = None

    def __delitem__(self, key: int):
        del(self.pokemon, key)
        if self.active == key:
            self.active = None

    def append(self, item):
        self.pokemon.append(item)