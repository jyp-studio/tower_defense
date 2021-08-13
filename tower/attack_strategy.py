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


# red flame: single
class RedAttack(AttackStrategy):
    """attack an enemy once a time"""

    def attack(self, enemies: list, tower:Tower, cd_count:int)->int:
        attack_animate_time = 10 #等同各攻擊動畫的max_current_sprites+1

        exist_enemy = False
        if cd_count < tower.cd_max_count:
            if cd_count - 1 == tower.cd_max_count-attack_animate_time:
                
                #確認有無敵人在圈內
                for en in enemies:
                    if in_range(en, tower):
                        if en.name != "fly":    #非飛行敵人才有攻擊動畫
                            x, y = en.rect.center
                            tower.throw(x, y - 100)
                            exist_enemy = True
                            break

                if not exist_enemy:
                    cd_count = tower.cd_max_count-attack_animate_time    #讓塔的cd維持在判斷可以開始攻擊動畫的時候
        
            return cd_count

        else:
            for en in enemies:
                if in_range(en, tower):
                    if en.name != "fly":    #非飛行敵人才有攻擊
                        en.health -= tower.damage
                        break
            cd_count = 0
            return cd_count


# blue flame: AOE
class BlueAttack(AttackStrategy):
    """attack all the enemy in range once a time"""

    # attack_anime=BlueFlame(0,0)

    def attack(self, enemies: list, tower:Tower, cd_count:int)->int:
        attack_animate_time = 10 #等同各攻擊動畫的max_current_sprites+1

        exist_enemy = False
        if cd_count < tower.cd_max_count:
            if cd_count - 1 == tower.cd_max_count-attack_animate_time:
                
                #確認有無敵人在圈內
                for en in enemies:
                    if in_range(en, tower):
                        if en.name != "fly":
                            x, y = en.rect.center
                            tower.throw(x, y - 100)
                            exist_enemy = True

                if not exist_enemy:
                    cd_count = tower.cd_max_count-attack_animate_time    #讓塔的cd維持在判斷可以開始攻擊動畫的時候
        
            return cd_count

        else:
            for en in enemies:
                if in_range(en, tower):
                    if en.name == "fly":
                        pass
                    elif en.name == "skull":
                        en.health -= tower.damage*2
                    else:
                        en.health -= tower.damage
            cd_count = 0
            return cd_count


# moon: AOE slow
class MoonAttack(AttackStrategy):

    # attack_anime=Magic(0,0)

    def attack(self, enemies: list, tower, cd_count)->int:
        attack_animate_time = 4 #等同各攻擊動畫的max_current_sprites+1

        exist_enemy = False
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
            for en in enemies:
                attack_counter = 0
                if in_range(en, tower):

                    if en.name == "orc":    #對orc加傷
                        en.health -= tower.damage*2
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

    # attack_anime=Lightning(0,0)

    def attack(self, enemies: list, tower, cd_count) -> int:
        
        attack_animate_time = 14 #等同各攻擊動畫的max_current_sprites+1

        exist_enemy = False
        if cd_count < tower.cd_max_count:
            if cd_count - 1 == tower.cd_max_count-attack_animate_time:
                
                #確認有無敵人在圈內
                for en in enemies:
                    if in_range(en, tower):
                        x, y = en.rect.center
                        tower.throw(x, y)
                        exist_enemy = True

                if not exist_enemy:
                    cd_count = tower.cd_max_count-attack_animate_time    #讓塔的cd維持在判斷可以開始打雷的時候
        
            return cd_count

        else:
            for en in enemies:
                if in_range(en, tower):
                    if en.name == "boss":   #對boss傷害
                        if en.health >= en.max_health * 0.05:   #5%以上扣20%，以下秒殺
                            en.health -= en.health * 0.05
                        else:
                            en.health = 0
                    else:   #對普通怪傷害
                        en.health -= tower.damage * 3
            cd_count = 0
            return cd_count



