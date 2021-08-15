import pygame
from settings import WIN_WIDTH, WIN_HEIGHT,FPS,game_status,singleton_vol_controller,test_transparency,singleton_map_controller,MOUSE
from exit_win.exit_win import ExitWin
from dir_path import *
import os


GameOver_IMG=pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR,"next_level.png")), (WIN_WIDTH, WIN_HEIGHT))


class GameWin:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.next_btn = pygame.Rect(385, 355, 250, 50)  # x, y, width, height
        self.exit_btn=pygame.Rect(452, 415, 120, 50)
        self.buttons=[self.next_btn,
                      self.exit_btn]

        self.sound = pygame.mixer.Sound(os.path.join(SOUND_DIR,"sound.mp3"))
        self.sound.set_volume(singleton_vol_controller.sound_volume)
    
    def draw(self):
        self.win.blit(GameOver_IMG,(0,0))
        # self.win.fill((128,128,128))
        surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        for btn in self.buttons:
            pygame.draw.rect(surface,(255,255,255,128),btn)
        self.win.blit(surface, (0, 0))

    def draw_mouse(self):
        x, y = pygame.mouse.get_pos()
        # pygame.mouse.set_visible(False)
        self.win.blit(MOUSE, (x, y))

    def play_music(self):
        pygame.mixer.music.fadeout(int(1*1000)) 
        pygame.mixer.music.load(os.path.join(SOUND_DIR,"next_level.mp3"))
        pygame.mixer.music.set_volume(singleton_vol_controller.music_volume)
        pygame.mixer.music.play(-1)
        self.sound.set_volume(singleton_vol_controller.sound_volume)

    def run(self):
        clock = pygame.time.Clock()
        
        run=True
        self.play_music()
        while run:
            clock.tick(FPS)
            self.draw()
            self.draw_mouse()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitWin=ExitWin()
                    exitWin.run()
                    if game_status["run"]:
                        run=True
                    else:
                        run=False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()

                    if self.next_btn.collidepoint(x, y):
                        run=False
                        game_status["restart"]=True
                        singleton_map_controller.map_index=singleton_map_controller.next_map_index
                        singleton_map_controller.change_map()
                    
                    if self.exit_btn.collidepoint(x, y):
                        game_status["restart"]=False
                        game_status["go_start_menu"]= True
                        run=False
            pygame.display.update()