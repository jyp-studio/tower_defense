import pygame
import os
from menu.menus import Button
from settings import singleton_vol_controller,singleton_map_controller
from game.user_request import RequestSubject,MinusVolume,AddVolume,Back,MinusMapIndex,AddMapIndex,GoStartMenu

class OptMenuModel:
    def __init__(self):
        self.back_game=False
        self.back_start_menu=False

        self.sound = pygame.mixer.Sound("./sound/sound.mp3")
        self.sound.set_volume(singleton_vol_controller.sound_volume)

        self.minus_img=pygame.transform.scale(pygame.image.load(os.path.join("images", "minus.png")), (50, 50))
        self.add_img=pygame.transform.scale(pygame.image.load(os.path.join("images", "add.png")), (50, 50))
        self.back_img=pygame.transform.scale(pygame.image.load(os.path.join("images", "back.png")), (150, 50))
        self.menu_img=pygame.transform.scale(pygame.image.load(os.path.join("images", "menu.png")), (150, 50))
        self.left_img=pygame.transform.scale(pygame.image.load(os.path.join("images", "left.png")), (50, 50))
        self.right_img=pygame.transform.scale(pygame.image.load(os.path.join("images", "right.png")), (50, 50))

        self.map_preview_img=pygame.transform.scale(pygame.image.load(os.path.join("images", "Map"+str(singleton_map_controller.map_index)+".png")), (500, 300))

        self.minusSoundVol_btn=Button(self.minus_img,"minusSound",349, 355)  # image, name: str, x: int, y: int
        self.addSoundVol_btn=Button(self.add_img,"addSound",399, 355)  

        self.minusMusicVol_btn=Button(self.minus_img,"minusMusic",349, 430)  
        self.addMusicVol_btn=Button(self.add_img,"addMusic",399, 430)

        self.back_btn=Button(self.back_img,"back",300, 500)
        self.menu_btn=Button(self.menu_img,"goStartMenu",700,500)

        self.left_btn=Button(self.left_img,"minusMapIndex",200,160)
        self.right_btn=Button(self.right_img,"addMapIndex",825,160)

        self.buttons = [self.minusSoundVol_btn,
                        self.addSoundVol_btn,
                        self.minusMusicVol_btn,
                        self.addMusicVol_btn,
                        self.back_btn,
                        self.menu_btn,
                        self.left_btn,
                        self.right_btn]

        self.selected_button = None

        self.subject = RequestSubject(self)
        self.minusVolumer = MinusVolume(self.subject)
        self.addVolumer = AddVolume(self.subject)
        self.backListener = Back(self.subject)
        self.minusMapIndex = MinusMapIndex(self.subject)
        self.addMapIndex = AddMapIndex(self.subject)
        self.goStartMenu = GoStartMenu(self.subject)

    def user_request(self, user_request: str):
        """ add tower, sell tower, upgrade tower"""
        self.subject.notify(user_request)

    def get_request(self, events: dict) -> str:
        """get keyboard response or button response"""
        # initial
        self.selected_button = None
    
        # mouse event
        if events["mouse position"] is not None:
            x, y = events["mouse position"]
            self.select(x, y)
            if self.selected_button is not None:
                return self.selected_button.response
            return "nothing"
        return "nothing"

    def select(self, mouse_x: int, mouse_y: int) -> None:
        """change the state of whether the items are selected"""
        for btn in self.buttons:
            if btn.clicked(mouse_x, mouse_y):
                self.selected_button = btn