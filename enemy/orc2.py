from __future__ import annotations
from enemy.enemies import *
pygame.init()


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
        self.health = 150
        self.max_health = 150
        self.is_dead = 0



