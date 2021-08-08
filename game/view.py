import pygame
import time
from settings import WIN_WIDTH, WIN_HEIGHT, HP_IMAGE, HP_GRAY_IMAGE, singleton_map_controller
from color_settings import *


class GameView:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font = pygame.font.SysFont("comicsans", 30)

    def draw_bg(self):
        self.win.blit(singleton_map_controller.curMap, (0, 0))

    def draw_enemies(self, enemies):
        for en in enemies.get():
            self.win.blit(en.image, en.rect)
            # draw health bar
            bar_width = en.rect.w * (en.health / en.max_health)
            max_bar_width = en.rect.w
            bar_height = 5
            pygame.draw.rect(self.win, RED, [en.rect.x, en.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(self.win, GREEN, [en.rect.x, en.rect.y - 10, bar_width, bar_height])

    def draw_towers(self, towers):
        # draw tower
        for tw in towers:
            self.win.blit(tw.image, tw.rect)

    def draw_range(self, selected_tower):
        # draw tower range
        if selected_tower is not None:
            tw = selected_tower
            # create a special surface that is able to render semi-transparent image
            surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
            transparency = 120
            pygame.draw.circle(surface, (128, 128, 128, transparency), tw.rect.center, tw.range)
            self.win.blit(surface, (0, 0))

    def draw_menu(self, menu):
        self.win.blit(menu.image, menu.rect)

    def draw_plots(self, plots):
        for pt in plots:
            self.win.blit(pt.image, pt.rect)

    def draw_money(self, money: int):
        """ (Q2.1)render the money"""
        text = self.font.render(f"$: {money}", True, (255, 255, 255))
        self.win.blit(text, (5, 45))

    def draw_wave(self, wave: int):
        """(Q2.2)render the wave"""
        text = self.font.render(f"Wave: {wave}", True, (255, 255, 255))
        self.win.blit(text, (5, 15))

    def draw_hp(self, lives):
        # draw_lives
        hp_rect = HP_IMAGE.get_rect()
        for i in range(10):
            self.win.blit(HP_GRAY_IMAGE, (WIN_WIDTH // 2 - hp_rect.w * (2.5 - i % 5), hp_rect.h * (i // 5)))
        for i in range(lives):
            self.win.blit(HP_IMAGE, (WIN_WIDTH // 2 - hp_rect.w * (2.5 - i % 5), hp_rect.h * (i // 5)))
    
    def draw_UI(self,UI):
        self.win.blit(UI.frame,(0,0))
    
    def draw_btn(self,buttons):
        for btn in buttons:
            self.win.blit(btn.image, btn.rect)
            # pygame.draw.rect(self.win, (128, 128, 128),btn.rect)

    def draw_time(self):
        now=time.localtime(time.time())
        y=str(now.tm_year).zfill(4)
        m=str(now.tm_mon).zfill(2)
        d=str(now.tm_mday).zfill(2)
        h=str(now.tm_hour).zfill(2)
        min=str(now.tm_min).zfill(2)
        sec=str(now.tm_sec).zfill(2)
        text = self.font.render(f"{y}/{m}/{d}", True, (255, 255, 255))
        self.win.blit(text, (200, 15))
        text = self.font.render(f"{h}:{min}:{sec}", True, (255, 255, 255))
        self.win.blit(text, (200, 45))


