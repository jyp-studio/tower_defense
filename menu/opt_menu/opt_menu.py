import pygame
from settings import FPS,game_status
from opt_menu.controller import OptMenuController
from opt_menu.model import OptMenuModel
from opt_menu.view import OptMenuView

class OptMenu:
    def __init__(self):
        self.back_game=False

    def run(self):
        # initialization
        pygame.init()
        menu_model = OptMenuModel()  # core of the game (database, game logic...)
        menu_view = OptMenuView()  # render everything
        menu_control = OptMenuController(menu_model, menu_view)  # deal with the game flow and user request

        self.back_game=False
        while game_status["run"] and not self.back_game and not game_status["go_start_menu"]:
            pygame.time.Clock().tick(FPS)  # control the frame rate
            menu_control.receive_user_input()  # receive user input
            menu_control.update_model()  # update the model
            menu_control.update_view()  # update the view
            pygame.display.update()
            self.back_game = menu_control.back_game