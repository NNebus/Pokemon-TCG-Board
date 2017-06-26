class Pokemon:

    damage_coins:int = 0

    def increase_damage(self):
        self.damage_coins += 1

    def decrase_damage(self):
        self.damage_coins -= 1
