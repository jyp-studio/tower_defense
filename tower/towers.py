from __future__ import annotations
from tower.attack_strategy import *
from gif import *
import os
import pygame


class Vacancy:
    def __init__(self, x:int, y: int):
        self.image = PLOT_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x: int, y: int) -> bool:
        """
        :param x: mouse pos x
        :param y: mouse pos y
        :return: bool
        """
        return True if self.rect.collidepoint(x, y) else False


# tower (product)
class Tower:
    """ super class of towers """
    def __init__(self, x: int, y: int, attack_strategy: AttackStrategy):
        """
        self.sprites: list for animation
        self.current_sprites: counter for each image
        self.max_current_sprites: total image
        self.update_speed: count speed
        self.sprites.append(OBELISK_IMAGE_0): append first image
        """
        self.sprites = []
        self.current_sprites = 0
        self.max_current_sprites = 10
        self.update_speed = 1
        self.sprites.append(OBELISK_IMAGE_0)
        self.image = self.sprites[self.current_sprites]  # image of the tower
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the tower
        self.name = ""
        self.intro = ""
        self.intro1 = ""
        self.intro2 = ""

        self.level = 0  # level of the tower
        self._range = [100, 110, 120, 130, 140, 150, 300]  # tower attack range
        self._damage = [10, 20, 30, 40, 50, 60, 100]   # tower damage
        self.cd_count = 0  # used in self.is_cool_down()
        self.cd_max_count = 60  # used in self.is_cool_down()
        self.animate_count = 0
        self.attack_strategy = attack_strategy  # chose an attack strategy (AOE, single attack ....)
        self.attack_strategy_name = ""
        self.value = [100, 140, 200, 300, 380, 460, 10000]

        # bullet list
        self.particle_list = []

    def update(self):
        self.current_sprites += self.update_speed
        if self.current_sprites >= self.max_current_sprites:
            self.current_sprites = 0
        self.image = self.sprites[int(self.current_sprites)]

    def attack(self, enemy_group: list):
        # cd
        if self.cd_count < self.cd_max_count:
            self.cd_count += 1
        
        # syntax: attack_strategy().attack(tower, enemy_group, cd_count)
        # It's something like you hire a "Strategist" to decide how to attack the enemy
        # You can add other ways of attack just by expanding the "attack_strategy.py"

        self.cd_count = self.attack_strategy.attack(enemy_group, self, self.cd_count)

    def throw(self, x: int, y: int):
        pass

    def get_upgrade_cost(self) -> int:
        return self.value[self.level+1]

    def get_ultra_cost(self) -> int:
        return self.value[6]

    def get_cost(self) -> int:
        return self.value[self.level]

    def get_sell_price(self) -> int:
        return int(self.value[self.level] / 2)

    @property
    def range(self) -> int:
        return self._range[self.level]

    @property
    def damage(self) -> int:
        return self._damage[self.level]

    def clicked(self, x: int, y: int) -> bool:
        """
        :param x: mouse pos x
        :param y: mouse pos y
        :return: bool
        """
        return True if self.rect.collidepoint(x, y) else False





