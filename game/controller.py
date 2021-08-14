from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.model import GameModel
    from game.view import GameView
import pygame
from settings import game_status
from exit_win.exit_win import ExitWin


# controller
class GameControl:
    def __init__(self, game_model:GameModel, game_view:GameView):
        self.model = game_model
        self.view = game_view
        self.events = {"game quit": False,
                       "mouse position": [0, 0],
                       "keyboard key": 0,
                       "Add money": 0,
                       "die": False,
                       "live":False,
                       "Kill all": 0,
                       "Add towers": 0,
                       "pause_esc": 0,
                       "health up": 0
                       }
        self.request = None  # response of user input

    def update_model(self):
        """update the model and the view here"""
        self.request = self.model.get_request(self.events)
        self.model.user_request(self.request)
        self.model.call_menu()
        self.model.towers_attack()
        self.model.enemies_advance()

        for tw in self.model.towers:
            tw.update()
        for en in self.model.enemies.get():
            en.update()

    def receive_user_input(self):
        """receive user input from the events"""
        # event initialization
        self.events = {"game quit": False,
                       "mouse position": None,
                       "keyboard key": None,
                       "Add money": None,
                       "die": False,
                       "live":False,
                       "Kill all": None,
                       "Add towers": None,
                       "pause_esc": None,
                       "health up": None
                       }
        if self.model.hp <= 0:
            self.events["die"] = True

        if self.model.wave == 3 and self.model.level_counter == 1 and not len(self.model.enemies.get()):
            self.events["live"] = True
        elif self.model.wave == 6 and self.model.level_counter == 2 and not len(self.model.enemies.get()):
            self.events["live"] = True
        elif self.model.wave == 9 and self.model.level_counter == 3 and not len(self.model.enemies.get()):
            self.events["live"] = True
        elif self.model.wave == 12 and self.model.level_counter == 4 and not len(self.model.enemies.get()):
            self.events["live"] = True
        elif self.model.wave == 13 and self.model.level_counter == 5 and not len(self.model.enemies.get()):
            self.events["live"] = True
        # update event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.events["game quit"] = True
                exitWin = ExitWin(self.view.win)
                exitWin.run()

            # player press action
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    self.events["keyboard key"] = pygame.K_n
                if event.key == pygame.K_TAB:
                    self.events["Add money"] = pygame.K_TAB
                if event.key == pygame.K_k:
                    self.events["Kill all"] = pygame.K_k
                if event.key == pygame.K_t:
                    self.events["Add towers"] = pygame.K_t
                if event.key == pygame.K_h:
                    self.events["health up"] = pygame.K_h
                if event.key == pygame.K_ESCAPE:
                    self.events["pause_esc"] = pygame.K_ESCAPE
            # player click action
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.events["mouse position"] = [x, y]

    def update_view(self):
        # render background
        self.view.draw_bg()
        for tw in self.model.towers:
            if tw.name == "Obelisk Tower" or tw.name == "Moon Tower":
                self.view.draw_bullet(tw)
        self.view.draw_base()
        self.view.draw_enemies(self.model.enemies)
        self.view.draw_towers(self.model.towers)
        for tw in self.model.towers:
            if tw.name == "Fire Totem" or tw.name == "Ice Totem":
                self.view.draw_bullet(tw)
        self.view.draw_top_info()
        self.view.draw_potion_list()
        self.view.draw_hp(self.model.hp)
        self.view.draw_range(self.model.selected_tower)
        self.view.draw_plots(self.model.plots)
        if self.model.menu is not None:
            self.view.draw_menu(self.model.menu)
            self.view.draw_btn(self.model.menu.buttons)
        self.view.draw_btn(self.model.main_menu.buttons)
        self.view.draw_money(self.model.money)
        self.view.draw_wave(self.model.wave)
        self.view.draw_potionprice()
        self.view.draw_time()
        if self.model.selected_tower is not None and self.model.show_tower_info:
            self.view.draw_properties(self.model.selected_tower)
        if self.model.selected_potion_info is not None:
            self.view.draw_potion_property(self.model.selected_potion_info)
        self.view.draw_mouse()




    @property
    def quit_game(self)->bool:
        return self.events["game quit"]


