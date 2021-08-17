from __future__ import annotations

import random
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from enemy.enemies import Enemy
    from tower.towers import Tower

import math
import pygame
import os
from abc import ABC, abstractmethod
from settings import singleton_vol_controller
from dir_path import *

pygame.mixer.init()

def in_range(enemy:Enemy, tower:Tower)->bool:
    x1, y1 = enemy.rect.center
    x2, y2 = tower.rect.center
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance <= tower.range:
        return True
    return False


"""
syntax: attack_strategy().attack(tower, enemy_group, cd_count)
It's something like you hire a "Strategist" to decide how to attack the enemy
You can add other ways of attack just by expand this module
"""


class AttackStrategy(ABC):
    """Abstract class of attack method"""
    @ abstractmethod
    def attack(self, enemies, tower, cd_count):
        return "Please implement this method"


# red flame: single
class RedAttack(AttackStrategy):
    """attack an enemy once a time"""
    attack_sound =pygame.mixer.Sound(os.path.join(SOUND_DIR,"flame.mp3"))

    def attack(self, enemies: list, tower:Tower, cd_count:int)->int:
        self.attack_sound.set_volume(singleton_vol_controller.sound_volume)
        attack_animate_time = 10 #等同各攻擊動畫的max_current_sprites+1

        exist_enemy = False
        if cd_count < tower.cd_max_count:
            if cd_count - 1 == tower.cd_max_count-attack_animate_time:
                
                #確認有無敵人在圈內
                for en in enemies:
                    if in_range(en, tower):
                        if en.name == "fly" or en.name == "ghost":#非飛行敵人才有攻擊動畫
                            break
                        else:
                            x, y = en.rect.center
                            tower.throw(x, y - 100)
                            exist_enemy = True
                            break

                if not exist_enemy:
                    cd_count = tower.cd_max_count-attack_animate_time    #讓塔的cd維持在判斷可以開始攻擊動畫的時候
        
            return cd_count

        else:
            self.attack_sound.play()
            for en in enemies:
                if in_range(en, tower):
                    if en.name == "fly" or en.name == "ghost":    #非飛行敵人才有攻擊
                        break
                    else:
                        en.health -= tower.damage
                        break
            cd_count = 0
            return cd_count


# blue flame: AOE
class BlueAttack(AttackStrategy):
    def __init__(self):
        self.count = 0
        self.count_max = 9
    """attack all the enemy in range once a time"""

    attack_sound =pygame.mixer.Sound(os.path.join(SOUND_DIR,"blue_flame.mp3"))

    def attack(self, enemies: list, tower:Tower, cd_count:int)->int:
        self.attack_sound.set_volume(singleton_vol_controller.sound_volume)
        attack_animate_time = 10 #等同各攻擊動畫的max_current_sprites+1

        exist_enemy = False
        if cd_count < tower.cd_max_count:
            if cd_count - 1 == tower.cd_max_count-attack_animate_time:

                self.count = 0
                #確認有無敵人在圈內
                for en in enemies:
                    if in_range(en, tower) and self.count <= self.count_max:
                        if en.name == "fly" or en.name == "ghost":
                            break
                        else:
                            x, y = en.rect.center
                            tower.throw(x, y - 100)
                            self.count += 1
                            exist_enemy = True

                if not exist_enemy:
                    cd_count = tower.cd_max_count-attack_animate_time    #讓塔的cd維持在判斷可以開始攻擊動畫的時候
        
            return cd_count

        else:
            self.attack_sound.play()
            self.count = 0
            for en in enemies:
                if in_range(en, tower) and self.count <= self.count_max:
                    if en.name == "fly" or en.name == "ghost":
                        pass
                    elif en.name == "skull":
                        en.health -= tower.damage*2
                    else:
                        en.health -= tower.damage
                        
            cd_count = 0
            return cd_count


# moon: AOE slow
class MoonAttack(AttackStrategy):

    attack_sound =pygame.mixer.Sound(os.path.join(SOUND_DIR,"magic.mp3"))

    def attack(self, enemies: list, tower, cd_count)->int:
        self.attack_sound.set_volume(singleton_vol_controller.sound_volume)
        attack_animate_time = 4 #等同各攻擊動畫的max_current_sprites+1

        exist_enemy = False
        self.count = 0
        if cd_count < tower.cd_max_count:
            if cd_count - 1 == tower.cd_max_count-attack_animate_time:
                
                #確認有無敵人在圈內
                for en in enemies:
                    if in_range(en, tower):
                        x, y = en.rect.center
                        tower.throw(x, y - 100)
                        exist_enemy = True

                if not exist_enemy:
                    cd_count = tower.cd_max_count-attack_animate_time    #讓塔的cd維持在判斷可以開始攻擊動畫的時候
        
            return cd_count

        else:
            self.attack_sound.play()
            for en in enemies:
                attack_counter = 0
                if in_range(en, tower):

                    if en.name == "orc":    #對orc加傷
                        en.health -= tower.damage*2
                    elif en.name == "shield":
                        en.health -= tower.damage * 0.8
                    elif en.name == "ghost":
                        damage = random.choice([tower.damage * 3, 0])
                        en.health -= damage
                        if damage == 0:
                            x, y = en.rect.center
                            tower.miss_throw(x, y)
                    else:
                        en.health -= tower.damage
    
                    # en.stride *= 0.8
                    # attack_counter += 1
                else:
                    pass
                    # en.stride *= 1.25 ** attack_counter
            cd_count = 0
            return cd_count


# obelisk: snipe all
class ObeliskSnipe(AttackStrategy):
    def __init__(self):
        self.count = 0
        self.count_max = 4
    attack_sound =pygame.mixer.Sound(os.path.join(SOUND_DIR,"lightning.mp3"))

    def attack(self, enemies: list, tower, cd_count) -> int:
        self.attack_sound.set_volume(singleton_vol_controller.sound_volume)
        attack_animate_time = 14 #等同各攻擊動畫的max_current_sprites+1

        exist_enemy = False
        self.count = 0
        if cd_count < tower.cd_max_count:
            if cd_count - 1 == tower.cd_max_count-attack_animate_time:
                
                #確認有無敵人在圈內
                for en in enemies:
                    if in_range(en, tower) and self.count <= self.count_max:
                        x, y = en.rect.center
                        tower.throw(x, y)
                        exist_enemy = True
                        self.count += 1

                if not exist_enemy:
                    cd_count = tower.cd_max_count-attack_animate_time    #讓塔的cd維持在判斷可以開始打雷的時候
        
            return cd_count

        else:
            self.attack_sound.play()
            self.count = 0
            for en in enemies:
                if in_range(en, tower):
                    if en.name == "boss":   #對boss傷害
                        en.health -= tower.damage * 5
                    elif en.name == "shield":
                        en.health -= tower.damage * 0.8 * 3
                    elif en.name == "ultra boss":
                        damage = random.choice([0, 5, 6, 7, 7, 7, 8, 8, 9, 10])
                        en.health -= damage * tower.damage
                        if damage == 0:
                            x, y = en.rect.center
                            tower.miss_throw(x, y)
                    elif en.name == "ghost":
                        damage = random.choice([tower.damage * 3, 0])
                        en.health -= damage
                        if damage == 0:
                            x, y = en.rect.center
                            tower.miss_throw(x, y)
                    else:   #對普通怪傷害
                        en.health -= tower.damage * 3
    
            cd_count = 0
            return cd_count



