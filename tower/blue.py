from __future__ import annotations
from tower.towers import *
from gif import *


class BlueFireTower(Tower):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, AOESlowAttack())
        self.name = "Ice Totem"
        self.intro = "Black magic wizards sacrifice hundreds of thousands of "
        self.intro1 = "virus-infected mutants to summon ice totems "
        self.intro2 = "in the endless abyss"
        self.attack_strategy_name = "AOE Slow Attack"
        self.sprites = []
        self.update_speed = 0.2
        self.max_current_sprites = 6
        self.sprites.append(BLUE_IMAGE_0)
        self.sprites.append(BLUE_IMAGE_1)
        self.sprites.append(BLUE_IMAGE_2)
        self.sprites.append(BLUE_IMAGE_3)
        self.sprites.append(BLUE_IMAGE_4)
        self.sprites.append(BLUE_IMAGE_5)
        self.sprites.append(BLUE_IMAGE_6)

        self._range = [120, 125, 130, 135, 140, 145, 280]
        self._damage = [10, 15, 19, 25, 30, 37, 60]
        self.value = [150, 200, 250, 300, 400, 500, 10000]







