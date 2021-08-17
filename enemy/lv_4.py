from __future__ import annotations
from enemy.enemies import *
from gif import *
pygame.init()


class EnemySKULL1(Enemy):
    def __init__(self):
        super().__init__(YELLOW_SKULL_0)
        self.name = "skull"
        self.max_current_sprites = 8
        self.update_speed = 0.5
        self.sprites.append(YELLOW_SKULL_1)
        self.sprites.append(YELLOW_SKULL_2)
        self.sprites.append(YELLOW_SKULL_3)
        self.sprites.append(YELLOW_SKULL_4)
        self.sprites.append(YELLOW_SKULL_5)
        self.sprites.append(YELLOW_SKULL_6)
        self.sprites.append(YELLOW_SKULL_7)

        self.stride = 4
        self.max_stride = 4
        self.health = 1000
        self.max_health = 1000
        self.is_dead = 0


class EnemySKULL2(Enemy):
    def __init__(self):
        super().__init__(GREEN_SKULL_0)
        self.name = "skull"
        self.max_current_sprites = 8
        self.update_speed = 0.5
        self.sprites.append(GREEN_SKULL_0)
        self.sprites.append(GREEN_SKULL_1)
        self.sprites.append(GREEN_SKULL_2)
        self.sprites.append(GREEN_SKULL_3)
        self.sprites.append(GREEN_SKULL_4)
        self.sprites.append(GREEN_SKULL_5)
        self.sprites.append(GREEN_SKULL_6)
        self.sprites.append(GREEN_SKULL_7)

        self.stride = 4
        self.max_stride = 4
        self.health = 1000
        self.max_health = 1000
        self.is_dead = 1


class EnemySKULL3(Enemy):
    def __init__(self):
        super().__init__(BLUE_SKULL_0)
        self.name = "skull"
        self.max_current_sprites = 8
        self.update_speed = 0.5
        self.sprites.append(BLUE_SKULL_1)
        self.sprites.append(BLUE_SKULL_2)
        self.sprites.append(BLUE_SKULL_3)
        self.sprites.append(BLUE_SKULL_4)
        self.sprites.append(BLUE_SKULL_5)
        self.sprites.append(BLUE_SKULL_6)
        self.sprites.append(BLUE_SKULL_7)

        self.stride = 4
        self.max_stride = 4
        self.health = 1000
        self.max_health = 1000
        self.is_dead = 2


class EnemySKULL4(Enemy):
    def __init__(self):
        super().__init__(PURPLE_SKULL_0)
        self.name = "skull"
        self.max_current_sprites = 8
        self.update_speed = 0.5
        self.sprites.append(PURPLE_SKULL_1)
        self.sprites.append(PURPLE_SKULL_2)
        self.sprites.append(PURPLE_SKULL_3)
        self.sprites.append(PURPLE_SKULL_4)
        self.sprites.append(PURPLE_SKULL_5)
        self.sprites.append(PURPLE_SKULL_6)
        self.sprites.append(PURPLE_SKULL_7)

        self.stride = 4
        self.max_stride = 4
        self.health = 1000
        self.max_health = 1000
        self.is_dead = 3


class EnemySKULL5(Enemy):
    def __init__(self):
        super().__init__(RED_SKULL_0)
        self.name = "skull"
        self.max_current_sprites = 8
        self.update_speed = 0.5
        self.sprites.append(RED_SKULL_1)
        self.sprites.append(RED_SKULL_2)
        self.sprites.append(RED_SKULL_3)
        self.sprites.append(RED_SKULL_4)
        self.sprites.append(RED_SKULL_5)
        self.sprites.append(RED_SKULL_6)
        self.sprites.append(RED_SKULL_7)

        self.stride = 4
        self.max_stride = 4
        self.health = 1000
        self.max_health = 1000
        self.is_dead = 4


class EnemySKULL6(Enemy):
    def __init__(self):
        super().__init__(YELLOW_SKULL_0)
        self.name = "skull"
        self.max_current_sprites = 8
        self.update_speed = 0.5
        self.sprites.append(GREEN_SKULL_1)
        self.sprites.append(BLUE_SKULL_2)
        self.sprites.append(PURPLE_SKULL_3)
        self.sprites.append(RED_SKULL_4)
        self.sprites.append(YELLOW_SKULL_5)
        self.sprites.append(GREEN_SKULL_6)
        self.sprites.append(BLUE_SKULL_7)

        self.stride = 4
        self.max_stride = 4
        self.health = 1000
        self.max_health = 1000
        self.is_dead = 5


class EnemyEvil(Enemy):
    def __init__(self):
        super().__init__(EVIL_SKULL_0)
        self.name = "immortal"
        self.max_current_sprites = 8
        self.update_speed = 0.5
        self.sprites.append(EVIL_SKULL_1)
        self.sprites.append(EVIL_SKULL_2)
        self.sprites.append(EVIL_SKULL_3)
        self.sprites.append(EVIL_SKULL_4)
        self.sprites.append(EVIL_SKULL_5)
        self.sprites.append(EVIL_SKULL_6)
        self.sprites.append(EVIL_SKULL_7)

        self.stride = 2
        self.max_stride = 2
        self.health = 3000
        self.max_health = 3000
        self.is_dead = 0




