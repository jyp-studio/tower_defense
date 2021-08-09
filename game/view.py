import pygame
import os
import time
from settings import WIN_WIDTH, WIN_HEIGHT, HP_IMAGE, HP_GRAY_IMAGE, singleton_map_controller
from color_settings import *

start_time = time.time()


class GameView:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.game_time = int(time.time() - start_time)
        self.font = pygame.font.Font(os.path.join("font", "BNMachine.ttf"), 25)
        self.font2 = pygame.font.Font(os.path.join("font", "BNMachine.ttf"), 25)

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
            x, y = tw.rect.center
            if selected_tower.name == "Moon Tower":
                pygame.draw.circle(surface, (255, 0, 0, transparency), (x - 21, y), tw.range)
            elif selected_tower.name == "Obelisk Tower":
                pygame.draw.circle(surface, (255, 0, 0, transparency), (x - 3, y + 40), tw.range)
            else:
                pygame.draw.circle(surface, (255, 0, 0, transparency), (x - 19, y), tw.range)
            self.win.blit(surface, (0, 0))

    def draw_menu(self, menu):
        self.win.blit(menu.image, menu.rect)
        for btn in menu.buttons:
            self.win.blit(btn.image, btn.rect)

    def draw_properties(self, selected_tower):
        if selected_tower is not None:
            surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
            transparency = 150
            pygame.draw.rect(surface, (0, 0, 0, transparency), [162, 150, 700, 400])
            self.win.blit(surface, (0, 0))
            font = pygame.font.Font(os.path.join("font", "CESCOBold.ttf"), 50)
            font1 = pygame.font.Font(os.path.join("font", "CESCOBold.ttf"), 25)
            name = f"{selected_tower.name}"
            intro = f"{selected_tower.intro}"
            intro1 = f"{selected_tower.intro1}"
            intro2 = f"{selected_tower.intro2}"
            if selected_tower.level == 6:
                level = f"Level:  Max"
            else:
                level = f"Level:  {selected_tower.level}"
            range = f"Attack Range:  {selected_tower.range}"
            damage = f"Damage:  {selected_tower.damage}"
            cd = f"Cool Down Time:  {selected_tower.cd_max_count}"
            attack_strategy = f"Attack Strategy:  {selected_tower.attack_strategy_name}"
            sell_price = f"Sell Price:  {selected_tower.value[selected_tower.level]}"

            name_text = font.render(name, True, (255, 255, 255))
            self.win.blit(name_text, (180, 170))
            intro_text = font1.render(intro, True, (255, 255, 255))
            self.win.blit(intro_text, (180, 170 + 50))
            intro1_text = font1.render(intro1, True, (255, 255, 255))
            self.win.blit(intro1_text, (180, 170 + 75))
            intro2_text = font1.render(intro2, True, (255, 255, 255))
            self.win.blit(intro2_text, (180, 170 + 100))
            level_text = font1.render(level, True, (255, 255, 255))
            self.win.blit(level_text, (180, 170 + 130))
            range_text = font1.render(range, True, (255, 255, 255))
            self.win.blit(range_text, (180, 170 + 160))
            damage_text = font1.render(damage, True, (255, 255, 255))
            self.win.blit(damage_text, (180, 170 + 190))
            cd_text = font1.render(cd, True, (255, 255, 255))
            self.win.blit(cd_text, (180, 170 + 220))
            attack_strategy_text = font1.render(attack_strategy, True, (255, 255, 255))
            self.win.blit(attack_strategy_text, (180, 170 + 250))
            sell_price_text = font1.render(sell_price, True, (255, 255, 255))
            self.win.blit(sell_price_text, (180, 170 + 280))

    def draw_plots(self, plots):
        for pt in plots:
            self.win.blit(pt.image, pt.rect)

    def draw_money(self, money: int):
        """ (Q2.1)render the money"""
        text = self.font2.render(f"$: {money}", True, (255, 255, 255))
        self.win.blit(text, (5, 40))

    def draw_wave(self, wave: int):
        """(Q2.2)render the wave"""
        text = self.font2.render(f"Wave: {wave}", True, (255, 255, 255))
        self.win.blit(text, (5, 10))

    def draw_hp(self, lives):
        # draw_lives
        hp_rect = HP_IMAGE.get_rect()
        for i in range(10):
            self.win.blit(HP_GRAY_IMAGE, (WIN_WIDTH // 2 - (hp_rect.w + 5) * (2.5 - i % 5), hp_rect.h * (i // 5) + 8))
        for i in range(lives):
            self.win.blit(HP_IMAGE, (WIN_WIDTH // 2 - (hp_rect.w + 5) * (2.5 - i % 5), hp_rect.h * (i // 5) + 8))

    def draw_UI(self, UI):
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
        text = self.font2.render(f"{y}/{m}/{d}", True, WHITE)
        self.win.blit(text, (220, 10))
        text = self.font2.render(f"{h}:{min}:{sec}", True, WHITE)
        self.win.blit(text, (220, 40))

    def draw_game_time(self):
        minute = self.game_time // 60
        second = str(self.game_time % 60).zfill(2)
        time_text = self.font.render(f"{minute}:{second}", True, WHITE)
        self.win.blit(time_text, (700, 15))


