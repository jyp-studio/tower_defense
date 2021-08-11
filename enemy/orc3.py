from __future__ import annotations
from enemy.enemies import *
pygame.init()


class EnemyOrc3(Enemy):
    def __init__(self):
        super().__init__(ORC3_0)
        self.name = "orc"
        self.max_current_sprites = 6
        self.update_speed = 0.25
        self.sprites.append(ORC3_1)
        self.sprites.append(ORC3_2)
        self.sprites.append(ORC3_3)
        self.sprites.append(ORC3_4)
        self.sprites.append(ORC3_5)
        self.sprites.append(ORC3_6)

        self.stride = 2
        self.health = 400
        self.max_health = 400
        self.is_dead = 0






