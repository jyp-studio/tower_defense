import pygame
import math

numofwords=26   #number of words in a line
def str_divide(sentense):   #divide a string into lots of lines
    lines=[]
    for i in range(0,math.ceil(len(sentense)/numofwords)):
        tail=min((i+1)*numofwords,len(sentense))
        lines.append(sentense[i*numofwords:tail])
    return lines

blood_pot_info="Recover 1 HP and pay $2000"
aoe_pot_info  ="Attack all enemy by their 10% HP and pay $2000"
POTION_INFO_DICT={
    "blood_potion":str_divide(blood_pot_info),
    "aoe_potion":str_divide(aoe_pot_info)
}

class PotionInfo:
    def __init__(self,potion_btn):
        self.name=potion_btn.name
        self.info=POTION_INFO_DICT[potion_btn.name]
        self.rect=pygame.Rect(potion_btn.rect)
        x,y=self.rect.center
        self.rect.center=(x+70,y)