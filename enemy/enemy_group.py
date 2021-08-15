from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.model import GameModel
import pygame
import math
import random
import os
from settings import singleton_map_controller,singleton_vol_controller
from gif import *
from color_settings import *
from dir_path import *
from enemy.lv_1 import *
from enemy.lv_2 import *
from enemy.lv_3 import *
from enemy.lv_4 import *
from enemy.lv_5 import *

pygame.init()
hit_base_sound =pygame.mixer.Sound(os.path.join(SOUND_DIR,"enemy_hit_base.mp3"))

class EnemyGroup:
    def __init__(self, level: int):
        self.campaign_count = 0
        self.campaign_max_count = 15   # (unit: frame)
        self.__reserved_members = []
        self.__expedition = []
        self.wave_counter = level

    def advance(self, model: GameModel):
        # use model.hp and model.money to access the hp and money information
        self.campaign()
        for en in self.__expedition:
            en.move()
            if en.name == "ultra boss":
                if en.skill():
                    ran_en = random.choice([EnemyROCK(), EnemyKnight()])
                    self.__expedition.append(ran_en)
            if en.health <= 0:
                if en.is_dead == 0:
                    self.retreat(en)
                    if en.name == "boss":
                        model.money += 1000
                    elif en.name == "skull":
                        model.money += 500
                    elif en.name == "orc" or en.name == "fly":
                        model.money += 200
                    else:
                        model.money += 30
                else:
                    if en.is_dead == 5:
                        en.is_dead = 4
                        en.sprites.clear()
                        en.sprites.append(GREEN_SKULL_0)
                        en.sprites.append(GREEN_SKULL_1)
                        en.sprites.append(GREEN_SKULL_2)
                        en.sprites.append(GREEN_SKULL_3)
                        en.sprites.append(GREEN_SKULL_4)
                        en.sprites.append(GREEN_SKULL_5)
                        en.sprites.append(GREEN_SKULL_6)
                        en.sprites.append(GREEN_SKULL_7)
                        en.health = 500
                        en.max_health = 500
                    elif en.is_dead == 4:
                        en.is_dead = 3
                        en.sprites.clear()
                        en.sprites.append(BLUE_SKULL_0)
                        en.sprites.append(BLUE_SKULL_1)
                        en.sprites.append(BLUE_SKULL_2)
                        en.sprites.append(BLUE_SKULL_3)
                        en.sprites.append(BLUE_SKULL_4)
                        en.sprites.append(BLUE_SKULL_5)
                        en.sprites.append(BLUE_SKULL_6)
                        en.sprites.append(BLUE_SKULL_7)
                        en.health = 500
                        en.max_health = 500
                    elif en.is_dead == 3:
                        en.is_dead = 2
                        en.sprites.clear()
                        en.sprites.append(PURPLE_SKULL_0)
                        en.sprites.append(PURPLE_SKULL_1)
                        en.sprites.append(PURPLE_SKULL_2)
                        en.sprites.append(PURPLE_SKULL_3)
                        en.sprites.append(PURPLE_SKULL_4)
                        en.sprites.append(PURPLE_SKULL_5)
                        en.sprites.append(PURPLE_SKULL_6)
                        en.sprites.append(PURPLE_SKULL_7)
                        en.health = 500
                        en.max_health = 500
                    elif en.is_dead == 2:
                        en.is_dead = 1
                        en.sprites.clear()
                        en.sprites.append(RED_SKULL_0)
                        en.sprites.append(RED_SKULL_1)
                        en.sprites.append(RED_SKULL_2)
                        en.sprites.append(RED_SKULL_3)
                        en.sprites.append(RED_SKULL_4)
                        en.sprites.append(RED_SKULL_5)
                        en.sprites.append(RED_SKULL_6)
                        en.sprites.append(RED_SKULL_7)
                        en.health = 500
                        en.max_health = 500
                    else:
                        en.is_dead = 0
                        en.sprites.clear()
                        en.sprites.append(PURPLE_SKULL_0)
                        en.sprites.append(RED_SKULL_1)
                        en.sprites.append(YELLOW_SKULL_2)
                        en.sprites.append(GREEN_SKULL_3)
                        en.sprites.append(BLUE_SKULL_4)
                        en.sprites.append(PURPLE_SKULL_5)
                        en.sprites.append(RED_SKULL_6)
                        en.sprites.append(YELLOW_SKULL_7)
                        en.health = 2000
                        en.max_health = 2000

            # delete the object when it reach the base
            elif singleton_map_controller.curBaseRect.collidepoint(en.rect.centerx, en.rect.centery):
                self.retreat(en)
                if en.name == "ultra boss":
                    model.hp -= 10
                elif en.name == "boss":
                    model.hp -= 5
                else:
                    model.hp -= 1
                hit_base_sound.set_volume(0.5)
                hit_base_sound.play()

    def campaign(self):
        """Enemy go on an expedition."""
        if self.campaign_count > self.campaign_max_count and self.__reserved_members:
            self.__expedition.append(self.__reserved_members.pop())
            self.campaign_count = 0
        else:
            self.campaign_count += 1

    def add(self, num: int):
        """Generate the enemies for next wave"""
        if self.is_empty():
            if self.wave_counter % 13 == 0:
                self.__reserved_members = [EnemyFly() for _ in range(num - 20)]
                self.wave_counter += 1
            elif self.wave_counter % 13 == 1:
                self.__reserved_members = [EnemyWorm() for _ in range(num - 10)]
                self.wave_counter += 1
            elif self.wave_counter % 13 == 2:
                self.__reserved_members = [EnemyBlackBat(), EnemyBlackBat(), EnemyBlackBat(), EnemyBlackBat(), EnemyBlackBat(),
                                           EnemyWorm(), EnemyWorm(), EnemyWorm(), EnemyWorm(), EnemyWorm(), EnemyWorm(),
                                           EnemyWorm(), EnemyWorm(), EnemyWorm(), EnemyWorm(), EnemyWorm(), EnemyWorm(),
                                           EnemyFly(), EnemyFly(), EnemyFly(), EnemyFly(), EnemyFly(), EnemyFly(), EnemyFly(),
                                           EnemyFly(), EnemyFly(), EnemyFly(), EnemyFly(), EnemyFly(), EnemyFly()
                                           ]
                self.wave_counter += 1
            elif self.wave_counter % 13 == 3:
                self.__reserved_members = [EnemyOrc1() for _ in range(num - 10)]
                self.wave_counter += 1
            elif self.wave_counter % 13 == 4:
                self.__reserved_members = [EnemyOrc2() for _ in range(num - 20)]
                self.wave_counter += 1
            elif self.wave_counter % 13 == 5:
                self.__reserved_members = [EnemyOrc3(), EnemyOrc3(), EnemyOrc3(), EnemyOrc3(), EnemyOrc3(),
                                           EnemyOrc2(), EnemyOrc2(), EnemyOrc2(), EnemyOrc2(), EnemyOrc2(),
                                           EnemyOrc2(), EnemyOrc2(), EnemyOrc2(), EnemyOrc2(), EnemyOrc2(),
                                           EnemyOrc1(), EnemyOrc1(), EnemyOrc1(), EnemyOrc1(), EnemyOrc1()
                                           ]
                self.wave_counter += 1
            elif self.wave_counter % 13 == 6:
                self.__reserved_members = [EnemyBat() for _ in range(num - 10)]
                self.wave_counter += 1
            elif self.wave_counter % 13 == 7:
                self.__reserved_members = [EnemyRedBat() for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 13 == 8:
                self.__reserved_members = [EnemyGhost(), EnemyGhost(), EnemyGhost(), EnemyGhost(), EnemyGhost(),
                                           EnemyRedBat(), EnemyRedBat(), EnemyRedBat(), EnemyRedBat(), EnemyRedBat(),
                                           EnemyRedBat(), EnemyRedBat(), EnemyRedBat(), EnemyRedBat(), EnemyRedBat(),
                                           EnemyBat(), EnemyBat(), EnemyBat(), EnemyBat(), EnemyBat(),
                                           ]
                self.wave_counter += 1
            elif self.wave_counter % 13 == 9:
                self.__reserved_members = [EnemySKULL1() for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 13 == 10:
                self.__reserved_members = [EnemySKULL3() for _ in range(num - 10)]
                self.wave_counter += 1
            elif self.wave_counter % 13 == 11:
                self.__reserved_members = [EnemyEvil(), EnemyEvil(), EnemyEvil(), EnemySKULL6(), EnemySKULL6(),
                                           EnemySKULL6(), EnemySKULL6(), EnemySKULL6(), EnemySKULL6(), EnemySKULL6()]
                self.wave_counter += 1
            else:
                self.__reserved_members = [EnemyMage()]
                self.wave_counter = 0

    def get(self) -> list:
        """Get the enemy list"""
        return self.__expedition

    def is_empty(self) -> bool:
        """Return whether the enemy is empty (so that we can move on to next wave)"""
        return False if self.__reserved_members or self.__expedition else True

    def retreat(self, enemy: Enemy):
        """Remove the enemy from the expedition"""
        self.__expedition.remove(enemy)

    def retreat_all(self):
        self.__expedition = []
        self.__reserved_members = []





