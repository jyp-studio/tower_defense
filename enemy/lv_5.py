from __future__ import annotations
from enemy.enemies import *

pygame.init()


class EnemyROCK(Enemy):
    def __init__(self):
        super().__init__(ROCK_0)
        self.name = "boss"
        self.max_current_sprites = 2
        self.update_speed = 0.25
        self.sprites.append(ROCK_1)

        self.stride = 2
        self.max_stride = 2
        self.health = 2000
        self.max_health = 2000
        self.is_dead = 0


class EnemyKnight(Enemy):
    def __init__(self):
        super().__init__(KNIGHT_0)
        self.name = "boss"
        self.max_current_sprites = 7
        self.update_speed = 0.5
        self.sprites.append(KNIGHT_1)
        self.sprites.append(KNIGHT_2)
        self.sprites.append(KNIGHT_3)
        self.sprites.append(KNIGHT_4)
        self.sprites.append(KNIGHT_5)
        self.sprites.append(KNIGHT_6)
        self.sprites.append(KNIGHT_7)

        self.stride = 5
        self.max_stride = 5
        self.health = 1000
        self.max_health = 1000
        self.is_dead = 0


class EnemyMage(Enemy):
    def __init__(self):
        super().__init__(MAGE_0)
        self.name = "ultra boss"
        self.max_current_sprites = 6
        self.update_speed = 0.1
        self.sprites.append(MAGE_1)
        self.sprites.append(MAGE_2)
        self.sprites.append(MAGE_3)
        self.sprites.append(MAGE_4)
        self.sprites.append(MAGE_5)
        self.sprites.append(MAGE_6)

        self.stride = 0.3
        self.max_stride = 1
        self.health = 9999
        self.max_health = 9999
        self.is_dead = 0

        self.summon_counter = 0
        self.summon_max_counter = 60

    def summon(self):
        if self.summon_counter < self.summon_max_counter:
            self.summon_counter += 1
            return False
        else:
            self.summon_counter = 0
            return True

    def buff(self):
        if self.health < self.max_health - 1000:
            self.health += 1000
        else:
            self.health = self.max_health





