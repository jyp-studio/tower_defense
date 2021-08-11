from __future__ import annotations
from enemy.enemies import Enemy
from gif import *

pygame.init()


class EnemyFly(Enemy):
    def __init__(self):
        super().__init__(FLY_0)
        self.name = "fly"
        self.max_current_sprites = 3
        self.update_speed = 0.5
        self.sprites.append(FLY_1)
        self.sprites.append(FLY_2)
        self.sprites.append(FLY_3)

        self.stride = 6
        self.health = 20
        self.max_health = 20
        self.is_dead = 0
        self.right_direction = False





