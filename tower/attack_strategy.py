from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from enemy.enemies import Enemy
    from tower.towers import Tower
import math
from abc import ABC, abstractmethod


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


class SingleAttack(AttackStrategy):
    """attack an enemy once a time"""
    def attack(self, enemies: list, tower:Tower, cd_count:int)->int:
        if cd_count < tower.cd_max_count:
            return cd_count

        for en in enemies:
            if in_range(en, tower):
                x, y = en.rect.center
                tower.throw(x, y)
                en.health -= tower.damage
                cd_count = 0
                return cd_count
        return cd_count


class SingleSlowAttack(AttackStrategy):
    """attack an enemy once a time"""
    def attack(self, enemies: list, tower:Tower, cd_count:int)->int:
        if cd_count < tower.cd_max_count:
            return cd_count

        for en in enemies:
            if en.name == "goblin":
                previous_stride = 10
            elif en.name == "orc":
                previous_stride = 5
            else:
                previous_stride = 3

            if in_range(en, tower):
                en.health -= tower.damage
                if en.stride > 2:
                    en.stride -= 2
                else:
                    en.stride = 0.5
                cd_count = 0
                return cd_count
            else:
                en.stride = previous_stride

        return cd_count


class AOE(AttackStrategy):
    """attack all the enemy in range once a time"""
    def attack(self, enemies: list, tower:Tower, cd_count:int)->int:
        if cd_count < tower.cd_max_count:
            return cd_count

        for en in enemies:
            if in_range(en, tower):
                en.health -= tower.damage
                cd_count = 0
        return cd_count


class AOESlowAttack(AttackStrategy):
    def attack(self, enemies: list, tower, cd_count)->int:
        if cd_count < tower.cd_max_count:
            return cd_count

        for en in enemies:
            attack_counter = 0
            if in_range(en, tower):
                en.health -= tower.damage
                en.stride *= 0.8
                attack_counter += 1
            else:
                en.stride *= 1.25 ** attack_counter
        cd_count=0
        return cd_count


class Snipe(AttackStrategy):
    def attack(self, enemies: list, tower, cd_count) -> int:
        
        attack_animate_time = 9

        exist_enemy = False
        if cd_count < tower.cd_max_count:
            if cd_count - 1 == tower.cd_max_count-attack_animate_time:
                
                #確認有無敵人在圈內
                for en in enemies:
                    if in_range(en, tower):
                        x, y = en.rect.center
                        tower.throw(x, y - 100)
                        exist_enemy = True
                        break

                if not exist_enemy:
                    cd_count = tower.cd_max_count-attack_animate_time    #讓塔的cd維持在判斷可以開始打雷的時候
        
            return cd_count

        for en in enemies:
            if in_range(en, tower):
                en.health -= tower.damage * 5
                cd_count = 0
                break
        return cd_count



