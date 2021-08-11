from __future__ import annotations
from tower.towers import *
from gif import *


class RedFireTower(Tower):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, AOE())
        self.name = "Fire Totem"
        self.intro = "The shaman with white magic devoted his heart "
        self.intro1 = "to the flame totem to make it alive"
        self.intro2 = "and defend the survival of mankind"
        self.attack_strategy_name = "AOE"
        self.sprites = []
        self.update_speed = 0.2
        self.max_current_sprites = 6
        self.sprites.append(RED_IMAGE_0)
        self.sprites.append(RED_IMAGE_1)
        self.sprites.append(RED_IMAGE_2)
        self.sprites.append(RED_IMAGE_3)
        self.sprites.append(RED_IMAGE_4)
        self.sprites.append(RED_IMAGE_5)
        self.sprites.append(RED_IMAGE_6)

        self._range = [120, 125, 130, 135, 140, 145, 250]
        self._damage = [8, 14, 18, 22, 25, 35, 50]
        self.value = [120, 160, 220, 320, 400, 500, 10000]





