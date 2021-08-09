import pygame
import math
import os
from settings import PATH, BASE
from color_settings import *

pygame.init()
GOBLIN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "enemy_2.png")), (80, 80))
ORC_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "enemy_1.png")), (80, 80))
IMMORTAL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "enemy.png")), (60, 60))
DEAD_IMMORTAL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "enemy_3.png")), (70, 70))
MUMMY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "enemy_4.png")), (70, 70))
DARK_ANGEL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "enemy_5.png")), (70, 70))
DEAD_DARK_ANGEL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "enemy_6.png")), (70, 70))
GREEN_MONSTER_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "enemy_7.png")), (100, 100))


class Enemy:
    def __init__(self, image, stride: int, health: int, is_dead: int):
        self.name = ""
        self.path = PATH
        self.path_index = 0
        self.move_count = 0
        self.stride = stride
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.path_index = 0
        self.move_count = 0
        self.health = health
        self.max_health = health
        self.is_dead = is_dead

    def move(self):
        x1, y1 = self.path[self.path_index]
        x2, y2 = self.path[self.path_index + 1]
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        max_count = int(distance / self.stride)
        # compute the unit vector
        unit_vector_x = (x2 - x1) / distance
        unit_vector_y = (y2 - y1) / distance
        # compute the movement
        delta_x = unit_vector_x * self.stride * self.move_count
        delta_y = unit_vector_y * self.stride * self.move_count
        # update the position and counter
        if self.move_count <= max_count:
            self.rect.center = (x1 + delta_x, y1 + delta_y)
            self.move_count += 1
        else:
            self.move_count = 0
            self.path_index += 1
            self.rect.center = self.path[self.path_index]

    @classmethod
    def goblin_enemy(cls):
        goblin_enemy = cls(GOBLIN_IMAGE, 10, 50, 0)
        goblin_enemy.name = "goblin"

    @classmethod
    def orc_enemy(cls):
        orc_enemy = cls(ORC_IMAGE, 3, 200, 0)
        orc_enemy.name = "orc"

    @classmethod
    def immortal_enemy(cls):
        immortal_enemy = cls(IMMORTAL_IMAGE, 1, 500, 1)
        immortal_enemy.name = "immortal"

    @classmethod
    def mummy_enemy(cls):
        mummy_enemy = cls(MUMMY_IMAGE, 2, 1000, 0)
        mummy_enemy.name = "mummy"

    @classmethod
    def dark_angel_enemy(cls):
        dark_angel_enemy = cls(DARK_ANGEL_IMAGE, 4, 1000, 2)
        dark_angel_enemy.name = "dark angel"

    @classmethod
    def green_monster_enemy(cls):
        green_monster_enemy = cls(DARK_ANGEL_IMAGE, 1, 6000, 0)
        green_monster_enemy.name = "green monster"


class EnemyGroup:
    def __init__(self):
        self.campaign_count = 0
        self.campaign_max_count = 60   # (unit: frame)
        self.__reserved_members = []
        self.__expedition = []
        self.wave_counter = 0

    def advance(self, model):
        # use model.hp and model.money to access the hp and money information
        self.campaign()
        for en in self.__expedition:
            en.move()
            if en.health <= 0:
                if en.is_dead == 0:
                    self.retreat(en)
                else:
                    if en.is_dead == 1:
                        en.is_dead = 0
                        en.health = 200
                        en.stride = 10
                        en.image = DEAD_IMMORTAL_IMAGE
                    if en.is_dead == 2:
                        en.is_dead = 0
                        en.health = 2000
                        en.stride = 1
                        en.image = DEAD_DARK_ANGEL_IMAGE
                model.money += 15
            # delete the object when it reach the base
            if BASE.collidepoint(en.rect.centerx, en.rect.centery):
                self.retreat(en)
                model.hp -= 1

    def campaign(self):
        """Enemy go on an expedition."""
        if self.campaign_count > self.campaign_max_count and self.__reserved_members:
            self.__expedition.append(self.__reserved_members.pop())
            self.campaign_count = 0
        else:
            self.campaign_count += 1

    def add(self, num):
        """Generate the enemies for next wave"""
        if self.is_empty():
            if self.wave_counter % 6 == 0:
                self.__reserved_members = [Enemy(GOBLIN_IMAGE, 10, 50, 0) for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 6 == 1:
                self.__reserved_members = [Enemy(ORC_IMAGE, 3, 200, 0) for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 6 == 2:
                self.__reserved_members = [Enemy(IMMORTAL_IMAGE, 1, 500, 1) for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 6 == 3:
                self.__reserved_members = [Enemy(MUMMY_IMAGE, 2, 1000, 0) for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 6 == 4:
                self.__reserved_members = [Enemy(DARK_ANGEL_IMAGE, 4, 1000, 2) for _ in range(num)]
                self.wave_counter += 1
            else:
                self.__reserved_members = [Enemy(GREEN_MONSTER_IMAGE, 1, 6000, 0) for _ in range(num)]
                self.wave_counter = 0

    def get(self):
        """Get the enemy list"""
        return self.__expedition

    def is_empty(self):
        """Return whether the enemy is empty (so that we can move on to next wave)"""
        return False if self.__reserved_members or self.__expedition else True

    def retreat(self, enemy):
        """Remove the enemy from the expedition"""
        self.__expedition.remove(enemy)

    def retreat_all(self):
        self.__expedition = []
        self.__reserved_members = []





