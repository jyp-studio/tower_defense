from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.model import GameModel
import pygame
import math
import random
import os
from settings import singleton_map_controller
from gif import *
from color_settings import *

pygame.init()


class Enemy:
    def __init__(self, image):
        self.name = ""
        dir = random.randint(1, len(singleton_map_controller.curPathPage))
        self.path = singleton_map_controller.curPathPage[dir]
        self.path_index = 0
        self.move_count = 0
        self.stride = 3
        self.health = 50
        self.max_health = 50
        self.is_dead = 0

        self.sprites = []
        self.current_sprites = 0
        self.max_current_sprites = 10
        self.update_speed = 1
        self.sprites.append(image)
        self.image = self.sprites[self.current_sprites]
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.path_index = 0
        self.right_direction = True

    def move(self):
        x1, y1 = self.path[self.path_index]
        x2, y2 = self.path[self.path_index + 1]
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        max_count = int(distance / self.stride)
        # direction
        direction = x2 - x1
        if direction < 0:
            self.right_direction = False
        else:
            self.right_direction = True
        # compute the unit vector
        unit_vector_x = (x2 - x1) / distance
        unit_vector_y = (y2 - y1) / distance
        # compute the movement
        delta_x = unit_vector_x * self.stride * self.move_count
        delta_y = unit_vector_y * self.stride * self.move_count
        # update the position and counter
        if self.move_count <= max_count:
            self.rect.center = (x1 + delta_x, y1 + delta_y)
            self.move_count += 1
        else:
            self.move_count = 0
            self.path_index += 1
            self.rect.center = self.path[self.path_index]

    def update(self):
        self.current_sprites += self.update_speed
        if self.current_sprites >= self.max_current_sprites:
            self.current_sprites = 0
        # flip images
        if not self.right_direction:
            flip_image = pygame.transform.flip(self.sprites[int(self.current_sprites)], True, False)
            self.image = flip_image
        else:
            self.image = self.sprites[int(self.current_sprites)]

    def direction(self):
        return self.right_direction


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
        self.health = 70
        self.max_health = 70
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
        self.health = 150
        self.max_health = 150
        self.is_dead = 0


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


class EnemyBat(Enemy):
    def __init__(self):
        super().__init__(BAT_0)
        self.name = "bat"
        self.max_current_sprites = 3
        self.update_speed = 0.25
        self.sprites.append(BAT_1)
        self.sprites.append(BAT_2)
        self.sprites.append(BAT_3)

        self.stride = 7
        self.health = 100
        self.max_health = 100
        self.is_dead = 0


class EnemySKULL1(Enemy):
    def __init__(self):
        super().__init__(YELLOW_SKULL_0)
        self.name = "skull"
        self.max_current_sprites = 7
        self.update_speed = 0.5
        self.sprites.append(YELLOW_SKULL_1)
        self.sprites.append(YELLOW_SKULL_2)
        self.sprites.append(YELLOW_SKULL_3)
        self.sprites.append(YELLOW_SKULL_4)
        self.sprites.append(YELLOW_SKULL_5)
        self.sprites.append(YELLOW_SKULL_6)
        self.sprites.append(YELLOW_SKULL_7)

        self.stride = 1
        self.health = 500
        self.max_health = 500
        self.is_dead = 5


class EnemySKULL2(Enemy):
    def __init__(self):
        super().__init__(GREEN_SKULL_0)
        self.name = "skull"
        self.max_current_sprites = 7
        self.update_speed = 0.5
        self.sprites.append(GREEN_SKULL_0)
        self.sprites.append(GREEN_SKULL_1)
        self.sprites.append(GREEN_SKULL_2)
        self.sprites.append(GREEN_SKULL_3)
        self.sprites.append(GREEN_SKULL_4)
        self.sprites.append(GREEN_SKULL_5)
        self.sprites.append(GREEN_SKULL_6)
        self.sprites.append(GREEN_SKULL_7)

        self.stride = 1
        self.health = 500
        self.max_health = 500
        self.is_dead = 4


class EnemySKULL3(Enemy):
    def __init__(self):
        super().__init__(BLUE_SKULL_0)
        self.name = "skull"
        self.max_current_sprites = 7
        self.update_speed = 0.5
        self.sprites.append(BLUE_SKULL_1)
        self.sprites.append(BLUE_SKULL_2)
        self.sprites.append(BLUE_SKULL_3)
        self.sprites.append(BLUE_SKULL_4)
        self.sprites.append(BLUE_SKULL_5)
        self.sprites.append(BLUE_SKULL_6)
        self.sprites.append(BLUE_SKULL_7)

        self.stride = 1
        self.health = 500
        self.max_health = 500
        self.is_dead = 3


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
        self.health = 500
        self.max_health = 500
        self.is_dead = 2


class EnemySKULL5(Enemy):
    def __init__(self):
        super().__init__(RED_SKULL_0)
        self.name = "skull"
        self.max_current_sprites = 7
        self.update_speed = 0.5
        self.sprites.append(RED_SKULL_1)
        self.sprites.append(RED_SKULL_2)
        self.sprites.append(RED_SKULL_3)
        self.sprites.append(RED_SKULL_4)
        self.sprites.append(RED_SKULL_5)
        self.sprites.append(RED_SKULL_6)
        self.sprites.append(RED_SKULL_7)

        self.stride = 1
        self.health = 500
        self.max_health = 500
        self.is_dead = 1


class EnemySKULL6(Enemy):
    def __init__(self):
        super().__init__(YELLOW_SKULL_0)
        self.name = "skull"
        self.max_current_sprites = 7
        self.update_speed = 0.5
        self.sprites.append(GREEN_SKULL_1)
        self.sprites.append(BLUE_SKULL_2)
        self.sprites.append(PURPLE_SKULL_3)
        self.sprites.append(RED_SKULL_4)
        self.sprites.append(YELLOW_SKULL_5)
        self.sprites.append(GREEN_SKULL_6)
        self.sprites.append(BLUE_SKULL_7)

        self.stride = 1
        self.health = 1000
        self.max_health = 1000
        self.is_dead = 0


class EnemyROCK(Enemy):
    def __init__(self):
        super().__init__(ROCK_0)
        self.name = "boss"
        self.max_current_sprites = 2
        self.update_speed = 0.25
        self.sprites.append(ROCK_1)

        self.stride = 0.1
        self.health = 99999
        self.max_health = 99999
        self.is_dead = 0

      
class EnemyGroup:
    def __init__(self):
        self.campaign_count = 0
        self.campaign_max_count = 60   # (unit: frame)
        self.__reserved_members = []
        self.__expedition = []
        self.wave_counter = 0

    def advance(self, model:GameModel):
        # use model.hp and model.money to access the hp and money information
        self.campaign()
        for en in self.__expedition:
            en.move()
            if en.health <= 0:
                if en.is_dead == 0:
                    self.__expedition.append(EnemySKULL1())
                    self.retreat(en)
                    model.money += 15
                else:
                    if en.is_dead == 5:
                        en.is_dead = 4
                        en.sprites.clear()
                        en.sprites.append(GREEN_SKULL_0)
                        en.sprites.append(GREEN_SKULL_1)
                        en.sprites.append(GREEN_SKULL_2)
                        en.sprites.append(GREEN_SKULL_3)
                        en.sprites.append(GREEN_SKULL_4)
                        en.sprites.append(GREEN_SKULL_5)
                        en.sprites.append(GREEN_SKULL_6)
                        en.sprites.append(GREEN_SKULL_7)
                        en.health = 500
                        en.max_health = 500
                    elif en.is_dead == 4:
                        en.is_dead = 3
                        en.sprites.clear()
                        en.sprites.append(BLUE_SKULL_0)
                        en.sprites.append(BLUE_SKULL_1)
                        en.sprites.append(BLUE_SKULL_2)
                        en.sprites.append(BLUE_SKULL_3)
                        en.sprites.append(BLUE_SKULL_4)
                        en.sprites.append(BLUE_SKULL_5)
                        en.sprites.append(BLUE_SKULL_6)
                        en.sprites.append(BLUE_SKULL_7)
                        en.health = 500
                        en.max_health = 500
                    elif en.is_dead == 3:
                        en.is_dead = 2
                        en.sprites.clear()
                        en.sprites.append(PURPLE_SKULL_0)
                        en.sprites.append(PURPLE_SKULL_1)
                        en.sprites.append(PURPLE_SKULL_2)
                        en.sprites.append(PURPLE_SKULL_3)
                        en.sprites.append(PURPLE_SKULL_4)
                        en.sprites.append(PURPLE_SKULL_5)
                        en.sprites.append(PURPLE_SKULL_6)
                        en.sprites.append(PURPLE_SKULL_7)
                        en.health = 500
                        en.max_health = 500
                    elif en.is_dead == 2:
                        en.is_dead = 1
                        en.sprites.clear()
                        en.sprites.append(RED_SKULL_0)
                        en.sprites.append(RED_SKULL_1)
                        en.sprites.append(RED_SKULL_2)
                        en.sprites.append(RED_SKULL_3)
                        en.sprites.append(RED_SKULL_4)
                        en.sprites.append(RED_SKULL_5)
                        en.sprites.append(RED_SKULL_6)
                        en.sprites.append(RED_SKULL_7)
                        en.health = 500
                        en.max_health = 500
                    else:
                        en.is_dead = 0
                        en.sprites.clear()
                        en.sprites.append(PURPLE_SKULL_0)
                        en.sprites.append(RED_SKULL_1)
                        en.sprites.append(YELLOW_SKULL_2)
                        en.sprites.append(GREEN_SKULL_3)
                        en.sprites.append(BLUE_SKULL_4)
                        en.sprites.append(PURPLE_SKULL_5)
                        en.sprites.append(RED_SKULL_6)
                        en.sprites.append(YELLOW_SKULL_7)
                        en.health = 2000
                        en.max_health = 2000

            # delete the object when it reach the base
            if singleton_map_controller.curBaseRect.collidepoint(en.rect.centerx, en.rect.centery):
                self.retreat(en)
                model.hp -= 1

    def campaign(self):
        """Enemy go on an expedition."""
        if self.campaign_count > self.campaign_max_count and self.__reserved_members:
            self.__expedition.append(self.__reserved_members.pop())
            self.campaign_count = 0
        else:
            self.campaign_count += 1

    def add(self, num:int):
        """Generate the enemies for next wave"""
        if self.is_empty():
            if self.wave_counter % 7 == 0:
                self.__reserved_members = [EnemyFly() for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 7 == 1:
                self.__reserved_members = [EnemyOrc1() for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 7 == 2:
                self.__reserved_members = [EnemyOrc2() for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 7 == 3:
                self.__reserved_members = [EnemyOrc3() for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 7 == 4:
                self.__reserved_members = [EnemyBat() for _ in range(num)]
                self.wave_counter += 1
            elif self.wave_counter % 7 == 5:
                self.__reserved_members = [EnemySKULL1() for _ in range(num)]
                self.wave_counter += 1
            else:
                self.__reserved_members = [EnemyROCK() for _ in range(num)]
                self.wave_counter = 0

    def get(self) -> list:
        """Get the enemy list"""
        return self.__expedition

    def is_empty(self) -> bool:
        """Return whether the enemy is empty (so that we can move on to next wave)"""
        return False if self.__reserved_members or self.__expedition else True

    def retreat(self, enemy: Enemy):
        """Remove the enemy from the expedition"""
        self.__expedition.remove(enemy)

    def retreat_all(self):
        self.__expedition = []
        self.__reserved_members = []





