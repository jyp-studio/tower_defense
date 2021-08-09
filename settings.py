import pygame
import os
from singleton import VolController,MapController

# screen size
WIN_WIDTH = 1024
WIN_HEIGHT = 600
# frame rate
FPS = 60
# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (147, 0, 147)
# enemy path
PATH = [(22, 308), (52, 283), (84, 283), (110, 305), (116, 341), (115, 375), (112, 405), (116, 433),
          (135, 455), (159, 475), (188, 480), (217, 481), (243, 474), (267, 463), (291, 454), (315, 441),
          (334, 423), (343, 398), (339, 368), (328, 345), (305, 331), (282, 322), (264, 303), (255, 283),
          (259, 259), (274, 239), (294, 225), (318, 214), (347, 212), (373, 217), (394, 230), (410, 250),
          (429, 266), (446, 282), (465, 295), (483, 310), (502, 321), (523, 309), (535, 282), (535, 254),
          (533, 230), (532, 190)]
PATH1 = [(87, 269), (97, 276), (108, 282), (119, 287), (130, 292), (141, 297), (153, 302), (164, 306),
        (175, 311), (186, 315), (198, 319), (211, 322), (223, 326), (237, 330), (249, 332), (262, 335), (276, 338),
        (290, 339), (302, 342), (315, 346), (326, 348), (339, 349), (354, 350), (371, 352), (381, 355), (392, 357),
        (403, 359), (417, 361), (430, 364), (446, 365), (459, 367), (472, 369), (488, 369), (500, 369), (513, 369),
        (529, 366), (543, 365), (556, 363), (571, 360), (586, 356), (600, 353), (611, 349), (625, 345), (638, 339),
        (651, 335), (665, 331), (679, 326), (693, 320), (704, 315), (715, 311), (727, 307), (740, 302), (753, 299),
        (766, 295), (777, 289), (789, 281), (803, 277), (816, 273), (828, 270), (840, 263), (856, 262), (869, 257),
        (881, 255), (894, 252), (907, 248), (918, 244), (933, 240), (950, 237), (964, 235), (979, 233), (991, 232),
        (1001, 232), (1013, 232)]
PATH2 = [(302, 595), (310, 588), (320, 583), (330, 578), (339, 573), (349, 568), (359, 561), (369, 554),
        (378, 548), (387, 540), (396, 532), (405, 523), (413, 515), (421, 506), (428, 495), (433, 486), (438, 475),
        (442, 465), (445, 454), (447, 441), (450, 427), (453, 412), (456, 401), (461, 390), (470, 384), (479, 380),
        (489, 379), (502, 379), (512, 378), (524, 375), (538, 373), (547, 371), (558, 369), (571, 366), (581, 362),
        (590, 359), (600, 355), (611, 350), (622, 346), (633, 343), (645, 341), (658, 337), (668, 333), (681, 329),
        (694, 326), (704, 322), (715, 318), (726, 313), (736, 308), (748, 303), (758, 297), (767, 295), (781, 290),
        (793, 286), (806, 281), (817, 276), (830, 272), (841, 268), (851, 263), (861, 260), (871, 258), (882, 255),
        (893, 253), (903, 251), (916, 250), (932, 249), (944, 247), (957, 246), (971, 242), (985, 242), (1003, 240),
        (1015, 239)]
# base
BASE = pygame.Rect(430, 90, 195, 130)

# image
HP_GRAY_IMAGE = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (35, 33))
HP_IMAGE = pygame.transform.scale(pygame.image.load("images/hp.png"), (35, 33))

# singleton
singleton_vol_controller=VolController()
singleton_map_controller=MapController()

# global var
game_status={
    "run":True,
    "go_start_menu":False}
