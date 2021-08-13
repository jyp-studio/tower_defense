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
        self.health = 70
        self.max_health = 70
        self.is_dead = 0


