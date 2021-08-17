from __future__ import annotations
import pygame
import os
import random
from tower.blue import *
from tower.red import *
from tower.moon import *
from tower.obelisk import *
from settings import singleton_vol_controller,singleton_map_controller,game_status,potion_price
from potion.potionInfo import PotionInfo
from dir_path import *

from gif import *

from victory.victory import Victory


"""This module is import in model.py"""

"""
Here we demonstrate how does the Observer Pattern work
Once the subject updates, if will notify all the observer who has register the subject
"""


class RequestSubject:
    def __init__(self, model):
        self.__observers = []
        self.model = model

    def register(self, observer):
        self.__observers.append(observer)

    def notify(self, user_request:str):
        for o in self.__observers:
            o.update(user_request, self.model)


class EnemyGenerator:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """add new enemy"""
        if user_request == "start new wave":
            if model.enemies.is_empty():
                model.enemies.add(30)
                model.wave += 1


class HealthUp:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """add new enemy"""
        if user_request == "health up" and model.hp < 10:
            model.hp += 1


class AddMoney:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """add money"""
        if user_request == "add money":
            model.money = 99999999999


class KillAll:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """kill all enemies"""
        if user_request == "kill all":
            model.enemies.retreat_all()


class AddTowers:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """Add obelisks tower"""
        if user_request == "add towers":
            for tw in model.towers:
                x, y = tw.rect.center
                if tw.name == "Moon Tower":
                    model.plots.append(Vacancy(x - 18, y))
                elif tw.name == "Obelisk Tower":
                    model.plots.append(Vacancy(x, y + 50))
                else:
                    model.plots.append(Vacancy(x - 20, y + 5))
                model.towers.remove(tw)

            for plot in model.plots:
                x, y = plot.rect.center
                tower_dict = {"moon": MoonTower(x + 18, y),
                              "red fire": RedFireTower(x + 20, y - 5),
                              "blue fire": BlueFireTower(x + 20, y - 5),
                              "obelisk": ObeliskTower(x, y - 50)}
                ran_tower = random.choice(["moon", "red fire", "blue fire", "obelisk"])
                new_tower = tower_dict[ran_tower]
                model.towers.append(new_tower)
                new_tower.level = 6
            model.plots.clear()


class TowerSeller:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """sell tower"""
        if user_request == "sell":
            x, y = model.selected_tower.rect.center
            model.money += model.selected_tower.get_sell_price()
            ####
            if model.selected_tower.name == "Moon Tower":
                model.plots.append(Vacancy(x - 18, y))
            elif model.selected_tower.name == "Obelisk Tower":
                model.plots.append(Vacancy(x, y + 50))
            else:
                model.plots.append(Vacancy(x - 20, y + 5))
            model.towers.remove(model.selected_tower)
            model.selected_tower = None


class TowerDeveloper:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        if user_request == "upgrade" and model.selected_tower.level < 5:
            if model.money >= model.selected_tower.get_upgrade_cost():
                model.money -= model.selected_tower.get_upgrade_cost()
                model.selected_tower.level += 1
            # if the money > upgrade cost of the selected tower , level+1
            # use model.selected_tower to access the selected tower data
            # use model.money to access to money data


class TowerEvolution:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        if user_request == "ultra" and model.selected_tower.level == 5:
            if model.money >= model.selected_tower.get_ultra_cost():
                model.money -= model.selected_tower.get_ultra_cost()
                model.selected_tower.level = 6


class TowerProperties:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        if user_request == "properties":
            model.show_tower_info = True


class TowerFactory:
    def __init__(self, subject:RequestSubject):
        subject.register(self)
        self.tower_name = ["moon", "red fire", "blue fire", "obelisk"]

    def update(self, user_request: str, model):
        """add new tower"""
        for name in self.tower_name:
            if user_request == name:
                if model.selected_plot is not None:
                    x, y = model.selected_plot.rect.center
                    tower_dict = {"moon": MoonTower(x + 18, y),
                                  "red fire": RedFireTower(x + 20, y - 5),
                                  "blue fire": BlueFireTower(x + 20, y - 5),
                                  "obelisk": ObeliskTower(x, y - 50)}
                    new_tower = tower_dict[user_request]
                    if model.money >= new_tower.get_cost():
                        model.money -= new_tower.get_cost()
                        model.towers.append(new_tower)
                        model.plots.remove(model.selected_plot)
                        model.selected_plot = None


class Music:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music on"""
        if user_request == "music":
            pygame.mixer.music.unpause()
            model.sound.play()


class Muse:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music off"""
        if user_request == "mute":
            pygame.mixer.music.pause()
            model.sound.play()


class MinusVolume:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """minusSound"""
        if user_request == "minusSound":
            singleton_vol_controller.minusVol(model.sound,0.05)
            model.sound.play()
        elif user_request == "minusMusic":
            singleton_vol_controller.minusVol(pygame.mixer.music,0.05)
            model.sound.play()


class AddVolume:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """addSound"""
        if user_request == "addSound":
            singleton_vol_controller.addVol(model.sound,0.05)
            model.sound.play()
        elif user_request == "addMusic":
            singleton_vol_controller.addVol(pygame.mixer.music,0.05)
            model.sound.play()


class Back:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """back"""
        if user_request == "back":
            model.back_game=True
            model.sound.play()


class Pause:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """pause"""
        if user_request == "pause":
            model.sound.play()
            model.opt_menu.run()
            model.sound.set_volume(singleton_vol_controller.sound_volume)


class MinusMapIndex:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """minusMapIndex"""
        if user_request == "minusMapIndex":
            model.sound.play()
            singleton_map_controller.map_index-=1
            model.map_preview_img=pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "preview_map_"+str(singleton_map_controller.map_index)+".png")), (500, 230))


class AddMapIndex:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """AddMapIndex"""
        if user_request == "addMapIndex":
            model.sound.play()
            singleton_map_controller.map_index+=1
            model.map_preview_img=pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "preview_map_"+str(singleton_map_controller.map_index)+".png")), (500, 230))


class ShowHint:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """AddMapIndex"""
        if user_request == "hint":
            model.sound.play()
            model.is_show_hint = True


class GoStartMenu:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """Change var game_status["go_start_menu"] in settings.py"""
        if user_request == "goStartMenu":
            model.sound.play()
            game_status["go_start_menu"] = True

class Die:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """deal with event: die by call GameOver.run()"""
        if user_request == "die":
            model.GameOverMenu.run()

class Live:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """deal with event: die by call GameOver.run()"""
        if user_request == "live":
            if singleton_map_controller.next_map_index<=singleton_map_controller.max_map_index:
                model.GameWinMenu.run()
            else:
                victory_menu=Victory()
                victory_menu.run()


class PotionAoe:
    def __init__(self, x: int, y: int):
        self.sprites = [METEOR_0, METEOR_1, METEOR_2, METEOR_3, METEOR_4]
        self.current_sprites = 0
        self.max_current_sprites = 5
        self.update_speed = 0.5
        self.image = self.sprites[self.current_sprites]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.current_sprites += self.update_speed
        if self.current_sprites >= self.max_current_sprites:
            self.current_sprites = 0
        self.image = self.sprites[int(self.current_sprites)]


class PotionKill:
    def __init__(self, x: int, y: int):
        self.sprites = [KILL_1, KILL_2, KILL_3, KILL_4, KILL_5, KILL_6, KILL_7, KILL_8,
                        KILL_9, KILL_10, KILL_11, KILL_12, KILL_13, KILL_14, KILL_15
                        ]
        self.current_sprites = 0
        self.max_current_sprites = 15
        self.update_speed = 0.5
        self.image = self.sprites[self.current_sprites]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.current_sprites += self.update_speed
        if self.current_sprites >= self.max_current_sprites:
            self.current_sprites = 0
        self.image = self.sprites[int(self.current_sprites)]


class PotionSlow:
    def __init__(self, x: int, y: int):
        self.sprites = [SLOW, SLOW, SLOW, SLOW]
        self.current_sprites = 0
        self.max_current_sprites = 4
        self.update_speed = 0.5
        self.image = self.sprites[self.current_sprites]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.current_sprites += self.update_speed
        if self.current_sprites >= self.max_current_sprites:
            self.current_sprites = 0
        self.image = self.sprites[int(self.current_sprites)]


class PotionBoss:
    def __init__(self, x: int, y: int):
        self.sprites = [BEAM_0, BEAM_1, BEAM_2, BEAM_3, BEAM_4, BEAM_5, BEAM_5, BEAM_5]
        self.current_sprites = 0
        self.max_current_sprites = 8
        self.update_speed = 0.5
        self.image = self.sprites[self.current_sprites]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.current_sprites += self.update_speed
        if self.current_sprites >= self.max_current_sprites:
            self.current_sprites = 0
        self.image = self.sprites[int(self.current_sprites)]


class PotionTower:
    def __init__(self, x: int, y: int):
        self.sprites = [CD, CD, CD, CD]
        self.current_sprites = 0
        self.max_current_sprites = 4
        self.update_speed = 0.5
        self.image = self.sprites[self.current_sprites]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.current_sprites += self.update_speed
        if self.current_sprites >= self.max_current_sprites:
            self.current_sprites = 0
        self.image = self.sprites[int(self.current_sprites)]


class Potionfunction:
    def __init__(self, subject: RequestSubject):
        subject.register(self)

        self.particle_list = []
        self.cd = True

    def update(self, user_request: str, model):

        if user_request == "blood_potion":
            if model.hp < model.max_hp and model.money >= potion_price["blood_potion"]:
                model.hp += 1
                model.money -= potion_price["blood_potion"]
                potion_price["blood_potion"] += 1000
                model.sound.play()
                model.hp_sound.play()
        if user_request == "aoe_potion":
            if model.money >= potion_price["aoe_potion"]:
                if len(model.enemies.get()) != 0:
                    for en in model.enemies.get():
                        if en.name == "ultra boss" or en.name == "boss":
                            pass
                        else:
                            x, y = en.rect.center
                            self.aoe_throw(x, y)
                            temp = int(en.max_health * 0.3)
                            en.health -= temp
                            model.meteor_sound.play()

                    model.money -= potion_price["aoe_potion"]
                    potion_price["aoe_potion"] += 2000
                    model.sound.play()

        if user_request == "kill_potion":
            if model.money >= potion_price["kill_potion"] and model.hp > 5:
                if len(model.enemies.get()) != 0:
                    for en in model.enemies.get():
                        if en.name == "ultra boss" or en.name == "boss":
                            break
                        else:
                            x, y = en.rect.center
                            self.kill_throw(x, y + 40)
                            en.health = 0
                            model.evil_sound.play()

                    model.money -= potion_price["kill_potion"]
                    model.hp -= 5
                    potion_price["kill_potion"] += 5000
                    model.sound.play()

        if user_request == "slow_potion":
            if model.money >= potion_price["slow_potion"]:
                if len(model.enemies.get()) != 0:
                    for en in model.enemies.get():
                        x, y = en.rect.center
                        self.slow_throw(x + 10, y + 40)
                        if en.stride > 0.5:
                            en.stride -= 0.5
                        else:
                            en.stride = 0.3

                    model.money -= potion_price["slow_potion"]
                    potion_price["slow_potion"] += 3000
                    model.sound.play()
                    model.debuff_sound.play()
        if user_request == "boss_potion":
            if model.money >= potion_price["boss_potion"]:
                if len(model.enemies.get()) != 0:
                    for en in model.enemies.get():
                        if en.name == "ultra boss" or en.name == "boss":
                            x, y = en.rect.center
                            self.boss_throw(x, y - 200)
                            en.health -= int(en.max_health * 0.5)
                            model.beam_sound.play()
                        else:
                            break
                    model.money -= potion_price["boss_potion"]
                    potion_price["boss_potion"] += 3000
                    model.sound.play()

        if user_request == "tower_potion":
            if model.money >= potion_price["tower_potion"] and self.cd:
                if len(model.towers) != 0:
                    for tw in model.towers:
                        x, y = tw.rect.center
                        self.tower_throw(x + 10, y + 50)
                        tw.cd_max_count -= 5
                        self.cd = False

                    model.money -= potion_price["tower_potion"]
                    model.sound.play()
                    model.buff_sound.play()

    def aoe_throw(self, x: int, y: int):
        self.particle_list.append(PotionAoe(x - 190, y - 200))

    def kill_throw(self, x: int, y: int):
        self.particle_list.append(PotionKill(x, y - 100))

    def slow_throw(self, x: int, y: int):
        self.particle_list.append(PotionSlow(x, y - 100))

    def boss_throw(self, x: int, y: int):
        self.particle_list.append(PotionBoss(x, y - 100))

    def tower_throw(self, x: int, y: int):
        self.particle_list.append(PotionTower(x, y - 100))


class MousePosTracker:
    def __init__(self, subject:RequestSubject):
       subject.register(self)
    
    def update(self, user_request: str, model):
        if user_request == "nothing":
            x,y=pygame.mouse.get_pos()

            btn_list=model.main_menu.buttons
            potion_set={"blood_potion","aoe_potion","kill_potion","slow_potion","boss_potion","tower_potion"}
            for btn in btn_list:
                if btn.name in potion_set:  #this btn is a potion button
                    if btn.clicked(x,y):
                        model.selected_potion_info=PotionInfo(btn)
                        break
                    else:
                        model.selected_potion_info=None
