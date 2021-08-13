from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.model import GameModel
import pygame
import math
import random
import os
from settings import singleton_map_controller
from gif import *
from color_settings import *

pygame.init()


class Enemy:
    def __init__(self, image):
        self.name = ""
        dir = random.randint(1, len(singleton_map_controller.curPathPage))
        self.path = singleton_map_controller.curPathPage[dir]
        self.path_index = 0
        self.move_count = 0
        self.stride = 3
        self.max_stride=3
        self.health = 50
        self.max_health = 50
        self.is_dead = 0

        self.sprites = []
        self.current_sprites = 0
        self.max_current_sprites = 10
        self.update_speed = 1
        self.sprites.append(image)
        self.image = self.sprites[self.current_sprites]
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.path_index = 0
        self.right_direction = True

    def move(self):
        x1, y1 = self.path[self.path_index]
        x2, y2 = self.path[self.path_index + 1]
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        max_count = int(distance / self.stride)
        # direction
        direction = x2 - x1
        if direction < 0:
            self.right_direction = False
        else:
            self.right_direction = True
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

    def update(self):
        self.current_sprites += self.update_speed
        if self.current_sprites >= self.max_current_sprites:
            self.current_sprites = 0
        # flip images
        if not self.right_direction:
            flip_image = pygame.transform.flip(self.sprites[int(self.current_sprites)], True, False)
            self.image = flip_image
        else:
            self.image = self.sprites[int(self.current_sprites)]

    def direction(self):
        return self.right_direction



