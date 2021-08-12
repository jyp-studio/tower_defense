from __future__ import annotations
from tower.towers import *
from gif import *


class Beam:
    def __init__(self, en_x: int, en_y: int, tw_x, tw_y):
        self.sprites = []
        self.current_sprites = 0
        self.max_current_sprites = 5
        self.update_speed = 0.8
        self.sprites.append(BEAM_0)
        self.sprites.append(BEAM_1)
        self.sprites.append(BEAM_2)
        self.sprites.append(BEAM_3)
        self.sprites.append(BEAM_4)
        self.sprites.append(BEAM_5)
        self.image = self.sprites[self.current_sprites]
        self.rect = self.image.get_rect()
        self.rect.center = (en_x, en_y)

    def update(self):
        self.current_sprites += self.update_speed
        if self.current_sprites >= self.max_current_sprites:
            self.current_sprites = 0
        self.image = self.sprites[int(self.current_sprites)]


class MoonTower(Tower):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, SingleSlowAttack())
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
        pass
        #self.particle_list.append(Beam(x, y))






