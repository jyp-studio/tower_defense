from __future__ import annotations
from tower.towers import *
from gif import *
from tower.towers import Tower


class Lightning:
    def __init__(self, x: int, y: int):
        self.sprites = []
        self.current_sprites = 0
        self.max_current_sprites = 8
        self.update_speed = 0.8
        self.sprites.append(LIGHT_0)
        self.sprites.append(LIGHT_1)
        self.sprites.append(LIGHT_2)
        self.sprites.append(LIGHT_3)
        self.sprites.append(LIGHT_4)
        self.sprites.append(LIGHT_5)
        self.sprites.append(LIGHT_6)
        self.sprites.append(LIGHT_7)
        self.sprites.append(LIGHT_8)
        self.image = self.sprites[self.current_sprites]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.current_sprites += self.update_speed
        if self.current_sprites >= self.max_current_sprites:
            self.current_sprites = 0
        self.image = self.sprites[int(self.current_sprites)]


class ObeliskTower(Tower):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, Snipe())
        self.name = "Obelisk Tower"
        self.intro = "The obelisk from the underground of ancient Egypt "
        self.intro1 = "has the awesome power of annihilating the enemy with "
        self.intro2 = "one strike by falling terrifying lightning."
        self.attack_strategy_name = "Snipe"
        self.sprites = []
        self.max_current_sprites = 13
        self.update_speed = 0.25
        self.sprites.append(OBELISK_IMAGE_0)
        self.sprites.append(OBELISK_IMAGE_1)
        self.sprites.append(OBELISK_IMAGE_2)
        self.sprites.append(OBELISK_IMAGE_3)
        self.sprites.append(OBELISK_IMAGE_4)
        self.sprites.append(OBELISK_IMAGE_5)
        self.sprites.append(OBELISK_IMAGE_6)
        self.sprites.append(OBELISK_IMAGE_7)
        self.sprites.append(OBELISK_IMAGE_8)
        self.sprites.append(OBELISK_IMAGE_9)
        self.sprites.append(OBELISK_IMAGE_10)
        self.sprites.append(OBELISK_IMAGE_11)
        self.sprites.append(OBELISK_IMAGE_12)
        self.sprites.append(OBELISK_IMAGE_13)

        self._range = [120, 140, 150, 160, 170, 180, 280]  # tower attack range
        self._damage = [20, 40, 60, 80, 120, 160, 400] # tower damage
        self.cd_max_count = 120
        self.value = [1000, 2000, 3000, 4000, 5000, 6000, 20000]

    def throw(self, x: int, y: int):
        self.particle_list.append(Lightning(x, y))


