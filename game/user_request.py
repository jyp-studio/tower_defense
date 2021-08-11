from __future__ import annotations
from tower.blue import *
from tower.red import *
from tower.moon import *
from tower.obelisk import *
from settings import singleton_vol_controller,singleton_map_controller,game_status,potion_price

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

    def notify(self, user_request:str):
        for o in self.__observers:
            o.update(user_request, self.model)


class EnemyGenerator:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """add new enemy"""
        if user_request == "start new wave":
            if model.enemies.is_empty():
                if 0 < model.wave % 7 <= 3:
                    model.enemies.add(10 * model.wave)
                elif model.wave % 7 == 5:
                    model.enemies.add(4)
                elif model.wave % 7 == 6:
                    model.enemies.add(1)
                else:
                    model.enemies.add(10 * (model.wave + 1))
                model.wave += 1


class HealthUp:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """add new enemy"""
        if user_request == "health up" and model.hp < 10:
            model.hp += 1


class AddMoney:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """add money"""
        if user_request == "add money":
            model.money = 99999999999


class KillAll:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """kill all enemies"""
        if user_request == "kill all":
            model.enemies.retreat_all()


class AddTowers:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """Add obelisks tower"""
        if user_request == "add towers":
            for tw in model.towers:
                x, y = tw.rect.center
                if tw.name == "Moon Tower":
                    model.plots.append(Vacancy(x - 18, y))
                elif tw.name == "Obelisk Tower":
                    model.plots.append(Vacancy(x, y + 50))
                else:
                    model.plots.append(Vacancy(x - 20, y + 5))
                model.towers.remove(tw)

            for plot in model.plots:
                x, y = plot.rect.center
                tower_dict = {"moon": MoonTower(x + 18, y),
                              "red fire": RedFireTower(x + 20, y - 5),
                              "blue fire": BlueFireTower(x + 20, y - 5),
                              "obelisk": ObeliskTower(x, y - 50)}
                ran_tower = random.choice(["moon", "red fire", "blue fire", "obelisk"])
                new_tower = tower_dict[ran_tower]
                model.towers.append(new_tower)
            model.plots.clear()


class TowerSeller:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """sell tower"""
        if user_request == "sell":
            x, y = model.selected_tower.rect.center
            model.money += model.selected_tower.get_sell_price()
            ####
            if model.selected_tower.name == "Moon Tower":
                model.plots.append(Vacancy(x - 18, y))
            elif model.selected_tower.name == "Obelisk Tower":
                model.plots.append(Vacancy(x, y + 50))
            else:
                model.plots.append(Vacancy(x - 20, y + 5))
            model.towers.remove(model.selected_tower)
            model.selected_tower = None


class TowerDeveloper:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        if user_request == "upgrade" and model.selected_tower.level < 5:
            if model.money >= model.selected_tower.get_upgrade_cost():
                model.money -= model.selected_tower.get_upgrade_cost()
                model.selected_tower.level += 1
            # if the money > upgrade cost of the selected tower , level+1
            # use model.selected_tower to access the selected tower data
            # use model.money to access to money data


class TowerEvolution:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        if user_request == "ultra" and model.selected_tower.level == 5:
            if model.money >= model.selected_tower.get_ultra_cost():
                model.money -= model.selected_tower.get_ultra_cost()
                model.selected_tower.level = 6


class TowerProperties:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        if user_request == "properties":
            model.show_tower_info = True


class TowerFactory:
    def __init__(self, subject:RequestSubject):
        subject.register(self)
        self.tower_name = ["moon", "red fire", "blue fire", "obelisk"]

    def update(self, user_request: str, model):
        """add new tower"""
        for name in self.tower_name:
            if user_request == name:
                if model.selected_plot is not None:
                    x, y = model.selected_plot.rect.center
                    tower_dict = {"moon": MoonTower(x + 18, y),
                                  "red fire": RedFireTower(x + 20, y - 5),
                                  "blue fire": BlueFireTower(x + 20, y - 5),
                                  "obelisk": ObeliskTower(x, y - 50)}
                    new_tower = tower_dict[user_request]
                    if model.money >= new_tower.get_cost():
                        model.money -= new_tower.get_cost()
                        model.towers.append(new_tower)
                        model.plots.remove(model.selected_plot)
                        model.selected_plot = None


class Music:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music on"""
        if user_request == "music":
            pygame.mixer.music.unpause()
            model.sound.play()


class Muse:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music off"""
        if user_request == "mute":
            pygame.mixer.music.pause()
            model.sound.play()


class MinusVolume:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """minusSound"""
        if user_request == "minusSound":
            singleton_vol_controller.minusVol(model.sound,0.05)
            model.sound.play()
        elif user_request == "minusMusic":
            singleton_vol_controller.minusVol(pygame.mixer.music,0.05)
            model.sound.play()


class AddVolume:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """addSound"""
        if user_request == "addSound":
            singleton_vol_controller.addVol(model.sound,0.05)
            model.sound.play()
        elif user_request == "addMusic":
            singleton_vol_controller.addVol(pygame.mixer.music,0.05)
            model.sound.play()


class Back:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """back"""
        if user_request == "back":
            model.back_game=True
            model.sound.play()


class Pause:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """pause"""
        if user_request == "pause":
            model.sound.play()
            model.opt_menu.run()
            model.sound.set_volume(singleton_vol_controller.sound_volume)


class MinusMapIndex:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """minusMapIndex"""
        if user_request == "minusMapIndex":
            model.sound.play()
            singleton_map_controller.map_index-=1
            model.map_preview_img=pygame.transform.scale(pygame.image.load(os.path.join("images", "Map"+str(singleton_map_controller.map_index)+".png")), (500, 300))


class AddMapIndex:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """AddMapIndex"""
        if user_request == "addMapIndex":
            model.sound.play()
            singleton_map_controller.map_index+=1
            model.map_preview_img=pygame.transform.scale(pygame.image.load(os.path.join("images", "Map"+str(singleton_map_controller.map_index)+".png")), (500, 300))


class GoStartMenu:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """Change var game_status["go_start_menu"] in settings.py"""
        if user_request == "goStartMenu":
            model.sound.play()
            game_status["go_start_menu"] = True

class Die:
    def __init__(self, subject:RequestSubject):
        subject.register(self)

    def update(self, user_request: str, model):
        """deal with event: die by call GameOver.run()"""
        if user_request == "die":
            model.GameOverMenu.run()

class Potionfunction:
    def __init__(self, subject:RequestSubject):
       subject.register(self)
    
    def update(self, user_request: str, model):

        if user_request == "blood_potion":
            if model.hp < model.max_hp and model.money >= potion_price["blood_potion"]:
                model.hp += 1
                model.money -= potion_price["blood_potion"]
                model.sound.play()
        if user_request == "aoe_potion":
            if model.money >= potion_price["aoe_potion"]:
                for en in model.enemies.get():
                    en.health -= en.max_health/10
                model.money -= potion_price["aoe_potion"]
                model.sound.play()