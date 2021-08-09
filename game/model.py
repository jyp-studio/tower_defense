import pygame
import os
from tower.towers import Tower, Vacancy
from enemy.enemies import EnemyGroup
from menu.menus import UpgradeMenu, BuildMenu, MainMenu
from settings import WIN_WIDTH, WIN_HEIGHT,singleton_vol_controller,singleton_map_controller
from game_UI.game_UI import GameUI
from opt_menu.opt_menu import OptMenu
from game_over.game_over import GameOver
from game.user_request import *


class GameModel:
    def __init__(self):
        # data
        self.bg_image = pygame.transform.scale(singleton_map_controller.curMap, (WIN_WIDTH, WIN_HEIGHT))
        self.__towers = []

        self.__enemies = EnemyGroup()
        self.__menu = None
        self.__main_menu = MainMenu()
        self.__plots = [Vacancy(150, 250), Vacancy(290, 420), Vacancy(400, 310),
                        Vacancy(450, 500), Vacancy(650, 420), Vacancy(900, 370)]

        self.show_tower_info = False

        self.move_tower = False

        # selected item
        self.selected_plot = None
        self.selected_tower = None
        self.selected_button = None
        # apply observer pattern
        self.subject = RequestSubject(self)
        self.seller = TowerSeller(self.subject)
        self.developer = TowerDeveloper(self.subject)
        self.evolution = TowerEvolution(self.subject)
        self.add_money = AddMoney(self.subject)
        self.factory = TowerFactory(self.subject)
        self.generator = EnemyGenerator(self.subject)
        self.dieHandler = Die(self.subject)
        self.potion = Potionfunction(self.subject)


        self.muse = Muse(self.subject)
        self.music = Music(self.subject)

        self.pause = Pause(self.subject)

        self.properties = TowerProperties(self.subject)
        self.proper = Music(self.subject)

        #
        self.wave = 0
        self.money = 1000
        self.max_hp = 10
        self.hp = self.max_hp
        self.sound = pygame.mixer.Sound(os.path.join("sound", "sound.mp3"))

        self.sound.set_volume(singleton_vol_controller.sound_volume)

        self.UI = GameUI()
        self.opt_menu = OptMenu()
        self.GameOverMenu = GameOver()

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
        if events["Add money"] is not None:
            return "add money"
        # mouse event
        if events["mouse position"] is not None:
            x, y = events["mouse position"]
            self.select(x, y)
            if self.selected_button is not None:
                return self.selected_button.response
            return "nothing"
        if events["die"]:
            return "die"
        return "nothing"

    def select(self, mouse_x: int, mouse_y: int) -> None:
        """change the state of whether the items are selected"""
        # if the item is clicked, select the item
        for tw in self.__towers:
            if tw.clicked(mouse_x, mouse_y):
                self.sound.play()
                self.selected_tower = tw
                self.selected_plot = None

        for pt in self.__plots:
            if pt.clicked(mouse_x, mouse_y):
                self.sound.play()
                self.selected_tower = None
                self.selected_plot = pt

        # if the button is clicked, get the button response.
        # and keep selecting the tower/plot.
        if self.__menu is not None:
            for btn in self.__menu.buttons:
                if btn.clicked(mouse_x, mouse_y):
                    self.sound.play()
                    self.selected_button = btn
                    # if select the move button then close the menu
                    if btn == "move":
                        self.__menu = None
            if self.selected_button is None:
                self.selected_tower = None
                self.selected_plot = None
                self.show_tower_info = False
                self.move_tower = False

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

    @property
    def main_menu(self):
        return self.__main_menu
    
    @main_menu.setter
    def main_menu(self, new_menu):
        self.__main_menu = new_menu












