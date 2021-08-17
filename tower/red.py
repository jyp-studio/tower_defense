from __future__ import annotations
from tower.towers import *
from gif import *
from tower.towers import Tower


class Flame:
    def __init__(self, x: int, y: int):
        self.sprites = []
        self.current_sprites = 0
        self.max_current_sprites = 9
        self.update_speed = 0.8
        self.sprites.append(FLAME_0)
        self.sprites.append(FLAME_1)
        self.sprites.append(FLAME_2)
        self.sprites.append(FLAME_3)
        self.sprites.append(FLAME_4)
        self.sprites.append(FLAME_5)
        self.sprites.append(FLAME_6)
        self.sprites.append(FLAME_7)
        self.sprites.append(FLAME_8)
        self.sprites.append(FLAME_9)
        self.image = self.sprites[self.current_sprites]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.current_sprites += self.update_speed
        if self.current_sprites >= self.max_current_sprites:
            self.current_sprites = 0
        self.image = self.sprites[int(self.current_sprites)]


class RedFireTower(Tower):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, RedAttack())
        self.name = "Fire Totem"
        self.intro = "The shaman with white magic devoted his heart "
        self.intro1 = "to the flame totem to make it alive"
        self.intro2 = "and defend the survival of mankind"
        self.attack_strategy_name = "Single Fast"
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

        self.cd_max_count = 15
        self._range = [120, 125, 130, 135, 140, 145, 250]
        self._damage = [10, 20, 40, 80, 300, 700, 1500]
        self.value = [250, 300, 350, 410, 480, 560, 2500]

    def throw(self, x: int, y: int):
        self.particle_list.append(Flame(x, y - 90))





