import pygame
from game.controller import GameControl
from game.model import GameModel
from game.view import GameView
from settings import FPS,game_status


class Game:
    def run(self):
        # initialization
        pygame.init()
        game_model = GameModel()  # core of the game (database, game logic...)
        game_view = GameView()  # render everything
        game_control = GameControl(game_model, game_view)  # deal with the game flow and user request

        while game_status["run"] and not game_status["go_start_menu"]:
            pygame.time.Clock().tick(FPS)  # control the frame rate
            game_control.receive_user_input()  # receive user input
            game_control.update_model()  # update the model
            game_control.update_view()  # update the view
            pygame.display.update()

