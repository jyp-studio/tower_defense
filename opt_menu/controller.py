from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from opt_menu.model import OptMenuModel
    from opt_menu.view import OptMenuView
import pygame
from settings import game_status
from exit_win.exit_win import ExitWin

class OptMenuController:
    def __init__(self, menu_model:OptMenuModel, menu_view:OptMenuView):
        self.model = menu_model
        self.view = menu_view
        self.events = {"game quit": False,
                       "mouse position": [0, 0],
                       "game back": False
                       }
        self.request = None  # response of user input

    def update_model(self):
        """update the model and the view here"""
        self.request = self.model.get_request(self.events)
        self.model.user_request(self.request)

    def receive_user_input(self):
        """receive user input from the events"""
        # event initialization
        self.events = {"game quit": False,
                       "mouse position": None,
                       }
        # update event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.events["game quit"] = True
                exitWin=ExitWin(self.view.win)
                exitWin.run()

            # player click action
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.events["mouse position"] = [x, y]

    def update_view(self):
        # render background
        self.view.draw_bg()
        self.view.draw_btn(self.model.buttons)
        self.view.draw_sound_volume()
        self.view.draw_music_volume()
        self.view.draw_map_preview(self.model.map_preview_img)
    
    @property
    def quit_game(self)->dict:
        return self.events["game quit"]
    
    @property
    def back_game(self)->bool:
        return self.model.back_game