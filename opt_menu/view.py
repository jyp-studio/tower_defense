import pygame
import math
import os
from settings import WIN_WIDTH, WIN_HEIGHT, HP_IMAGE, HP_GRAY_IMAGE,singleton_vol_controller
from color_settings import *

MENU_VIEW = pygame.transform.scale(pygame.image.load(os.path.join("images", "menu_background.png")), (WIN_WIDTH, WIN_HEIGHT))


class OptMenuView:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font = pygame.font.Font(os.path.join("font", "comicz.ttf"), 30)

    def draw_bg(self):
        self.win.blit(MENU_VIEW, (0, 0))
    
    def draw_btn(self,buttonList:list):
        for btn in buttonList:
            self.win.blit(btn.image, btn.rect)

    def draw_sound_volume(self):
        volume = math.ceil(singleton_vol_controller.sound_volume*100)
        volume = math.ceil(volume/5)*5
        text = self.font.render(f"Sound volume: {volume}%", True, (255, 255, 255))
        self.win.blit(text, (455,320))

    def draw_music_volume(self):
        volume = math.ceil(singleton_vol_controller.music_volume*100)
        volume = math.ceil(volume/5)*5
        text = self.font.render(f"Music volume: {volume}%", True, (255, 255, 255))
        self.win.blit(text, (455,395))

    def draw_map_preview(self, map_img:pygame.Surface):
        self.win.blit(map_img, (262,5))