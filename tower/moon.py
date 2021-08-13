from __future__ import annotations
from tower.towers import *
from gif import *


class Magic:
    def __init__(self, x: int, y: int):
        self.sprites = []
        self.current_sprites = 0
        self.max_current_sprites = 10
        self.update_speed = 0.5
        self.sprites.append(MAGIC_0)
        self.sprites.append(MAGIC_1)
        self.sprites.append(MAGIC_0)
        self.sprites.append(MAGIC_1)
        self.sprites.append(MAGIC_0)
        self.sprites.append(MAGIC_1)
        self.sprites.append(MAGIC_0)
        self.sprites.append(MAGIC_1)
        self.sprites.append(MAGIC_0)
        self.sprites.append(MAGIC_1)

        self.image = self.sprites[self.current_sprites]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.current_sprites += self.update_speed
        if self.current_sprites >= self.max_current_sprites:
            self.current_sprites = 0
        self.image = self.sprites[int(self.current_sprites)]


class MoonTower(Tower):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, MoonAttack())
        self.name = "Moon Tower"
        self.intro = "The ruby that absorbs the essence of the sun and the "
        self.intro1 = "moon is carved into the shape of the moon and installed "
        self.intro2 = "on the tower to form an indestructible moon tower."
        self.attack_strategy_name = "Single Slow Attack"
        self.sprites = []
        self.update_speed = 0.2
        self.max_current_sprites = 9
        self.sprites.append(MOON_IMAGE_0)
        self.sprites.append(MOON_IMAGE_1)
        self.sprites.append(MOON_IMAGE_2)
        self.sprites.append(MOON_IMAGE_3)
        self.sprites.append(MOON_IMAGE_4)
        self.sprites.append(MOON_IMAGE_5)
        self.sprites.append(MOON_IMAGE_6)
        self.sprites.append(MOON_IMAGE_7)
        self.sprites.append(MOON_IMAGE_8)
        self.sprites.append(MOON_IMAGE_9)
        self._range = [140, 160, 180, 200, 220, 250, 350]
        self.value = [100, 140, 200, 280, 360, 450, 10000]

    def throw(self, x: int, y: int):
        self.particle_list.append(Magic(x, y + 100))






