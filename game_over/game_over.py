import pygame
from settings import WIN_WIDTH, WIN_HEIGHT,FPS,game_status,singleton_vol_controller,test_transparency
from exit_win.exit_win import ExitWin

GameOver_IMG=pygame.transform.scale(pygame.image.load("images/game_over.png"), (WIN_WIDTH, WIN_HEIGHT))

class GameOver:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.restart_btn = pygame.Rect(430, 355, 170, 50)  # x, y, width, height
        self.exit_btn=pygame.Rect(430, 425, 170, 50)
        self.buttons=[self.restart_btn,
                      self.exit_btn]

        self.sound = pygame.mixer.Sound("./sound/sound.mp3")
        self.sound.set_volume(singleton_vol_controller.sound_volume)
    
    def draw(self):
        self.win.blit(GameOver_IMG,(0,0))
        surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        for btn in self.buttons:
            pygame.draw.rect(surface,(255,255,255,test_transparency),btn)
        self.win.blit(surface, (0, 0))

    def play_music(self):
        pygame.mixer.music.fadeout(int(1*1000)) 
        pygame.mixer.music.load("./sound/gameover.mp3")
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
                    run=False
                    exitWin=ExitWin(self.win)
                    exitWin.run()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()

                    if self.restart_btn.collidepoint(x, y):
                        run=False
                        game_status["restart"]=True
                    
                    if self.exit_btn.collidepoint(x, y):
                        game_status["restart"]=False
                        game_status["go_start_menu"]= True
                        run=False
            pygame.display.update()