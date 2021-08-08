import pygame

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
    
