import pygame
import os
from settings import FPS,WIN_WIDTH,WIN_HEIGHT
from menu.menus import Button
from dir_path import *

class GameUI:
    def __init__(self):
        self.frame = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "game_view.png")), (WIN_WIDTH, WIN_HEIGHT))