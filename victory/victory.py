import pygame
import os
from settings import WIN_WIDTH, WIN_HEIGHT,FPS,game_status,singleton_vol_controller,test_transparency,singleton_map_controller,MOUSE
from exit_win.exit_win import ExitWin

VIC_IMG=pygame.transform.scale(pygame.image.load("images/victory.png"), (WIN_WIDTH, WIN_HEIGHT))

class Victory:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.reward_btn = pygame.Rect(385, 355, 250, 50)  # x, y, width, height
        self.exit_btn=pygame.Rect(452, 415, 120, 50)
        self.buttons=[self.reward_btn,
                      self.exit_btn]

        self.sound = pygame.mixer.Sound("./sound/sound.mp3")
        self.sound.set_volume(singleton_vol_controller.sound_volume)

        self.has_draw_reward=False
        self.font = pygame.font.Font(os.path.join("font", "CESCOBold.ttf"), 30)
    
    def draw(self):
        self.win.blit(VIC_IMG,(0,0))
        surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        for btn in self.buttons:
            pygame.draw.rect(surface,(255,255,255,128),btn)
        self.win.blit(surface, (0, 0))

        x, y = pygame.mouse.get_pos()
        self.win.blit(MOUSE, (x, y))

        if self.has_draw_reward:
            self.draw_reward()

    def draw_reward(self):
        surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        sheet= pygame.Rect(160, 100, 700, 400)
        pygame.draw.rect(surface,(128,128,128,128),sheet)

        text = self.font.render("There are some hotkey we used in development.", True, (255, 255, 255))
        surface.blit(text, (170,150))
        text=self.font.render("Button tab is used to get lots of money.",True, (255, 255, 255))
        surface.blit(text, (170,200))
        text=self.font.render("Button k is used to kill all enemies in a wave.",True, (255, 255, 255))
        surface.blit(text, (170,250))
        text=self.font.render("Button t is used to build towers randomly.",True, (255, 255, 255))
        surface.blit(text, (170,300))
        text=self.font.render("Button h is used to recover 1 HP once.",True, (255, 255, 255))
        surface.blit(text, (170,350))

        self.win.blit(surface, (0,0))


    def play_music(self):
        pygame.mixer.music.fadeout(int(1*1000)) 
        pygame.mixer.music.load("./sound/victory.mp3")
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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitWin=ExitWin(self.win)
                    exitWin.run()
                    if game_status["run"]:
                        run=True
                    else:
                        run=False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.has_draw_reward=False

                    if self.reward_btn.collidepoint(x, y):
                        self.has_draw_reward=True
                    
                    if self.exit_btn.collidepoint(x, y):
                        game_status["go_start_menu"]= True
                        run=False

            pygame.display.update()