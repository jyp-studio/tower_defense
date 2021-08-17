from __future__ import annotations
from enemy.enemies import Enemy
from gif import *

pygame.init()


class EnemyFly(Enemy):
    def __init__(self):
        super().__init__(FLY_0)
        self.name = "bug"
        self.max_current_sprites = 4
        self.update_speed = 0.5
        self.sprites.append(FLY_1)
        self.sprites.append(FLY_2)
        self.sprites.append(FLY_3)

        self.stride = 6
        self.max_stride = 6
        self.health = 80
        self.max_health = 80
        self.is_dead = 0
        self.right_direction = True


class EnemyWorm(Enemy):
    def __init__(self):
        super().__init__(WORM_0)
        self.name = "bug"
        self.max_current_sprites = 5
        self.update_speed = 0.5
        self.sprites.append(WORM_1)
        self.sprites.append(WORM_2)
        self.sprites.append(WORM_3)
        self.sprites.append(WORM_4)

        self.stride = 6
        self.max_stride = 6
        self.health = 100
        self.max_health = 100
        self.is_dead = 0
        self.right_direction = True


class EnemyBlackBat(Enemy):
    def __init__(self):
        super().__init__(BLACK_BAT_0)
        self.name = "boss"
        self.max_current_sprites = 4
        self.update_speed = 0.5
        self.sprites.append(BLACK_BAT_1)
        self.sprites.append(BLACK_BAT_2)
        self.sprites.append(BLACK_BAT_3)

        self.stride = 6
        self.max_stride = 6
        self.health = 200
        self.max_health = 200
        self.is_dead = 0
        self.right_direction = True




