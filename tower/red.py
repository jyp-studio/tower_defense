from __future__ import annotations
from tower.towers import *
from gif import *
from tower.towers import Tower


class FireBall:
    def __init__(self, en_x: int, en_y: int, tw_x, tw_y):
        self.sprites = []
        self.current_sprites = 0
        self.max_current_sprites = 5
        self.update_speed = 0.8
        self.sprites.append(FIRE_BALL_0)
        self.sprites.append(FIRE_BALL_1)
        self.sprites.append(FIRE_BALL_2)
        self.sprites.append(FIRE_BALL_3)
        self.sprites.append(FIRE_BALL_4)
        self.sprites.append(FIRE_BALL_5)
        self.sprites.append(FIRE_BALL_6)
        self.image = self.sprites[self.current_sprites]
        self.rect = self.image.get_rect()
        self.en_x = en_x
        self.en_y = en_y
        self.tw_x = tw_x
        self.tw_y = tw_y

    def update(self):
        self.current_sprites += self.update_speed
        if self.current_sprites >= self.max_current_sprites:
            self.current_sprites = 0
        # flip
        direction = self.en_x - self.tw_x
        if direction < 0:
            flip_image = pygame.transform.flip(self.sprites[int(self.current_sprites)], True, False)
            self.image = flip_image
        else:
            self.image = self.sprites[int(self.current_sprites)]


class RedFireTower(Tower):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, SingleAttack())
        self.name = "Fire Totem"
        self.intro = "The shaman with white magic devoted his heart "
        self.intro1 = "to the flame totem to make it alive"
        self.intro2 = "and defend the survival of mankind"
        self.attack_strategy_name = "AOE"
        self.sprites = []
        self.update_speed = 0.2
        self.max_current_sprites = 6
        self.sprites.append(RED_IMAGE_0)
        self.sprites.append(RED_IMAGE_1)
        self.sprites.append(RED_IMAGE_2)
        self.sprites.append(RED_IMAGE_3)
        self.sprites.append(RED_IMAGE_4)
        self.sprites.append(RED_IMAGE_5)
        self.sprites.append(RED_IMAGE_6)

        self.cd_max_count = 120
        self._range = [120, 125, 130, 135, 140, 145, 250]
        self._damage = [8, 14, 18, 22, 25, 35, 50]
        self.value = [120, 160, 220, 320, 400, 500, 10000]

    def throw(self, en_x: int, en_y: int):
        x, y = self.rect.center
        particle = FireBall(x, y + 50, en_x, en_y)
        self.particle_list.append(particle)





