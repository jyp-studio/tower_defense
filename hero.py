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


class Hero:
    def __init__(self, x: int, y: int):
        self.name = ""
        self.image = FIRE_BALL_0  # image of the tower
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the tower

        self.level = 0  # level of the tower

        self._range = [100, 110, 120, 130, 140, 150, 300]  # tower attack range
        self._damage = [10, 20, 30, 40, 50, 60, 100]  # tower damage
        self.cd_count = 0  # used in self.is_cool_down()
        self.cd_max_count = 60  # used in self.is_cool_down()

        self.health = 50
        self.max_health = 50

        self.stride = 3

    def move(self):
        pass

    def attack(self):
        pass
