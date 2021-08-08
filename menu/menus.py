import pygame
import os

pygame.init()
MENU_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "upgrade_menu.png")), (200, 200))
UPGRADE_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "upgrade.png")), (60, 35))
SELL_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "sell.png")), (40, 40))

RAPID_TEST_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "rapid_test.png")), (40, 40))
PCR_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "pcr.png")), (40, 40))
ALCOHOL_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "alcohol.png")), (15, 40))

muse_button_image = pygame.transform.scale(pygame.image.load("images/muse.png"), (80, 80))
music_button_image = pygame.transform.scale(pygame.image.load("images/sound.png"), (80, 80))
pause_button_image = pygame.transform.scale(pygame.image.load("images/pause.png"), (80, 80))

up_button_image = pygame.transform.scale(pygame.image.load(os.path.join("images", "transparent.png")),(60,55))
down_button_image = pygame.transform.scale(pygame.image.load(os.path.join("images", "transparent.png")),(60,55))

class Button:
    def __init__(self, image, name: str, x: int, y: int):
        self.image = image
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x, y):
        return True if self.rect.collidepoint(x, y) else False

    @property
    def response(self):
        return self.name


class Menu:
    def __init__(self, x: int, y: int):
        self.image = MENU_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self._buttons = []

    @property
    def buttons(self):
        return self._buttons


class UpgradeMenu(Menu):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._buttons = [Button(UPGRADE_BTN_IMAGE, "upgrade", self.rect.centerx, self.rect.centery - 70),
                         Button(SELL_BTN_IMAGE, "sell", self.rect.centerx, self.rect.centery + 75),
                         ]


class BuildMenu(Menu):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._buttons = [Button(ALCOHOL_BTN_IMAGE, "alcohol", self.rect.centerx, self.rect.centery - 70),
                         Button(RAPID_TEST_BTN_IMAGE, "rapid test", self.rect.centerx, self.rect.centery + 75),
                         Button(PCR_BTN_IMAGE, "pcr", self.rect.centerx - 65, self.rect.centery + 10)
                         ]


class MainMenu:
    def __init__(self):
        self._buttons = [Button(music_button_image, "music", 815, 45),
                         Button(muse_button_image, "mute", 895, 45),
                         Button(pause_button_image, "pause", 980, 45),
                         Button(up_button_image, "potion_up",40,120),
                         Button(down_button_image, "potion_down",40,565),
                         ]

    @property
    def buttons(self):
        return self._buttons







