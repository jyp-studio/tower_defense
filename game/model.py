import pygame
import os
from tower.towers import Tower, Vacancy
from enemy.enemies import EnemyGroup
from menu.menus import UpgradeMenu, BuildMenu, MainMenu
from game.user_request import RequestSubject, TowerFactory, TowerSeller, TowerDeveloper, EnemyGenerator, Muse, Music
from settings import WIN_WIDTH, WIN_HEIGHT, BACKGROUND_IMAGE


class GameModel:
    def __init__(self):
        # data
        self.bg_image = pygame.transform.scale(BACKGROUND_IMAGE, (WIN_WIDTH, WIN_HEIGHT))
        self.__towers = [Tower.moon_tower(250, 380), Tower.obelisk_tower(180, 300)]
        self.__enemies = EnemyGroup()
        self.__menu = None
        self.__main_menu = MainMenu()
        self.__plots = [Vacancy(50, 350), Vacancy(350, 280)]
        # selected item
        self.selected_plot = None
        self.selected_tower = None
        self.selected_button = None
        # apply observer pattern
        self.subject = RequestSubject(self)
        self.seller = TowerSeller(self.subject)
        self.developer = TowerDeveloper(self.subject)
        self.factory = TowerFactory(self.subject)
        self.generator = EnemyGenerator(self.subject)
        self.muse = Muse(self.subject)
        self.music = Music(self.subject)
        #
        self.wave = 0
        self.money = 500000
        self.max_hp = 10
        self.hp = self.max_hp
        self.sound = pygame.mixer.Sound(os.path.join("sound", "sound.flac"))

    def user_request(self, user_request: str):
        """ add tower, sell tower, upgrade tower"""
        self.subject.notify(user_request)

    def get_request(self, events: dict) -> str:
        """get keyboard response or button response"""
        # initial
        self.selected_button = None
        # key event
        if events["keyboard key"] is not None:
            return "start new wave"
        # mouse event
        if events["mouse position"] is not None:
            x, y = events["mouse position"]
            self.select(x, y)
            if self.selected_button is not None:
                return self.selected_button.response
            return "nothing"
        return "nothing"

    def select(self, mouse_x: int, mouse_y: int) -> None:
        """change the state of whether the items are selected"""
        # if the item is clicked, select the item
        for tw in self.__towers:
            if tw.clicked(mouse_x, mouse_y):
                self.selected_tower = tw
                self.selected_plot = None
                return

        for pt in self.__plots:
            if pt.clicked(mouse_x, mouse_y):
                self.selected_tower = None
                self.selected_plot = pt
                return

        # if the button is clicked, get the button response.
        # and keep selecting the tower/plot.
        if self.__menu is not None:
            for btn in self.__menu.buttons:
                if btn.clicked(mouse_x, mouse_y):
                    self.selected_button = btn
            if self.selected_button is None:
                self.selected_tower = None
                self.selected_plot = None
        # menu btn
        for btn in self.__main_menu.buttons:
            if btn.clicked(mouse_x, mouse_y):
                self.selected_button = btn

    def call_menu(self):
        if self.selected_tower is not None:
            x, y = self.selected_tower.rect.center
            self.__menu = UpgradeMenu(x, y)
        elif self.selected_plot is not None:
            x, y = self.selected_plot.rect.center
            self.__menu = BuildMenu(x, y)
        else:
            self.__menu = None

    def towers_attack(self):
        for tw in self.__towers:
            tw.attack(self.__enemies.get())

    def enemies_advance(self):
        self.__enemies.advance(self)

    @property
    def enemies(self):
        return self.__enemies

    @property
    def towers(self):
        return self.__towers

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, new_menu):
        self.__menu = new_menu

    @property
    def plots(self):
        return self.__plots











