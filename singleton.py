import pygame
import os

# enemy path
PATH1_1 = [(91, 348), (110, 330), (135, 322), (158, 329), (184, 340), (195, 364), (195, 392), (191, 420), 
            (200, 448), (203, 473), (228, 485), (254, 490), (294, 488), (327, 483), (365, 473), (386, 452),
            (400, 429), (401, 400), (381, 372), (354, 355), (323, 339), (308, 320), (325, 295), (352, 273),
            (392, 256), (439, 263), (462, 287), (482, 313), (502, 328), (528, 343), (556, 323), (561, 287), 
            (564, 247), (569, 195)]
PATH1_2=[(614, 586), (621, 554), (637, 523), (667, 510), (706, 498), (743, 506), (782, 511), (830, 506), 
            (866, 496), (889, 470), (886, 437), (847, 422), (810, 403), (780, 378), (798, 342), (829, 323), 
            (853, 299), (856, 256), (813, 250), (768, 256), (725, 264), (692, 288), (649, 311), (609, 327), 
            (564, 331), (560, 298), (568, 239), (579, 198)]

PATH2 = [(109, 539), (116, 534), (122, 528), (131, 526), (140, 522), (145, 514), (152, 512), (161, 507), (169, 503), 
        (180, 499), (190, 493), (200, 490), (208, 484), (217, 482), (223, 475), (231, 469), (240, 460), (249, 457), 
        (256, 450), (262, 447), (268, 443), (273, 438), (277, 433), (284, 426), (291, 420), (299, 417), (306, 418), 
        (315, 424), (322, 427), (328, 430), (335, 434), (339, 436), (345, 438), (353, 440), (363, 446), (371, 448), 
        (381, 454), (386, 456), (391, 457), (398, 463), (403, 465), (412, 469), (420, 471), (430, 475), (434, 479), 
        (439, 481), (447, 484), (454, 487), (462, 490), (468, 493), (476, 497), (485, 502), (489, 505), (496, 507), 
        (502, 508), (509, 508), (516, 509), (523, 510), (531, 513), (542, 512), (549, 512), (556, 513), (562, 516), 
        (569, 515), (574, 515), (582, 515), (592, 517), (602, 517), (611, 520), (619, 520), (630, 522), (638, 521), 
        (647, 522), (652, 522), (660, 525), (669, 521), (677, 523), (684, 523), (692, 522), (696, 522), (706, 523), 
        (714, 525), (726, 527), (735, 527), (747, 527), (756, 530), (769, 531), (779, 531), (789, 529), (801, 526), 
        (811, 522), (819, 519), (828, 516), (837, 511), (846, 509), (856, 505), (863, 504), (872, 502), (881, 496), 
        (892, 492), (902, 485), (906, 477), (909, 468), (913, 455), (916, 445), (918, 436), (916, 427), (912, 415), 
        (914, 406), (912, 394), (905, 388), (899, 380), (890, 369), (881, 366), (870, 358), (862, 357), (853, 352), 
        (843, 347), (834, 347), (827, 343), (819, 339), (811, 335), (802, 329), (794, 331), (781, 328), (770, 322), 
        (764, 317), (751, 316), (742, 316), (733, 314), (727, 313), (718, 310), (712, 310), (703, 307), (696, 306), 
        (685, 303), (674, 303), (662, 308), (650, 313), (644, 317), (638, 321), (630, 324), (620, 326), (607, 327), 
        (598, 323), (592, 320), (585, 316), (573, 313), (565, 308), (558, 308), (546, 307), (542, 309), (536, 310), 
        (528, 312), (517, 313), (511, 314), (507, 314), (494, 313), (484, 308), (468, 305), (457, 304), (447, 305), 
        (438, 308), (430, 312), (418, 315), (407, 315), (392, 315), (383, 317), (372, 317), (359, 316), (350, 315), 
        (335, 306), (331, 303), (324, 298), (314, 294), (306, 292), (301, 288), (296, 285), (288, 278), (281, 276), 
        (272, 271), (264, 270), (256, 265), (243, 262), (235, 255), (225, 251), (219, 244), (216, 241), (219, 227), 
        (220, 214), (223, 200), (232, 191), (236, 185), (243, 174), (250, 166), (259, 164), (273, 158), (285, 155), 
        (292, 153), (303, 152), (310, 149), (317, 146), (326, 143), (333, 143), (341, 139), (351, 139), (360, 139), 
        (373, 139), (376, 139), (393, 139), (396, 138), (407, 138), (408, 138), (419, 140), (430, 141), (440, 142), 
        (451, 142), (462, 144), (476, 148), (488, 151), (497, 149), (508, 149), (520, 149), (533, 148), (543, 149), 
        (549, 151), (554, 151), (564, 151), (569, 152), (576, 153), (582, 153), (596, 157), (605, 159), (611, 160), 
        (618, 160), (624, 160), (628, 163), (637, 168), (642, 169), (650, 172), (654, 175), (658, 175), (663, 178), 
        (670, 182), (677, 186), (687, 189), (695, 195), (704, 198), (707, 198), (713, 200), (723, 204), (726, 207), 
        (735, 209), (738, 211), (741, 211), (751, 216), (754, 217), (764, 218), (773, 219), (778, 220), (786, 223), 
        (791, 223), (800, 227), (812, 234), (820, 238), (832, 238), (841, 238), (849, 236), (851, 235), (852, 227), 
        (853, 223), (854, 214), (858, 205), (860, 202), (863, 193), (866, 184), (871, 172), (875, 168), (887, 149), 
        (890, 141), (896, 136), (907, 129)]

PATH3 = [(128, 509), (127, 519), (134, 529), (139, 536), (150, 539), (161, 537), (173, 535), (185, 530), (195, 526),
        (205, 523), (216, 520), (227, 515), (238, 514), (248, 511), (259, 507), (270, 502), (280, 496), (289, 490), (301, 486),
        (310, 481), (320, 475), (334, 469), (343, 464), (353, 458), (362, 452), (374, 449), (384, 442), (393, 436), (396, 425),
        (392, 415), (387, 404), (381, 391), (372, 378), (378, 371), (387, 364), (399, 357), (410, 352), (422, 348), (435, 345),
        (446, 342), (452, 332), (459, 321), (469, 312), (480, 304), (489, 299), (500, 297), (512, 294), (522, 292), (537, 292),
        (550, 294), (564, 297), (578, 299), (591, 305), (601, 310), (611, 315), (621, 321), (632, 330), (646, 334), (657, 340),
        (669, 346), (685, 353), (694, 357), (705, 360), (719, 361), (734, 361), (746, 359), (756, 353), (770, 342), (777, 329),
        (772, 317), (764, 306), (751, 297), (737, 287), (722, 280), (709, 266), (707, 250), (703, 235), (710, 222), (722, 214),
        (735, 209), (744, 204), (755, 199), (765, 193), (773, 190), (784, 185), (796, 180), (808, 175), (820, 170), (833, 166),
        (844, 161), (858, 157), (867, 155), (881, 152), (894, 152), (901, 160), (908, 170)]

PATH4 = [(116, 321), (123, 326), (130, 330), (137, 334), (146, 338), (154, 339), (164, 340), (174, 340), (184, 339), (195, 338),
        (204, 334), (213, 330), (224, 324), (235, 318), (240, 309), (242, 298), (241, 287), (241, 274), (244, 265), (253, 260), (262, 256),
        (271, 252), (283, 247), (293, 244), (304, 241), (315, 237), (324, 235), (335, 234), (345, 234), (357, 233), (368, 231), (376, 231),
        (389, 228), (397, 225), (406, 222), (415, 219), (423, 216), (430, 213), (439, 210), (447, 207), (455, 204), (463, 200), (471, 196),
        (480, 193), (489, 192), (498, 192), (509, 191), (515, 191), (522, 195), (530, 198), (539, 203), (545, 207), (552, 211), (558, 216),
        (562, 223), (567, 227), (572, 234), (576, 240), (581, 245), (588, 251), (596, 255), (602, 259), (608, 264), (614, 271), (614, 276),
        (611, 281), (610, 286), (606, 290), (601, 294), (592, 301), (586, 306), (578, 311), (565, 317), (556, 322), (548, 327), (536, 332),
        (526, 333), (515, 335), (505, 334), (494, 337), (487, 344), (481, 349), (478, 359), (478, 366), (481, 373), (486, 382), (492, 390),
        (497, 398), (505, 404), (512, 410), (519, 416), (524, 422), (530, 428), (537, 435), (543, 441), (552, 446), (556, 450), (562, 458),
        (570, 468), (579, 475), (585, 482), (596, 483), (606, 477), (614, 474), (623, 472), (633, 470), (642, 468), (650, 462), (661, 456),
        (671, 452), (683, 446), (693, 441), (702, 438), (712, 436), (724, 431), (732, 430), (745, 428), (757, 426), (769, 425), (783, 421),
        (795, 417), (806, 412), (815, 408), (823, 405), (833, 401), (844, 396), (853, 390), (861, 382), (867, 374), (869, 361), (873, 349),
        (878, 343), (885, 334), (890, 324), (897, 318), (905, 310), (912, 303), (918, 298), (925, 289), (933, 283), (941, 279), (950, 278),
        (962, 274), (973, 273), (985, 269), (998, 267), (1006, 265), (1015, 265)]

PATH5 = [(136, 448), (148, 448), (163, 449), (177, 449), (191, 449), (202, 449), (218, 449), (232, 447), (242, 445),
        (255, 443), (267, 441), (279, 441), (294, 440), (307, 440), (321, 438), (332, 437), (347, 436), (363, 435), (378, 432),
        (394, 429), (406, 427), (417, 425), (427, 421), (440, 413), (452, 408), (462, 402), (474, 395), (483, 386), (471, 380),
        (461, 372), (453, 360), (452, 346), (457, 337), (463, 332), (470, 326), (479, 320), (491, 312), (500, 306), (509, 302),
        (520, 296), (531, 292), (545, 289), (557, 288), (574, 288), (585, 288), (596, 289), (611, 290), (620, 291), (631, 291),
        (644, 291), (655, 292), (660, 283), (661, 270), (667, 260), (677, 256), (689, 252), (700, 252), (714, 250), (727, 249),
        (740, 249), (755, 249), (769, 250), (783, 250), (799, 250), (811, 251), (825, 251), (838, 250), (851, 250), (862, 250),
        (873, 249), (885, 245), (896, 241), (912, 238), (925, 237)]

PATH_DICT:dict={
    1:{
        1:PATH1_1,
        2:PATH1_2
    },
    2:{
        1:PATH2
    },
    3:{
        1:PATH3
    },
    4:{
        1:PATH4
    },
    5:{
        1:PATH5
    }
}
# base
BASE = pygame.Rect(485, 115, 160,170)
BASE2=pygame.Rect(780, 30, 160,170)
BASE3 = pygame.Rect(855, 5, 160, 170)
BASE4 = pygame.Rect(890, 106, 160, 170)
BASE5 = pygame.Rect(770, 95, 160, 170)
BASE_RECT_DICT:dict={
    1:BASE,
    2:BASE2,
    3:BASE3,
    4:BASE4,
    5:BASE5
}

VacancyPoints1=[(150, 250),(290, 420),(400, 310),(450, 500),(650, 420),(900, 370)]
VacancyPoints2=[(388, 221), (579, 229), (725, 416), (522, 410), (191, 309), (895, 308)]
VacancyPoints3=[(262, 403), (405, 520), (384, 314), (554, 320), (724, 328), (852, 399), (817, 245)]
VacancyPoints4=[(230, 184), (331, 364), (446, 454), (491, 248), (625, 384), (756, 300), (640, 201), (759, 498)]
VacancyPoints5=[(326, 352), (323, 511), (591, 469), (554, 337), (514, 212), (776, 300)]

VACANCY_DICT:dict={
    1:VacancyPoints1,
    2:VacancyPoints2,
    3:VacancyPoints3,
    4:VacancyPoints4,
    5:VacancyPoints5
}

class VolController:
    music_volume = 0.2
    sound_volume = 0.2

    @classmethod
    def minusVol(cls,voice:pygame.mixer.Sound or pygame.mixer.music,vol:float):
        res=voice.get_volume()-vol
        if(0.0<=res<=1.0):
            voice.set_volume(res)
        elif 0.0>res:
            voice.set_volume(0.0)
        else:
            voice.set_volume(1.0)
        
        if isinstance(voice,pygame.mixer.Sound):
            cls.sound_volume=voice.get_volume()
        else:
            cls.music_volume=voice.get_volume()

    @classmethod
    def addVol(cls,voice:pygame.mixer.Sound or pygame.mixer.music,vol:float):
        res=voice.get_volume()+vol
        if(0.0<=res<=1.0):
            voice.set_volume(res)
        elif 0.0>res:
            voice.set_volume(0.0)
        else:
            voice.set_volume(1.0)
        
        if isinstance(voice,pygame.mixer.Sound):
            cls.sound_volume=voice.get_volume()
        else:
            cls.music_volume=voice.get_volume()


class MapController:
    __max_map_index = 5

    def __init__(self,WIN_WIDTH:int, WIN_HEIGHT:int):
        self.__WIN_WIDTH=WIN_WIDTH
        self.__WIN_HEIGHT=WIN_HEIGHT

        self.__map_index=1
        with open('map.txt', 'r') as f:
            self.__map_index=int(f.read())
        self.__map_index=self.__map_index if 1<=self.__map_index<=self.__max_map_index else 1

        self.__next_map_index=int(self.__map_index+1)
        
        self.__curMap= pygame.transform.scale(pygame.image.load(os.path.join("images", "Map"+str(self.__map_index)+".png")),(self.__WIN_WIDTH,self.__WIN_HEIGHT))

        self.__curPathPage=PATH_DICT[self.__map_index]

        self.__curBaseRect=BASE_RECT_DICT[self.__map_index]

        self.__curVacancyList=VACANCY_DICT[self.__map_index]

    def change_map(self):
        with open('map.txt', 'w') as f:
            f.write(str(self.__map_index))
        self.__curMap= pygame.transform.scale(pygame.image.load(os.path.join("images", "Map"+str(self.__map_index)+".png")),(self.__WIN_WIDTH,self.__WIN_HEIGHT))
        self.__curPathPage=PATH_DICT[self.__map_index]
        self.__curBaseRect=BASE_RECT_DICT[self.__map_index]
        self.__curVacancyList=VACANCY_DICT[self.__map_index]
    @property
    def map_index(self)->int:
        return self.__map_index
    
    @map_index.setter
    def map_index(self, value:int):
        self.__map_index=value if 1<=value<=self.__max_map_index else self.__map_index
    
    @property
    def next_map_index(self)->int:
        return self.__next_map_index
    
    @next_map_index.setter
    def next_map_index(self, value:int):
        self.__next_map_index=value if 2<=value<=self.__max_map_index else self.__next_map_index

    @property
    def curMap(self)->pygame.Surface:
        return self.__curMap
    
    @property
    def curBaseRect(self)->pygame.Rect:
        return self.__curBaseRect
    
    @property
    def curPathPage(self)->dict:
        return self.__curPathPage
    
    @property
    def curVacancyList(self)->list:
        return self.__curVacancyList