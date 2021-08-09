import pygame
import os

# enemy path
PATH1_1 = [(94, 343), (136, 319), (185, 348), (191, 408), (200, 475), (259, 500), (331, 477), (396, 438), (396, 376), 
        (321, 344), (320, 286), (390, 250), (455, 280), (501, 333), (561, 337), (566, 281), (570, 213)]

PATH2_1 = [(87, 269), (97, 276), (108, 282), (119, 287), (130, 292), (141, 297), (153, 302), (164, 306),
        (175, 311), (186, 315), (198, 319), (211, 322), (223, 326), (237, 330), (249, 332), (262, 335), (276, 338),
        (290, 339), (302, 342), (315, 346), (326, 348), (339, 349), (354, 350), (371, 352), (381, 355), (392, 357),
        (403, 359), (417, 361), (430, 364), (446, 365), (459, 367), (472, 369), (488, 369), (500, 369), (513, 369),
        (529, 366), (543, 365), (556, 363), (571, 360), (586, 356), (600, 353), (611, 349), (625, 345), (638, 339),
        (651, 335), (665, 331), (679, 326), (693, 320), (704, 315), (715, 311), (727, 307), (740, 302), (753, 299),
        (766, 295), (777, 289), (789, 281), (803, 277), (816, 273), (828, 270), (840, 263), (856, 262), (869, 257),
        (881, 255), (894, 252), (907, 248), (918, 244), (933, 240), (950, 237), (964, 235), (979, 233), (991, 232),
        (1001, 232), (1013, 232)]
PATH2_2 = [(302, 595), (310, 588), (320, 583), (330, 578), (339, 573), (349, 568), (359, 561), (369, 554),
        (378, 548), (387, 540), (396, 532), (405, 523), (413, 515), (421, 506), (428, 495), (433, 486), (438, 475),
        (442, 465), (445, 454), (447, 441), (450, 427), (453, 412), (456, 401), (461, 390), (470, 384), (479, 380),
        (489, 379), (502, 379), (512, 378), (524, 375), (538, 373), (547, 371), (558, 369), (571, 366), (581, 362),
        (590, 359), (600, 355), (611, 350), (622, 346), (633, 343), (645, 341), (658, 337), (668, 333), (681, 329),
        (694, 326), (704, 322), (715, 318), (726, 313), (736, 308), (748, 303), (758, 297), (767, 295), (781, 290),
        (793, 286), (806, 281), (817, 276), (830, 272), (841, 268), (851, 263), (861, 260), (871, 258), (882, 255),
        (893, 253), (903, 251), (916, 250), (932, 249), (944, 247), (957, 246), (971, 242), (985, 242), (1003, 240),
        (1015, 239)]

PATH_DICT={
    1:{
        1:PATH1_1
    },
    2:{
        1:PATH2_1,
        2:PATH2_2
    }
}
# base
BASE = pygame.Rect(485, 115, 160,170)
BASE2=pygame.Rect(850, 100, 160,170)
BASE_RECT_DICT={
    1:BASE,
    2:BASE2
}


class VolController:
    music_volume = 0.2
    sound_volume = 0.2

    @classmethod
    def minusVol(cls,voice,vol):
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
    def addVol(cls,voice,vol):
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
    __max_map_index=2
    def __init__(self,WIN_WIDTH, WIN_HEIGHT):
        self.__WIN_WIDTH=WIN_WIDTH
        self.__WIN_HEIGHT=WIN_HEIGHT

        self.__map_index=1
        with open('map.txt', 'r') as f:
            self.__map_index=int(f.read())
        self.__map_index=self.__map_index if 1<=self.__map_index<=self.__max_map_index else 1
        
        self.__curMap= pygame.transform.scale(pygame.image.load(os.path.join("images", "Map"+str(self.__map_index)+".png")),(self.__WIN_WIDTH,self.__WIN_HEIGHT))

        self.__curPathPage=PATH_DICT[self.__map_index]

        self.__curBaseRect=BASE_RECT_DICT[self.__map_index]

    def change_map(self):
        with open('map.txt', 'w') as f:
            f.write(str(self.__map_index))
        self.__curMap= pygame.transform.scale(pygame.image.load(os.path.join("images", "Map"+str(self.__map_index)+".png")),(self.__WIN_WIDTH,self.__WIN_HEIGHT))
        self.__curPathPage=PATH_DICT[self.__map_index]
        self.__curBaseRect=BASE_RECT_DICT[self.__map_index]
    @property
    def map_index(self):
        return self.__map_index
    
    @map_index.setter
    def map_index(self, value):
        self.__map_index=value if 1<=value<=self.__max_map_index else self.__map_index
        # self.curMap= pygame.image.load(os.path.join("images", "Map"+self.__map_index+".png"))

    @property
    def curMap(self):
        return self.__curMap
    
    @property
    def curBaseRect(self):
        return self.__curBaseRect
    
    @property
    def curPathPage(self):
        return self.__curPathPage