from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.model import GameModel
import pygame
import math
import random
import os
from settings import singleton_map_controller
from gif import *
from color_settings import *

from enemy.fly import *
from enemy.bat import *
from enemy.rock import *
from enemy.skull_yellow import *
from enemy.orc1 import *
from enemy.orc2 import *
from enemy.orc3 import *

pygame.init()


class EnemyGroup:
    def __init__(self):
        self.campaign_count = 0
        self.campaign_max_count = 60   # (unit: frame)
        self.__reserved_members = []
        self.__expedition = []
        self.wave_counter = 0

    def advance(self, model:GameModel):
        # use model.hp and model.money to access the hp and money information
        self.campaign()
        for en in self.__expedition:
            en.move()
            if en.health <= 0:
                if en.is_dead == 0:
                    self.retreat(en)
                    model.money += 15
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
            if singleton_map_controller.curBaseRect.collidepoint(en.rect.centerx, en.rect.centery):
                self.retreat(en)
                model.hp -= 1

    def campaign(self):
        """Enemy go on an expedition."""
        if self.campaign_count > self.campaign_max_count and self.__reserved_members:
            self.__expedition.append(self.__reserved_members.pop())
            self.campaign_count = 0
        else:
            self.campaign_count += 1

    def add(self, num:int):
        """Generate the enemies for next wave"""
        if self.is_empty():
            if self.wave_counter % 7 == 0:
                self.__reserved_members = [EnemyFly() for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 7 == 1:
                self.__reserved_members = [EnemyOrc1() for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 7 == 2:
                self.__reserved_members = [EnemyOrc2() for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 7 == 3:
                self.__reserved_members = [EnemyOrc3() for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 7 == 4:
                self.__reserved_members = [EnemyBat() for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 7 == 5:
                self.__reserved_members = [EnemySKULL1() for _ in range(num)]
                self.wave_counter += 1
            else:
                self.__reserved_members = [EnemyROCK() for _ in range(num)]
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





