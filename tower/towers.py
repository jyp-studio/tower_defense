from tower.attack_strategy import *
import os
import pygame

RAPID_TEST_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "rapid_test.png")), (70, 70))
PCR_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "pcr.png")), (70, 70))
ALCOHOL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "alcohol.png")), (25, 70))
PLOT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "vacant_lot.png")), (20, 20))


class Vacancy:
    def __init__(self, x, y):
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
    def __init__(self, x: int, y: int, attack_strategy, image):
        self.image = image  # image of the tower
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the tower
        self.level = 0  # level of the tower
        self._range = [100, 110, 120, 130, 140, 150]  # tower attack range
        self._damage = [10, 20, 30, 40, 50, 60]   # tower damage
        self.cd_count = 0  # used in self.is_cool_down()
        self.cd_max_count = 60  # used in self.is_cool_down()
        self.attack_strategy = attack_strategy  # chose an attack strategy (AOE, single attack ....)
        self.value = [100, 140, 200, 300, 380, 460]

    @classmethod
    # moon_tower attacks all the enemies
    def moon_tower(cls, x, y):
        moon_tower = cls(x, y, SingleSlowAttack(), RAPID_TEST_IMAGE)
        moon_tower._range = [130, 140, 150, 160, 170, 180]
        moon_tower._damage = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5]
        moon_tower.value = [100, 140, 200, 280, 360, 450]
        return moon_tower

    @classmethod
    # red_fire_tower attacks and inflicts continuous damages on an enemy
    def red_fire_tower(cls, x, y):
        red_fire_tower = cls(x, y, AOE(), ALCOHOL_IMAGE)
        red_fire_tower._range = [120, 125, 130, 135, 140, 145]
        red_fire_tower._damage = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
        red_fire_tower.value = [120, 160, 220, 320, 400, 500]
        return red_fire_tower

    @classmethod
    # blue_fire_tower attacks and slows down enemies
    def blue_fire_tower(cls, x, y):
        blue_fire_tower = cls(x, y, AOE(), ALCOHOL_IMAGE)
        blue_fire_tower._range = [120, 125, 130, 135, 140, 145]
        blue_fire_tower._damage = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
        blue_fire_tower.value = [120, 160, 220, 320, 400, 500]
        return blue_fire_tower

    @classmethod
    # obelisk_tower attacks an enemy far away
    def obelisk_tower(cls, x, y):
        obelisk_tower = cls(x, y, SnipeAll(), PCR_IMAGE)
        obelisk_tower._range = [100, 105, 110, 115, 120, 125]  # tower attack range
        obelisk_tower.cd_max_count = 120  # tower damage
        obelisk_tower.value = [120, 140, 200, 280, 360, 400]
        return obelisk_tower

    def attack(self, enemy_group: list):
        # cd
        if self.cd_count < self.cd_max_count:
            self.cd_count += 1
            return
        # syntax: attack_strategy().attack(tower, enemy_group, cd_count)
        # It's something like you hire a "Strategist" to decide how to attack the enemy
        # You can add other ways of attack just by expanding the "attack_strategy.py"
        self.cd_count = self.attack_strategy.attack(enemy_group, self, self.cd_count)

    def get_upgrade_cost(self):
        return self.value[self.level+1] - self.value[self.level]

    def get_cost(self):
        return self.value[self.level]

    @property
    def range(self):
        return self._range[self.level]

    @property
    def damage(self):
        return self._damage[self.level]

    def clicked(self, x: int, y: int) -> bool:
        """
        :param x: mouse pos x
        :param y: mouse pos y
        :return: bool
        """
        return True if self.rect.collidepoint(x, y) else False





