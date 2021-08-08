import math
from abc import ABC, abstractmethod


def in_range(enemy, tower):
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
    def attack(self, enemies: list, tower, cd_count):
        for en in enemies:
            if in_range(en, tower):
                en.health -= tower.damage
                cd_count = 0
                return cd_count
        return cd_count


class SingleSlowAttack(AttackStrategy):
    """attack an enemy once a time"""
    def attack(self, enemies: list, tower, cd_count):
        for en in enemies:
            if en.name == "goblin":
                previous_stride = 10
            elif en.name == "orc":
                previous_stride = 5
            else:
                previous_stride = 3
            if in_range(en, tower):
                en.health -= tower.damage
                if en.stride > 4:
                    en.stride -= 4
                else:
                    en.stride = 1
                cd_count = 0
                return cd_count
            else:
                en.stride = previous_stride
        return cd_count


class AOE(AttackStrategy):
    """attack all the enemy in range once a time"""
    def attack(self, enemies: list, tower, cd_count):
        for en in enemies:
            if in_range(en, tower):
                en.health -= tower.damage
                cd_count = 0
        return cd_count


class AOESlowAttack(AttackStrategy):
    """attack an enemy once a time"""
    def attack(self, enemies: list, tower, cd_count):
        for en in enemies:
            if en.name == "goblin":
                previous_stride = 10
            elif en.name == "orc":
                previous_stride = 5
            else:
                previous_stride = 3
            if in_range(en, tower):
                en.health -= tower.damage
                if en.stride > 4:
                    en.stride -= 4
                else:
                    en.stride = 1
                cd_count = 0
            else:
                en.stride = previous_stride
        return cd_count


class Snipe(AttackStrategy):
    """eliminate an enemy all in once"""
    def attack(self, enemies: list, tower, cd_count):
        for en in enemies:
            if in_range(en, tower):
                en.health -= tower.damage * 2
                cd_count = 0
                return cd_count
        return cd_count


class SnipeAll(AttackStrategy):
    """eliminate an enemy all in once"""
    def attack(self, enemies: list, tower, cd_count):
        for en in enemies:
            if in_range(en, tower):
                en.health -= tower.damage * 2
                cd_count = 0
        return cd_count




