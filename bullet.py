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


class Bullet:
    def __init__(self):
        self.name = ""
        self.image = ""