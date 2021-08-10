import pygame
from settings import WIN_WIDTH, WIN_HEIGHT,FPS,game_status,singleton_vol_controller
from exit_win.exit_win import ExitWin

GameOver_IMG=pygame.transform.scale(pygame.image.load("images/game_over.png"), (WIN_WIDTH, WIN_HEIGHT))

class GameOver:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.restart_btn = pygame.Rect(430, 365, 170, 50)  # x, y, width, height
        self.exit_btn=pygame.Rect(430, 435, 170, 50)
        self.buttons=[self.restart_btn,
                      self.exit_btn]

        self.sound = pygame.mixer.Sound("./sound/sound.mp3")
        self.sound.set_volume(singleton_vol_controller.sound_volume)
    
    def draw(self):
        self.win.blit(GameOver_IMG,(0,0))
        surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        for btn in self.buttons:
            pygame.draw.rect(surface,(255,255,255,128),btn)
        self.win.blit(surface, (0, 0))

    def run(self):
        clock = pygame.time.Clock()
        
        run=True
        while run:
            clock.tick(FPS)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run=False
                    exitWin=ExitWin(self.win)
                    exitWin.run()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()

                    if self.restart_btn.collidepoint(x, y):
                        run=False
                        game_status["restart"]=True
                    
                    if self.exit_btn.collidepoint(x, y):
                        exitWin=ExitWin(self.win)
                        exitWin.run()
                        if game_status["run"]:
                            game_status["restart"]=False
                        else:
                            run=False
            pygame.display.update()
