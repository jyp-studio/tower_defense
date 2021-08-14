from __future__ import annotations
from enemy.enemies import *
pygame.init()


class EnemyOrc1(Enemy):
    def __init__(self):
        super().__init__(ORC1_0)
        self.name = "orc"
        self.max_current_sprites = 6
        self.update_speed = 0.25
        self.sprites.append(ORC1_1)
        self.sprites.append(ORC1_2)
        self.sprites.append(ORC1_3)
        self.sprites.append(ORC1_4)
        self.sprites.append(ORC1_5)
        self.sprites.append(ORC1_6)

        self.stride = 3
        self.max_stride = 3
        self.health = 100
        self.max_health = 100
        self.is_dead = 0


class EnemyOrc2(Enemy):
    def __init__(self):
        super().__init__(ORC2_0)
        self.name = "orc"
        self.max_current_sprites = 6
        self.update_speed = 0.25
        self.sprites.append(ORC2_1)
        self.sprites.append(ORC2_2)
        self.sprites.append(ORC2_3)
        self.sprites.append(ORC2_4)
        self.sprites.append(ORC2_5)
        self.sprites.append(ORC2_6)

        self.stride = 5
        self.max_stride = 5
        self.health = 200
        self.max_health = 200
        self.is_dead = 0


class EnemyOrc3(Enemy):
    def __init__(self):
        super().__init__(ORC3_0)
        self.name = "boss"
        self.max_current_sprites = 6
        self.update_speed = 0.25
        self.sprites.append(ORC3_1)
        self.sprites.append(ORC3_2)
        self.sprites.append(ORC3_3)
        self.sprites.append(ORC3_4)
        self.sprites.append(ORC3_5)
        self.sprites.append(ORC3_6)

        self.stride = 2
        self.max_stride = 2
        self.health = 1000
        self.max_health = 1000
        self.is_dead = 0

