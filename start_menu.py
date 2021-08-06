import pygame
import os
from game.game import Game
from color_settings import *
from settings import WIN_WIDTH, WIN_HEIGHT, FPS

pygame.init()
pygame.mixer.init()


class StartMenu:
    def __init__(self):
        # win
        self.menu_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # background
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join("images", "start_menu.png")), (WIN_WIDTH, WIN_HEIGHT))
        # button
        self.start_btn = Buttons(349, 315, 338, 101)  # x, y, width, height
        self.sound_btn = Buttons(725, 525, 90, 70)
        self.mute_btn = Buttons(830, 525, 90, 70)
        self.buttons = [self.sound_btn,
                        self.mute_btn,
                        self.start_btn]
        # music and sound
        self.sound = pygame.mixer.Sound("./sound/sound.flac")

    def play_music(self):
        pygame.mixer.music.load("./sound/menu.wav")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        self.sound.set_volume(0.2)

    def menu_run(self):
        run = True
        clock = pygame.time.Clock()
        pygame.display.set_caption("Covid-19 Defense Game")
        self.play_music()
        while run:
            clock.tick(FPS)
            self.menu_win.blit(self.bg, (0, 0))
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # quit
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # check if hit start btn
                    if self.start_btn.clicked(x, y):
                        self.sound.play()
                        game = Game()
                        game.run()
                        run = False
                    if self.mute_btn.clicked(x, y):
                        pygame.mixer.music.pause()
                    if self.sound_btn.clicked(x, y):
                        pygame.mixer.music.unpause()
                    """(Q1.1) music on/off according to the button"""
                    # (hint) pygame.mixer.music.pause/unpause

            # while cursor is moving (not click)
            """(Q1.2) create button frame and draw"""
            # (hint) use a for loop to go through all the buttons, create the frame, and draw it.
            for button in self.buttons:
                if button.rect.collidepoint(x, y):
                    button.create_frame(x, y)
                    button.draw_frame(self.menu_win)
            pygame.display.update()
        pygame.quit()


class Buttons:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.frame = None

    def clicked(self, x: int, y: int) -> bool:
        if self.rect.collidepoint(x, y):
            return True
        return False

    def create_frame(self, x: int, y: int):
        """if cursor position is on the button, create button frame"""
        if self.clicked(x, y):
            x, y, w, h = self.rect
            self.frame = pygame.Rect(x - 5, y - 5, w + 10, h + 10)
        else:
            self.frame = None

    def draw_frame(self, win):
        if self.frame is not None:
            pygame.draw.rect(win, WHITE, self.frame, 10)
