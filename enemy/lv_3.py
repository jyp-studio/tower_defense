from __future__ import annotations
from enemy.enemies import *

pygame.init()


class EnemyBat(Enemy):
    def __init__(self):
        super().__init__(BAT_0)
        self.name = "fly"
        self.max_current_sprites = 4
        self.update_speed = 0.25
        self.sprites.append(BAT_1)
        self.sprites.append(BAT_2)
        self.sprites.append(BAT_3)

        self.stride = 6
        self.max_stride = 6
        self.health = 200
        self.max_health = 200
        self.is_dead = 0


class EnemyRedBat(Enemy):
    def __init__(self):
        super().__init__(RED_BAT_0)
        self.name = "fly"
        self.max_current_sprites = 4
        self.update_speed = 0.25
        self.sprites.append(RED_BAT_1)
        self.sprites.append(RED_BAT_2)
        self.sprites.append(RED_BAT_3)

        self.stride = 8
        self.max_stride = 8
        self.health = 980
        self.max_health = 980
        self.is_dead = 0


class EnemyGhost(Enemy):
    def __init__(self):
        super().__init__(GHOST_0)
        self.name = "ghost"
        self.max_current_sprites = 6
        self.update_speed = 0.25
        self.sprites.append(GHOST_1)
        self.sprites.append(GHOST_2)
        self.sprites.append(GHOST_3)
        self.sprites.append(GHOST_4)
        self.sprites.append(GHOST_5)

        self.stride = 4
        self.max_stride = 4
        self.health = 8000
        self.max_health = 8000
        self.is_dead = 0

        #def



