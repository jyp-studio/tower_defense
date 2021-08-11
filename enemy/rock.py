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
        self.health = 99999
        self.max_health = 99999
        self.is_dead = 0




