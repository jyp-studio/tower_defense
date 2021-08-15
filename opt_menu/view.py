import pygame
import math
import os
from settings import WIN_WIDTH, WIN_HEIGHT, HP_IMAGE, HP_GRAY_IMAGE,singleton_vol_controller,MOUSE
from color_settings import *
from dir_path import *

MENU_VIEW = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "menu_background.png")), (WIN_WIDTH, WIN_HEIGHT))


class OptMenuView:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font = pygame.font.Font(os.path.join(FONT_DIR, "CESCOBold.ttf"), 30)
        self.font1 = pygame.font.Font(os.path.join(FONT_DIR, "28 Days Later.ttf"), 30)

    def draw_bg(self):
        self.win.blit(MENU_VIEW, (0, 0))

    def draw_mouse(self):
        x, y = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        self.win.blit(MOUSE, (x, y))
    
    def draw_btn(self, buttonList: list):
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
        self.win.blit(text, (455, 450))

    def draw_map_hint(self, map_img: pygame.Surface, counter: int):
        pygame.draw.rect(MENU_VIEW, (0, 0, 0, 110), [262, 300, map_img.get_rect().w, map_img.get_rect().h])
        if counter == 1:
            text = self.font1.render(f"There are several variants of bugs,", True, (255, 255, 255))
            text1 = self.font1.render(f"remember that only Moon Tower and", True, (255, 255, 255))
            text2 = self.font1.render(f"Obelisk can attack flying species.", True, (255, 255, 255))
        elif counter == 2:
            text = self.font1.render(f"The cursed orcs have strong defenses,", True, (255, 255, 255))
            text1 = self.font1.render(f"remember that Moon Tower can do twice", True, (255, 255, 255))
            text2 = self.font1.render(f"as much damage to the terrifying orcs.", True, (255, 255, 255))
        elif counter == 3:
            text = self.font1.render(f"Flying monsters are raging, remember ", True, (255, 255, 255))
            text1 = self.font1.render(f"that ghosts have a chance to dodge ", True, (255, 255, 255))
            text2 = self.font1.render(f"attacks.", True, (255, 255, 255))
        elif counter == 4:
            text = self.font1.render(f"The skulls are resurrect constantly.", True, (255, 255, 255))
            text1 = self.font1.render(f"Remember that Blue Totem can", True, (255, 255, 255))
            text2 = self.font1.render(f"cause fatal damage to them.", True, (255, 255, 255))
        else:
            text = self.font1.render(f"Evil witches will summon knights and ", True, (255, 255, 255))
            text1 = self.font1.render(f"dwarfs as shields and restore blood.", True, (255, 255, 255))
            text2 = self.font1.render(f"Obelisk is indeed effective for the boss", True, (255, 255, 255))
        self.win.blit(text, (268, 150 ))
        self.win.blit(text1, (268, 120+ 300))
        self.win.blit(text2, (268, 160+ 300))

    def draw_map_preview(self, map_img: pygame.Surface, counter: int):
        self.win.blit(map_img, (262, 109))
        pygame.draw.rect(MENU_VIEW, BLACK, [262, 70, map_img.get_rect().w, 40])
        if counter == 1:
            text = self.font.render(f"Arrogant Triton", True, (255, 255, 255))
        elif counter == 2:
            text = self.font.render(f"Eternal Empire", True, (255, 255, 255))
        elif counter == 3:
            text = self.font.render(f"Augustine Autumn", True, (255, 255, 255))
        elif counter == 4:
            text = self.font.render(f"Heavy Artillery", True, (255, 255, 255))
        else:
            text = self.font.render(f"Dormant Realm", True, (255, 255, 255))
        center = (1024 / 2 - text.get_rect().w / 2, 75)
        self.win.blit(text, center)

