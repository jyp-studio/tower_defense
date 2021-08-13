import pygame
import os
from settings import WIN_WIDTH,WIN_HEIGHT,FPS,game_status,singleton_vol_controller,test_transparency

class ExitWin:
    def __init__(self,win:pygame.Surface):
        self.bg_win = win
        
        self.menu_img=pygame.transform.scale(pygame.image.load(os.path.join("images", "exit_menu.png")), (350,250))

        self.yes_btn = pygame.Rect(375, 315, 100, 50)
        self.no_btn = pygame.Rect(525, 315, 100, 50)

        self.buttons = [self.yes_btn,
                        self.no_btn]

        self.sound = pygame.mixer.Sound("./sound/sound.mp3")
        self.sound.set_volume(singleton_vol_controller.sound_volume)

    def draw(self):
        self.bg_win.blit(self.menu_img, (325,175))

        surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        for btn in self.buttons:
            pygame.draw.rect(surface,(255,255,255,test_transparency),btn)
        
        self.bg_win.blit(surface,(0,0))
        
    def run(self):
        is_menu_exit=False
        clock = pygame.time.Clock()
        self.draw()
        while not is_menu_exit:
            clock.tick(FPS)
            x, y = pygame.mouse.get_pos()

            for event in pygame.event.get():
                # quit
                if event.type == pygame.QUIT:
                    self.sound.play()
                    game_status["run"] = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.yes_btn.collidepoint(x, y):
                        self.sound.play()
                        game_status["run"]=False
                        is_menu_exit=True
                    if self.no_btn.collidepoint(x, y):
                        self.sound.play()
                        game_status["run"]=True
                        is_menu_exit=True
            pygame.display.update()
