import pygame
from tower.towers import Tower, Vacancy

"""This module is import in model.py"""

"""
Here we demonstrate how does the Observer Pattern work
Once the subject updates, if will notify all the observer who has register the subject
"""


class RequestSubject:
    def __init__(self, model):
        self.__observers = []
        self.model = model

    def register(self, observer):
        self.__observers.append(observer)

    def notify(self, user_request):
        for o in self.__observers:
            o.update(user_request, self.model)


class EnemyGenerator:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """add new enemy"""
        if user_request == "start new wave":
            if model.enemies.is_empty():
                model.enemies.add(10)
                model.wave += 1


class TowerSeller:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """sell tower"""
        if user_request == "sell":
            x, y = model.selected_tower.rect.center
            model.money += model.selected_tower.get_cost()
            model.plots.append(Vacancy(x, y))
            model.towers.remove(model.selected_tower)
            model.selected_tower = None


class TowerDeveloper:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        if user_request == "upgrade" and model.selected_tower.level < 5:
            if model.money >= model.selected_tower.get_cost():
                model.money -= model.selected_tower.get_cost()
                model.selected_tower.level += 1
            # if the money > upgrade cost of the selected tower , level+1
            # use model.selected_tower to access the selected tower data
            # use model.money to access to money data


class TowerFactory:
    def __init__(self, subject):
        subject.register(self)
        self.tower_name = ["moon_tower", "red_fire_tower", "blue_fire_tower", "obelisk_tower"]

    def update(self, user_request: str, model):
        """add new tower"""
        for name in self.tower_name:
            if user_request == name:
                x, y = model.selected_plot.rect.center
                tower_dict = {"moon_tower": Tower.moon_tower(x, y), "red_fire_tower": Tower.red_fire_tower(x, y),
                              "blue_fire_tower": Tower.blue_fire_tower(x, y), "obelisk_tower":Tower.obelisk_tower(x, y)}
                new_tower = tower_dict[user_request]
                if model.money > new_tower.get_cost():
                    model.money -= new_tower.get_cost()
                    model.towers.append(new_tower)
                    model.plots.remove(model.selected_plot)
                    model.selected_plot = None


class Music:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music on"""
        if user_request == "music":
            pygame.mixer.music.unpause()
            model.sound.play()


class Muse:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music off"""
        if user_request == "mute":
            pygame.mixer.music.pause()
            model.sound.play()

