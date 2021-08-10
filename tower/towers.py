from __future__ import annotations
from tower.attack_strategy import *
import os
import pygame

# obelisk image
OBELISK_IMAGE_0 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image0.png")), (150, 150))
OBELISK_IMAGE_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image1.png")), (150, 150))
OBELISK_IMAGE_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image2.png")), (150, 150))
OBELISK_IMAGE_3 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image3.png")), (150, 150))
OBELISK_IMAGE_4 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image4.png")), (150, 150))
OBELISK_IMAGE_5 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image5.png")), (150, 150))
OBELISK_IMAGE_6 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image6.png")), (150, 150))
OBELISK_IMAGE_7 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image7.png")), (150, 150))
OBELISK_IMAGE_8 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image8.png")), (150, 150))
OBELISK_IMAGE_9 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image9.png")), (150, 150))
OBELISK_IMAGE_10 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image10.png")), (150, 150))
OBELISK_IMAGE_11 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image11.png")), (150, 150))
OBELISK_IMAGE_12 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image12.png")), (150, 150))
OBELISK_IMAGE_13 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image13.png")), (150, 150))

# moon tower image
MOON_IMAGE_0 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image0.png")), (110, 110))
MOON_IMAGE_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image1.png")), (110, 110))
MOON_IMAGE_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image2.png")), (110, 110))
MOON_IMAGE_3 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image3.png")), (110, 110))
MOON_IMAGE_4 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image4.png")), (110, 110))
MOON_IMAGE_5 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image5.png")), (110, 110))
MOON_IMAGE_6 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image6.png")), (110, 110))
MOON_IMAGE_7 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image7.png")), (110, 110))
MOON_IMAGE_8 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image8.png")), (110, 110))
MOON_IMAGE_9 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image9.png")), (110, 110))

# red fire tower image
RED_IMAGE_0 = pygame.transform.scale(pygame.image.load(os.path.join("images", "red_image0.png")), (110, 110))
RED_IMAGE_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "red_image1.png")), (110, 110))
RED_IMAGE_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "red_image2.png")), (110, 110))
RED_IMAGE_3 = pygame.transform.scale(pygame.image.load(os.path.join("images", "red_image3.png")), (110, 110))
RED_IMAGE_4 = pygame.transform.scale(pygame.image.load(os.path.join("images", "red_image4.png")), (110, 110))
RED_IMAGE_5 = pygame.transform.scale(pygame.image.load(os.path.join("images", "red_image5.png")), (110, 110))
RED_IMAGE_6 = pygame.transform.scale(pygame.image.load(os.path.join("images", "red_image6.png")), (110, 110))

# blue fire tower image
BLUE_IMAGE_0 = pygame.transform.scale(pygame.image.load(os.path.join("images", "blue_image0.png")), (110, 110))
BLUE_IMAGE_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "blue_image1.png")), (110, 110))
BLUE_IMAGE_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "blue_image2.png")), (110, 110))
BLUE_IMAGE_3 = pygame.transform.scale(pygame.image.load(os.path.join("images", "blue_image3.png")), (110, 110))
BLUE_IMAGE_4 = pygame.transform.scale(pygame.image.load(os.path.join("images", "blue_image4.png")), (110, 110))
BLUE_IMAGE_5 = pygame.transform.scale(pygame.image.load(os.path.join("images", "blue_image5.png")), (110, 110))
BLUE_IMAGE_6 = pygame.transform.scale(pygame.image.load(os.path.join("images", "blue_image6.png")), (110, 110))

# vacancy image
PLOT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "vacant_lot.png")), (40, 40))


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
    def __init__(self, x: int, y: int, attack_strategy:AttackStrategy):
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
        self.attack_strategy = attack_strategy  # chose an attack strategy (AOE, single attack ....)
        self.attack_strategy_name = ""
        self.value = [100, 140, 200, 300, 380, 460, 10000]


    @classmethod
    # moon_tower attacks all the enemies
    def moon_tower(cls, x: int, y: int)->Tower:
        moon_tower = cls(x, y, SingleSlowAttack())
        moon_tower.name = "Moon Tower"
        moon_tower.intro = "The ruby that absorbs the essence of the sun and the "
        moon_tower.intro1 = "moon is carved into the shape of the moon and installed "
        moon_tower.intro2 = "on the tower to form an indestructible moon tower."
        moon_tower.attack_strategy_name = "Single Slow Attack"
        moon_tower.sprites = []
        moon_tower.update_speed = 0.2
        moon_tower.max_current_sprites = 9
        moon_tower.sprites.append(MOON_IMAGE_0)
        moon_tower.sprites.append(MOON_IMAGE_1)
        moon_tower.sprites.append(MOON_IMAGE_2)
        moon_tower.sprites.append(MOON_IMAGE_3)
        moon_tower.sprites.append(MOON_IMAGE_4)
        moon_tower.sprites.append(MOON_IMAGE_5)
        moon_tower.sprites.append(MOON_IMAGE_6)
        moon_tower.sprites.append(MOON_IMAGE_7)
        moon_tower.sprites.append(MOON_IMAGE_8)
        moon_tower.sprites.append(MOON_IMAGE_9)
        moon_tower._range = [140, 160, 180, 200, 220, 250, 350]
        moon_tower.value = [100, 140, 200, 280, 360, 450, 10000]
        return moon_tower

    @classmethod
    # red_fire_tower attacks and inflicts continuous damages on an enemy
    def red_fire_tower(cls, x: int, y: int)->Tower:
        red_fire_tower = cls(x, y, AOE())
        red_fire_tower.name = "Fire Totem"
        red_fire_tower.intro = "The shaman with white magic devoted his heart "
        red_fire_tower.intro1 = "to the flame totem to make it alive"
        red_fire_tower.intro2 = "and defend the survival of mankind"
        red_fire_tower.attack_strategy_name = "AOE"
        red_fire_tower.sprites = []
        red_fire_tower.update_speed = 0.2
        red_fire_tower.max_current_sprites = 6
        red_fire_tower.sprites.append(RED_IMAGE_0)
        red_fire_tower.sprites.append(RED_IMAGE_1)
        red_fire_tower.sprites.append(RED_IMAGE_2)
        red_fire_tower.sprites.append(RED_IMAGE_3)
        red_fire_tower.sprites.append(RED_IMAGE_4)
        red_fire_tower.sprites.append(RED_IMAGE_5)
        red_fire_tower.sprites.append(RED_IMAGE_6)

        red_fire_tower._range = [120, 125, 130, 135, 140, 145, 250]
        red_fire_tower._damage = [8, 14, 18, 22, 25, 35, 50]
        red_fire_tower.value = [120, 160, 220, 320, 400, 500, 10000]
        return red_fire_tower

    @classmethod
    # blue_fire_tower attacks and slows down enemies
    def blue_fire_tower(cls, x: int, y: int)->Tower:
        blue_fire_tower = cls(x, y, AOESlowAttack())
        blue_fire_tower.name = "Ice Totem"
        blue_fire_tower.intro = "Black magic wizards sacrifice hundreds of thousands of "
        blue_fire_tower.intro1 = "virus-infected mutants to summon ice totems "
        blue_fire_tower.intro2 = "in the endless abyss"
        blue_fire_tower.attack_strategy_name = "AOE Slow Attack"
        blue_fire_tower.sprites = []
        blue_fire_tower.update_speed = 0.2
        blue_fire_tower.max_current_sprites = 6
        blue_fire_tower.sprites.append(BLUE_IMAGE_0)
        blue_fire_tower.sprites.append(BLUE_IMAGE_1)
        blue_fire_tower.sprites.append(BLUE_IMAGE_2)
        blue_fire_tower.sprites.append(BLUE_IMAGE_3)
        blue_fire_tower.sprites.append(BLUE_IMAGE_4)
        blue_fire_tower.sprites.append(BLUE_IMAGE_5)
        blue_fire_tower.sprites.append(BLUE_IMAGE_6)

        blue_fire_tower._range = [120, 125, 130, 135, 140, 145, 280]
        blue_fire_tower._damage = [10, 15, 19, 25, 30, 37, 60]
        blue_fire_tower.value = [150, 200, 250, 300, 400, 500, 10000]
        return blue_fire_tower

    @classmethod
    # obelisk_tower attacks an enemy far away
    def obelisk_tower(cls, x: int, y: int)->Tower:
        obelisk_tower = cls(x, y, Snipe())
        obelisk_tower.name = "Obelisk Tower"
        obelisk_tower.intro = "The obelisk from the underground of ancient Egypt "
        obelisk_tower.intro1 = "has the awesome power of annihilating the enemy with "
        obelisk_tower.intro2 = "one strike by falling terrifying lightning."
        obelisk_tower.attack_strategy_name = "Snipe"
        obelisk_tower.sprites = []
        obelisk_tower.max_current_sprites = 13
        obelisk_tower.update_speed = 0.25
        obelisk_tower.sprites.append(OBELISK_IMAGE_0)
        obelisk_tower.sprites.append(OBELISK_IMAGE_1)
        obelisk_tower.sprites.append(OBELISK_IMAGE_2)
        obelisk_tower.sprites.append(OBELISK_IMAGE_3)
        obelisk_tower.sprites.append(OBELISK_IMAGE_4)
        obelisk_tower.sprites.append(OBELISK_IMAGE_5)
        obelisk_tower.sprites.append(OBELISK_IMAGE_6)
        obelisk_tower.sprites.append(OBELISK_IMAGE_7)
        obelisk_tower.sprites.append(OBELISK_IMAGE_8)
        obelisk_tower.sprites.append(OBELISK_IMAGE_9)
        obelisk_tower.sprites.append(OBELISK_IMAGE_10)
        obelisk_tower.sprites.append(OBELISK_IMAGE_11)
        obelisk_tower.sprites.append(OBELISK_IMAGE_12)
        obelisk_tower.sprites.append(OBELISK_IMAGE_13)

        obelisk_tower._range = [100, 105, 110, 115, 120, 125, 220]  # tower attack range
        obelisk_tower._damage = [20, 40, 60, 80, 120, 160, 400]
        obelisk_tower.cd_max_count = 120  # tower damage
        obelisk_tower.value = [1000, 2000, 3000, 4000, 5000, 6000, 20000]
        return obelisk_tower

    def update(self):
        self.current_sprites += self.update_speed
        if self.current_sprites >= self.max_current_sprites:
            self.current_sprites = 0
        self.image = self.sprites[int(self.current_sprites)]

    def attack(self, enemy_group: list):
        # cd
        if self.cd_count < self.cd_max_count:
            self.cd_count += 1
            return
        # syntax: attack_strategy().attack(tower, enemy_group, cd_count)
        # It's something like you hire a "Strategist" to decide how to attack the enemy
        # You can add other ways of attack just by expanding the "attack_strategy.py"
        self.cd_count = self.attack_strategy.attack(enemy_group, self, self.cd_count)

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





