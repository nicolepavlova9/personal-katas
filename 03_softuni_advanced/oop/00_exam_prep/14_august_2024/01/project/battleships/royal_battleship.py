from project.battleships.base_battleship import BaseBattleship


class RoyalBattleship(BaseBattleship):

    type = "Royal"

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, 100)

    def attack(self):
        self.ammunition -= 25
        if self.ammunition < 0:
            self.ammunition = 0