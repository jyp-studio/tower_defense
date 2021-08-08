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
# enemy path
PATH = [(22, 308), (52, 283), (84, 283), (110, 305), (116, 341), (115, 375), (112, 405), (116, 433),
          (135, 455), (159, 475), (188, 480), (217, 481), (243, 474), (267, 463), (291, 454), (315, 441),
          (334, 423), (343, 398), (339, 368), (328, 345), (305, 331), (282, 322), (264, 303), (255, 283),
          (259, 259), (274, 239), (294, 225), (318, 214), (347, 212), (373, 217), (394, 230), (410, 250),
          (429, 266), (446, 282), (465, 295), (483, 310), (502, 321), (523, 309), (535, 282), (535, 254),
          (533, 230), (532, 190)]
# base
BASE = pygame.Rect(430, 90, 195, 130)

# image
HP_GRAY_IMAGE = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (40, 40))
HP_IMAGE = pygame.transform.scale(pygame.image.load("images/hp.png"), (40, 40))

# singleton
singleton_vol_controller=VolController()
singleton_map_controller=MapController()

# global var
game_status={
    "run":True,
    "go_start_menu":False}

