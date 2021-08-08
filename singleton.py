import pygame
import os

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
    def __init__(self):
        self.__map_index=1
        with open('map.txt', 'r') as f:
            self.__map_index=int(f.read())
        self.__map_index=self.__map_index if 1<=self.__map_index<=self.__max_map_index else 1
        self.__curMap= pygame.image.load(os.path.join("images", "Map"+str(self.__map_index)+".png"))
    
    def change_map(self):
        with open('map.txt', 'w') as f:
            print(self.__map_index)
            f.write(str(self.__map_index))
        self.__curMap= pygame.image.load(os.path.join("images", "Map"+str(self.__map_index)+".png"))
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