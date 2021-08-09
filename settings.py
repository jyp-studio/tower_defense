import pygame
import os
from singleton import VolController,MapController

# screen size
WIN_WIDTH = 1024
WIN_HEIGHT = 600
# frame rate
FPS = 60
# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (147, 0, 147)

# image
HP_GRAY_IMAGE = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (40, 40))
HP_IMAGE = pygame.transform.scale(pygame.image.load("images/hp.png"), (40, 40))

# singleton
singleton_vol_controller=VolController()
singleton_map_controller=MapController(WIN_WIDTH, WIN_HEIGHT)

# global var
game_status={
    "run":True,
    "go_start_menu":False,
    "restart":False}
