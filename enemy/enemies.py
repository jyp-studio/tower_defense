import pygame
import math
import os
from settings import PATH, BASE
from color_settings import *

pygame.init()
ENEMY_IMAGE = pygame.image.load(os.path.join("images", "enemy.png"))


class Enemy:
    def __init__(self):
        self.path = PATH
        self.path_index = 0
        self.move_count = 0
        self.stride = 1
        self.image = pygame.transform.scale(ENEMY_IMAGE, (40, 50))
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.path_index = 0
        self.move_count = 0
        self.health = 10
        self.max_health = 10

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


class EnemyGroup:
    def __init__(self):
        self.campaign_count = 0
        self.campaign_max_count = 60   # (unit: frame)
        self.__reserved_members = []
        self.__expedition = []

    def advance(self, model):
        """Bonus.2"""
        # use model.hp and model.money to access the hp and money information
        self.campaign()
        for en in self.__expedition:
            en.move()
            if en.health <= 0:
                self.retreat(en)
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
            self.__reserved_members = [Enemy() for _ in range(num)]

    def get(self):
        """Get the enemy list"""
        return self.__expedition

    def is_empty(self):
        """Return whether the enemy is empty (so that we can move on to next wave)"""
        return False if self.__reserved_members or self.__expedition else True

    def retreat(self, enemy):
        """Remove the enemy from the expedition"""
        self.__expedition.remove(enemy)





