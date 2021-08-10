from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.model import GameModel
import pygame
import math
import random
import os
from settings import singleton_map_controller
from color_settings import *

pygame.init()
GOBLIN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "enemy_2.png")), (80, 80))
ORC_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "enemy_1.png")), (80, 80))
IMMORTAL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "enemy.png")), (60, 60))
DEAD_IMMORTAL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "enemy_3.png")), (70, 70))
MUMMY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "enemy_4.png")), (70, 70))
DARK_ANGEL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "enemy_5.png")), (70, 70))
DEAD_DARK_ANGEL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "enemy_6.png")), (70, 70))
GREEN_MONSTER_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "enemy_7.png")), (150, 150))


class Enemy:
    def __init__(self):
        self.name = ""
        dir = random.randint(1,len(singleton_map_controller.curPathPage))
        self.path = singleton_map_controller.curPathPage[dir]
        self.path_index = 0
        self.move_count = 0
        self.stride = 3
        self.image = GOBLIN_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.path_index = 0
        self.health = 50
        self.max_health = 50
        self.is_dead = 0

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


class GoblinEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "goblin"
        self.stride = 10


class OrcEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "orc"
        self.image = ORC_IMAGE
        self.stride = 3
        self.health = 200
        self.max_health = 200


class ImmortalEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "immortal"
        self.image = IMMORTAL_IMAGE
        self.stride = 0.5
        self.health = 500
        self.max_health = 500
        self.is_dead = 1


class MummyEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "mummy"
        self.image = MUMMY_IMAGE
        self.stride = 2
        self.health = 1000
        self.max_health = 1000
        self.is_dead = 0


class DarkAngelEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "dark angel"
        self.image = DARK_ANGEL_IMAGE
        self.stride = 4
        self.health = 1000
        self.max_health = 1000
        self.is_dead = 2


class GreenMonsterEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "green monster"
        self.image = GREEN_MONSTER_IMAGE
        self.stride = 0.5
        self.health = 600000
        self.max_health = 500000
        self.is_dead = 0

      
class EnemyGroup:
    def __init__(self):
        self.campaign_count = 0
        self.campaign_max_count = 60   # (unit: frame)
        self.__reserved_members = []
        self.__expedition = []
        self.wave_counter = 0

    def advance(self, model:GameModel):
        # use model.hp and model.money to access the hp and money information
        self.campaign()
        for en in self.__expedition:
            en.move()
            if en.health <= 0:
                if en.is_dead == 0:
                    self.retreat(en)
                    model.money += 15
                else:
                    if en.is_dead == 1:
                        en.image = DEAD_IMMORTAL_IMAGE
                        en.health = 100
                        en.max_health = 100
                        en.stride = 20
                        en.is_dead = 0
                    if en.is_dead == 2:
                        en.image = DEAD_DARK_ANGEL_IMAGE
                        en.health = 2000
                        en.max_health = 2000
                        en.stride = 0.5
                        en.is_dead = 0
            # delete the object when it reach the base
            if singleton_map_controller.curBaseRect.collidepoint(en.rect.centerx, en.rect.centery):
                self.retreat(en)
                model.hp -= 1

    def campaign(self):
        """Enemy go on an expedition."""
        if self.campaign_count > self.campaign_max_count and self.__reserved_members:
            self.__expedition.append(self.__reserved_members.pop())
            self.campaign_count = 0
        else:
            self.campaign_count += 1

    def add(self, num:int):
        """Generate the enemies for next wave"""
        if self.is_empty():
            if self.wave_counter % 6 == 0:
                self.__reserved_members = [GoblinEnemy() for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 6 == 1:
                self.__reserved_members = [OrcEnemy() for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 6 == 2:
                self.__reserved_members = [ImmortalEnemy() for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 6 == 3:
                self.__reserved_members = [MummyEnemy() for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 6 == 4:
                self.__reserved_members = [DarkAngelEnemy() for _ in range(num)]
                self.wave_counter += 1
            else:
                self.__reserved_members = [GreenMonsterEnemy() for _ in range(num)]
                self.wave_counter = 0

    def get(self) -> list:
        """Get the enemy list"""
        return self.__expedition

    def is_empty(self) -> bool:
        """Return whether the enemy is empty (so that we can move on to next wave)"""
        return False if self.__reserved_members or self.__expedition else True

    def retreat(self, enemy: Enemy):
        """Remove the enemy from the expedition"""
        self.__expedition.remove(enemy)

    def retreat_all(self):
        self.__expedition = []
        self.__reserved_members = []





