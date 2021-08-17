import pygame
import math

numofwords=26   #number of words in a line
def str_divide(sentense):   #divide a string into lots of lines
    lines=[]
    for i in range(0,math.ceil(len(sentense)/numofwords)):
        tail=min((i+1)*numofwords,len(sentense))
        lines.append(sentense[i*numofwords:tail])
    return lines


blood_pot_info = "Recover 1 HP"
aoe_pot_info = "Attack all enemy without boss and cause 30% max HP damage"
kill_pot_info = "Pay 5 HP, kill all enemies except boss"
slow_pot_info = "Slow down all enemies"
boss_pot_info = "Attack bosses and cause 50% max HP damage"
tower_pot_info = "Increase the attack speed of all towers by 5 (one time only)"
POTION_INFO_DICT={
    "blood_potion":str_divide(blood_pot_info),
    "aoe_potion":str_divide(aoe_pot_info),
    "kill_potion":str_divide(kill_pot_info),
    "slow_potion":str_divide(slow_pot_info),
    "boss_potion":str_divide(boss_pot_info),
    "tower_potion":str_divide(tower_pot_info)
}


class PotionInfo:
    def __init__(self,potion_btn):
        self.name=potion_btn.name
        self.info=POTION_INFO_DICT[potion_btn.name]
        self.rect=pygame.Rect(potion_btn.rect)
        x,y=self.rect.center
        self.rect.center=(x+70,y)