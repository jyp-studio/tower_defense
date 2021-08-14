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

        self.stride = 1
        self.max_stride = 1
        self.health = 99999
        self.max_health = 99999
        self.is_dead = 0


class EnemyKnight(Enemy):
    def __init__(self):
        super().__init__(KNIGHT_0)
        self.name = "boss"
        self.max_current_sprites = 2
        self.update_speed = 0.25
        self.sprites.append(KNIGHT_1)
        self.sprites.append(KNIGHT_2)
        self.sprites.append(KNIGHT_3)
        self.sprites.append(KNIGHT_4)
        self.sprites.append(KNIGHT_5)
        self.sprites.append(KNIGHT_6)
        self.sprites.append(KNIGHT_7)

        self.stride = 1
        self.max_stride = 1
        self.health = 99999
        self.max_health = 99999
        self.is_dead = 0


class EnemyMage(Enemy):
    def __init__(self):
        super().__init__(MAGE_0)
        self.name = "boss"
        self.max_current_sprites = 2
        self.update_speed = 0.25
        self.sprites.append(MAGE_1)
        self.sprites.append(MAGE_2)
        self.sprites.append(MAGE_3)
        self.sprites.append(MAGE_4)
        self.sprites.append(MAGE_5)
        self.sprites.append(MAGE_6)

        self.stride = 1
        self.max_stride = 1
        self.health = 99999
        self.max_health = 99999
        self.is_dead = 0




