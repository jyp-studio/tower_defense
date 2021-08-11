from __future__ import annotations
from enemy.enemies import *

pygame.init()


class EnemyBat(Enemy):
    def __init__(self):
        super().__init__(BAT_0)
        self.name = "bat"
        self.max_current_sprites = 3
        self.update_speed = 0.25
        self.sprites.append(BAT_1)
        self.sprites.append(BAT_2)
        self.sprites.append(BAT_3)

        self.stride = 7
        self.health = 100
        self.max_health = 100
        self.is_dead = 0




