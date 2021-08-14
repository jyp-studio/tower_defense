import pygame
import math
import os
from settings import WIN_WIDTH, WIN_HEIGHT, HP_IMAGE, HP_GRAY_IMAGE,singleton_vol_controller
from color_settings import *

MENU_VIEW = pygame.transform.scale(pygame.image.load(os.path.join("images", "menu_background.png")), (WIN_WIDTH, WIN_HEIGHT))
MOUSE = pygame.transform.scale(pygame.image.load(os.path.join("images", "mouse.png")), (20, 20))


class OptMenuView:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font = pygame.font.Font(os.path.join("font", "CESCOBold.ttf"), 30)

    def draw_bg(self):
        self.win.blit(MENU_VIEW, (0, 0))

    def draw_mouse(self):
        x, y = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        self.win.blit(MOUSE, (x, y))
    
    def draw_btn(self,buttonList:list):
        for btn in buttonList:
            self.win.blit(btn.image, btn.rect)

    def draw_sound_volume(self):
        volume = math.ceil(singleton_vol_controller.sound_volume*100)
        volume = math.ceil(volume/5)*5
        text = self.font.render(f"Sound volume: {volume}%", True, (255, 255, 255))
        self.win.blit(text, (455,375))

    def draw_music_volume(self):
        volume = math.ceil(singleton_vol_controller.music_volume*100)
        volume = math.ceil(volume/5)*5
        text = self.font.render(f"Music volume: {volume}%", True, (255, 255, 255))
        self.win.blit(text, (455,450))

    def draw_map_preview(self, map_img:pygame.Surface):
        self.win.blit(map_img, (262,40))