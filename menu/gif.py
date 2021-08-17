import pygame
import os
from dir_path import *

# obelisk image
OBELISK_IMAGE_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "obelisk_image0.png")), (150, 150))
OBELISK_IMAGE_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "obelisk_image1.png")), (150, 150))
OBELISK_IMAGE_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "obelisk_image2.png")), (150, 150))
OBELISK_IMAGE_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "obelisk_image3.png")), (150, 150))
OBELISK_IMAGE_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "obelisk_image4.png")), (150, 150))
OBELISK_IMAGE_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "obelisk_image5.png")), (150, 150))
OBELISK_IMAGE_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "obelisk_image6.png")), (150, 150))
OBELISK_IMAGE_7 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "obelisk_image7.png")), (150, 150))
OBELISK_IMAGE_8 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "obelisk_image8.png")), (150, 150))
OBELISK_IMAGE_9 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "obelisk_image9.png")), (150, 150))
OBELISK_IMAGE_10 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "obelisk_image10.png")), (150, 150))
OBELISK_IMAGE_11 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "obelisk_image11.png")), (150, 150))
OBELISK_IMAGE_12 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "obelisk_image12.png")), (150, 150))
OBELISK_IMAGE_13 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "obelisk_image13.png")), (150, 150))

# moon tower image
MOON_IMAGE_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "moon_image0.png")), (110, 110))
MOON_IMAGE_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "moon_image1.png")), (110, 110))
MOON_IMAGE_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "moon_image2.png")), (110, 110))
MOON_IMAGE_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "moon_image3.png")), (110, 110))
MOON_IMAGE_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "moon_image4.png")), (110, 110))
MOON_IMAGE_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "moon_image5.png")), (110, 110))
MOON_IMAGE_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "moon_image6.png")), (110, 110))
MOON_IMAGE_7 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "moon_image7.png")), (110, 110))
MOON_IMAGE_8 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "moon_image8.png")), (110, 110))
MOON_IMAGE_9 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "moon_image9.png")), (110, 110))

# red fire tower image
RED_IMAGE_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "red_image0.png")), (110, 110))
RED_IMAGE_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "red_image1.png")), (110, 110))
RED_IMAGE_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "red_image2.png")), (110, 110))
RED_IMAGE_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "red_image3.png")), (110, 110))
RED_IMAGE_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "red_image4.png")), (110, 110))
RED_IMAGE_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "red_image5.png")), (110, 110))
RED_IMAGE_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "red_image6.png")), (110, 110))

# blue fire tower image
BLUE_IMAGE_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "blue_image0.png")), (110, 110))
BLUE_IMAGE_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "blue_image1.png")), (110, 110))
BLUE_IMAGE_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "blue_image2.png")), (110, 110))
BLUE_IMAGE_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "blue_image3.png")), (110, 110))
BLUE_IMAGE_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "blue_image4.png")), (110, 110))
BLUE_IMAGE_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "blue_image5.png")), (110, 110))
BLUE_IMAGE_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "blue_image6.png")), (110, 110))

# vacancy image
PLOT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "vacant_lot.png")), (40, 40))


# skull image with various colors
PURPLE_SKULL_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_A", "PNG", "frame0000.png")), (80, 80))
PURPLE_SKULL_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_A", "PNG", "frame0002.png")), (80, 80))
PURPLE_SKULL_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_A", "PNG", "frame0004.png")), (80, 80))
PURPLE_SKULL_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_A", "PNG", "frame0006.png")), (80, 80))
PURPLE_SKULL_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_A", "PNG", "frame0008.png")), (80, 80))
PURPLE_SKULL_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_A", "PNG", "frame0010.png")), (80, 80))
PURPLE_SKULL_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_A", "PNG", "frame0012.png")), (80, 80))
PURPLE_SKULL_7 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_A", "PNG", "frame0014.png")), (80, 80))

GREEN_SKULL_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_B", "PNG", "frame0000.png")), (80, 80))
GREEN_SKULL_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_B", "PNG", "frame0002.png")), (80, 80))
GREEN_SKULL_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_B", "PNG", "frame0004.png")), (80, 80))
GREEN_SKULL_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_B", "PNG", "frame0006.png")), (80, 80))
GREEN_SKULL_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_B", "PNG", "frame0008.png")), (80, 80))
GREEN_SKULL_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_B", "PNG", "frame0010.png")), (80, 80))
GREEN_SKULL_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_B", "PNG", "frame0012.png")), (80, 80))
GREEN_SKULL_7 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_B", "PNG", "frame0014.png")), (80, 80))

RED_SKULL_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_C", "PNG", "frame0000.png")), (80, 80))
RED_SKULL_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_C", "PNG", "frame0002.png")), (80, 80))
RED_SKULL_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_C", "PNG", "frame0004.png")), (80, 80))
RED_SKULL_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_C", "PNG", "frame0006.png")), (80, 80))
RED_SKULL_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_C", "PNG", "frame0008.png")), (80, 80))
RED_SKULL_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_C", "PNG", "frame0010.png")), (80, 80))
RED_SKULL_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_C", "PNG", "frame0012.png")), (80, 80))
RED_SKULL_7 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_C", "PNG", "frame0014.png")), (80, 80))

YELLOW_SKULL_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_D", "PNG", "frame0000.png")), (80, 80))
YELLOW_SKULL_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_D", "PNG", "frame0002.png")), (80, 80))
YELLOW_SKULL_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_D", "PNG", "frame0004.png")), (80, 80))
YELLOW_SKULL_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_D", "PNG", "frame0006.png")), (80, 80))
YELLOW_SKULL_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_D", "PNG", "frame0008.png")), (80, 80))
YELLOW_SKULL_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_D", "PNG", "frame0010.png")), (80, 80))
YELLOW_SKULL_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_D", "PNG", "frame0012.png")), (80, 80))
YELLOW_SKULL_7 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_D", "PNG", "frame0014.png")), (80, 80))

BLUE_SKULL_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_E", "PNG", "frame0000.png")), (80, 80))
BLUE_SKULL_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_E", "PNG", "frame0002.png")), (80, 80))
BLUE_SKULL_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_E", "PNG", "frame0004.png")), (80, 80))
BLUE_SKULL_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_E", "PNG", "frame0006.png")), (80, 80))
BLUE_SKULL_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_E", "PNG", "frame0008.png")), (80, 80))
BLUE_SKULL_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_E", "PNG", "frame0010.png")), (80, 80))
BLUE_SKULL_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_E", "PNG", "frame0012.png")), (80, 80))
BLUE_SKULL_7 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "floating_skull_enemy", "style_E", "PNG", "frame0014.png")), (80, 80))

# orc with various species
ORC1_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "1_ORK", "WALK", "WALK_000.png")), (80, 80))
ORC1_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "1_ORK", "WALK", "WALK_001.png")), (80, 80))
ORC1_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "1_ORK", "WALK", "WALK_002.png")), (80, 80))
ORC1_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "1_ORK", "WALK", "WALK_003.png")), (80, 80))
ORC1_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "1_ORK", "WALK", "WALK_004.png")), (80, 80))
ORC1_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "1_ORK", "WALK", "WALK_005.png")), (80, 80))
ORC1_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "1_ORK", "WALK", "WALK_006.png")), (80, 80))

ORC2_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "2_ORK", "WALK", "WALK_000.png")), (80, 80))
ORC2_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "2_ORK", "WALK", "WALK_001.png")), (80, 80))
ORC2_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "2_ORK", "WALK", "WALK_002.png")), (80, 80))
ORC2_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "2_ORK", "WALK", "WALK_003.png")), (80, 80))
ORC2_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "2_ORK", "WALK", "WALK_004.png")), (80, 80))
ORC2_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "2_ORK", "WALK", "WALK_005.png")), (80, 80))
ORC2_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "2_ORK", "WALK", "WALK_006.png")), (80, 80))

ORC3_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "3_ORK", "WALK", "WALK_000.png")), (80, 80))
ORC3_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "3_ORK", "WALK", "WALK_001.png")), (80, 80))
ORC3_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "3_ORK", "WALK", "WALK_002.png")), (80, 80))
ORC3_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "3_ORK", "WALK", "WALK_003.png")), (80, 80))
ORC3_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "3_ORK", "WALK", "WALK_004.png")), (80, 80))
ORC3_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "3_ORK", "WALK", "WALK_005.png")), (80, 80))
ORC3_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "2D-Fantasy-Orcs-Free-Sprite-Sheets", "_PNG", "3_ORK", "WALK", "WALK_006.png")), (80, 80))

# bat
BAT_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "bat_0.png")), (40, 40))
BAT_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "bat_1.png")), (40, 40))
BAT_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "bat_2.png")), (40, 40))
BAT_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "bat_3.png")), (40, 40))

# fly
FLY_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "fly_0.png")), (80, 80))
FLY_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "fly_1.png")), (80, 80))
FLY_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "fly_2.png")), (80, 80))
FLY_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "fly_3.png")), (80, 80))

# rock
ROCK_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "rock_0.png")), (80, 80))
ROCK_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "rock_1.png")), (80, 80))

# lightning
LIGHT_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "lightning_0.png")), (50, 600))
LIGHT_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "lightning_1.png")), (50, 600))
LIGHT_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "lightning_2.png")), (50, 600))
LIGHT_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "lightning_3.png")), (50, 600))
LIGHT_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "lightning_4.png")), (50, 600))
LIGHT_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "lightning_5.png")), (50, 600))
LIGHT_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "lightning_6.png")), (50, 600))
LIGHT_7 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "lightning_7.png")), (50, 600))
LIGHT_8 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "lightning_8.png")), (50, 600))

# red beam
BEAM_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "red_beam_0.png")), (50, 600))
BEAM_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "red_beam_1.png")), (50, 600))
BEAM_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "red_beam_2.png")), (50, 600))
BEAM_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "red_beam_3.png")), (50, 600))
BEAM_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "red_beam_4.png")), (50, 600))
BEAM_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "red_beam_5.png")), (50, 600))

# fire ball
FIRE_BALL_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "fire_ball_0.png")), (50, 100))
FIRE_BALL_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "fire_ball_1.png")), (50, 100))
FIRE_BALL_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "fire_ball_2.png")), (50, 100))
FIRE_BALL_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "fire_ball_3.png")), (50, 100))
FIRE_BALL_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "fire_ball_4.png")), (50, 100))
FIRE_BALL_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "fire_ball_5.png")), (50, 100))
FIRE_BALL_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "fire_ball_6.png")), (50, 100))

# flame
FLAME_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "flame_0.png")), (400, 900))
FLAME_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "flame_1.png")), (400, 900))
FLAME_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "flame_2.png")), (400, 900))
FLAME_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "flame_3.png")), (400, 900))
FLAME_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "flame_4.png")), (400, 900))
FLAME_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "flame_5.png")), (400, 900))
FLAME_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "flame_6.png")), (400, 900))
FLAME_7 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "flame_7.png")), (400, 900))
FLAME_8 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "flame_8.png")), (400, 900))
FLAME_9 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "flame_9.png")), (400, 900))

# blue flame
BLUE_FLAME_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "blue_flame_0.png")), (400, 400))
BLUE_FLAME_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "blue_flame_1.png")), (400, 400))
BLUE_FLAME_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "blue_flame_2.png")), (400, 400))
BLUE_FLAME_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "blue_flame_3.png")), (400, 400))
BLUE_FLAME_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "blue_flame_4.png")), (400, 400))
BLUE_FLAME_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "blue_flame_5.png")), (400, 400))
BLUE_FLAME_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "blue_flame_6.png")), (400, 400))
BLUE_FLAME_7 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "blue_flame_7.png")), (400, 400))
BLUE_FLAME_8 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "blue_flame_8.png")), (400, 400))
BLUE_FLAME_9 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "blue_flame_9.png")), (400, 400))

# magic circle
MAGIC_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "magic_0.png")), (120, 60))
MAGIC_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "magic_1.png")), (120, 60))

# worm
WORM_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "worm_0.png")), (80, 80))
WORM_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "worm_1.png")), (80, 80))
WORM_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "worm_2.png")), (80, 80))
WORM_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "worm_3.png")), (80, 80))
WORM_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "worm_4.png")), (80, 80))

# red_bat
RED_BAT_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "red_bat_0.png")), (80, 80))
RED_BAT_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "red_bat_1.png")), (80, 80))
RED_BAT_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "red_bat_2.png")), (80, 80))
RED_BAT_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "red_bat_3.png")), (80, 80))

# black bat
BLACK_BAT_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "black_bat_0.png")), (80, 80))
BLACK_BAT_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "black_bat_1.png")), (80, 80))
BLACK_BAT_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "black_bat_2.png")), (80, 80))
BLACK_BAT_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "black_bat_3.png")), (80, 80))

# mage
MAGE_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "mage_0.png")), (100, 100))
MAGE_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "mage_1.png")), (100, 100))
MAGE_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "mage_2.png")), (100, 100))
MAGE_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "mage_3.png")), (100, 100))
MAGE_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "mage_4.png")), (100, 100))
MAGE_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "mage_5.png")), (100, 100))
MAGE_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "mage_6.png")), (100, 100))

# knight
KNIGHT_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "knight_0.png")), (80, 80))
KNIGHT_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "knight_1.png")), (80, 80))
KNIGHT_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "knight_2.png")), (80, 80))
KNIGHT_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "knight_3.png")), (80, 80))
KNIGHT_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "knight_4.png")), (80, 80))
KNIGHT_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "knight_5.png")), (80, 80))
KNIGHT_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "knight_6.png")), (80, 80))
KNIGHT_7 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "knight_7.png")), (80, 80))

# ghost
GHOST_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "ghost_0.png")), (100, 120))
GHOST_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "ghost_1.png")), (100, 120))
GHOST_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "ghost_2.png")), (100, 120))
GHOST_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "ghost_3.png")), (100, 120))
GHOST_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "ghost_4.png")), (100, 120))
GHOST_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "ghost_5.png")), (100, 120))

# evil skull
EVIL_SKULL_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Walk", "Bringer-of-Death_Walk_1.png")), (90, 100))
EVIL_SKULL_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Walk", "Bringer-of-Death_Walk_2.png")), (90, 100))
EVIL_SKULL_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Walk", "Bringer-of-Death_Walk_3.png")), (90, 100))
EVIL_SKULL_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Walk", "Bringer-of-Death_Walk_4.png")), (90, 100))
EVIL_SKULL_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Walk", "Bringer-of-Death_Walk_5.png")), (90, 100))
EVIL_SKULL_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Walk", "Bringer-of-Death_Walk_6.png")), (90, 100))
EVIL_SKULL_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Walk", "Bringer-of-Death_Walk_7.png")), (90, 100))
EVIL_SKULL_7 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Walk", "Bringer-of-Death_Walk_8.png")), (90, 100))

# meteor
METEOR_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "meteor_0.png")), (500, 500))
METEOR_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "meteor_1.png")), (500, 500))
METEOR_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "meteor_2.png")), (500, 500))
METEOR_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "meteor_3.png")), (500, 500))
METEOR_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "meteor_4.png")), (500, 500))

# miss
MISS = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "miss.png")), (100, 50))

# slow
SLOW = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "speed_lower.png")), (150, 50))

# tower buff
CD = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "buff.png")), (150, 50))

# kill
KILL_0 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Spell", "Bringer-of-Death_Spell_1.png")), (200, 180))
KILL_1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Spell", "Bringer-of-Death_Spell_2.png")), (200, 180))
KILL_2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Spell", "Bringer-of-Death_Spell_3.png")), (200, 180))
KILL_3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Spell", "Bringer-of-Death_Spell_4.png")), (200, 180))
KILL_4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Spell", "Bringer-of-Death_Spell_5.png")), (200, 180))
KILL_5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Spell", "Bringer-of-Death_Spell_6.png")), (200, 180))
KILL_6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Spell", "Bringer-of-Death_Spell_7.png")), (200, 180))
KILL_7 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Spell", "Bringer-of-Death_Spell_8.png")), (200, 180))
KILL_8 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Spell", "Bringer-of-Death_Spell_9.png")), (200, 180))
KILL_9 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Spell", "Bringer-of-Death_Spell_10.png")), (200, 180))
KILL_10 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Spell", "Bringer-of-Death_Spell_11.png")), (200, 180))
KILL_11 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Spell", "Bringer-of-Death_Spell_12.png")), (200, 180))
KILL_12 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Spell", "Bringer-of-Death_Spell_13.png")), (200, 180))
KILL_13 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Spell", "Bringer-of-Death_Spell_14.png")), (200, 180))
KILL_14 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Spell", "Bringer-of-Death_Spell_15.png")), (200, 180))
KILL_15 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Spell", "Bringer-of-Death_Spell_16.png")), (200, 180))

