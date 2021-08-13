from __future__ import annotations
from enemy.enemies import *
pygame.init()


class EnemySKULL4(Enemy):
    def __init__(self):
        super().__init__(PURPLE_SKULL_0)
        self.name = "skull"
        self.max_current_sprites = 7
        self.update_speed = 0.5
        self.sprites.append(PURPLE_SKULL_1)
        self.sprites.append(PURPLE_SKULL_2)
        self.sprites.append(PURPLE_SKULL_3)
        self.sprites.append(PURPLE_SKULL_4)
        self.sprites.append(PURPLE_SKULL_5)
        self.sprites.append(PURPLE_SKULL_6)
        self.sprites.append(PURPLE_SKULL_7)

        self.stride = 1
        self.max_stride = 1
        self.health = 500
        self.max_health = 500
        self.is_dead = 2




