from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import NumericProperty, StringProperty

class Resources():
    def __init__(self, humans, food, energy, materials, physonium):
        self.humans = humans
        self.materials = materials
        self.food = food
        self.energy = energy
        self.physonium = physonium
class Planet(BoxLayout):
    number_of_planet = NumericProperty()
    # planet_resources = Resources(NumericProperty(), NumericProperty(), NumericProperty(), NumericProperty(), NumericProperty())
    status = StringProperty()
    humans = NumericProperty()
    food = NumericProperty()
    energy = NumericProperty()
    materials = NumericProperty()
    physonium = NumericProperty()
    pos_x = NumericProperty()
    pos_y = NumericProperty()





class MenuWindow(Screen):
    def __init__(self, **kwds):
        self.sound_click = SoundLoader.load('sounds/ckick.wav')
        self.sound_click.volume = 0.1
        super().__init__(**kwds)
    def ButtonClicked(self):
        self.sound_click.play()
        return
class GameWindow(Screen):
    def __init__(self, **kwds):

        self.drop_down_But1 = DropBut()



        self.sound_click = SoundLoader.load('sounds/ckick.wav')
        self.sound_click.volume = 0.1
        super().__init__(**kwds)
    def ButtonClicked(self):
        self.sound_click.play()
        return
    def ChangeSource(self):
        if (self.colonized_source_1.source == "images/planet_1_256_light.png"):
            if (self.colonized_source_2.source == "images/planet_2_256_light.png"):
                if (self.colonized_source_3.source != "images/planet_1_256_light.png"):
                    self.colonized_source_3.source = "images/planet_1_256_light.png"
            else:
                self.colonized_source_2.source = "images/planet_2_256_light.png"
        else:
            self.colonized_source_1.source = "images/planet_1_256_light.png"

    def GetCurrentHuman(self):
        return int(self.humans.text)
    def GetCurrentFood(self):
        return int(self.food.text)
    def GetCurrentEnergy(self):
        return int(self.energy.text)
    def GetCurrentMaterial(self):
        return int(self.material.text)
    def GetCurrentPhysonium(self):
        return int(self.physonium.text)
    def IsReqForPlanet_1(self):
        if (self.GetCurrentHuman() >= int(self.resources_1.values[0])) and (self.GetCurrentFood() >= int(self.resources_1.values[1])) and (self.GetCurrentEnergy() >= int(self.resources_1.values[2])) and (self.GetCurrentMaterial() >= int(self.resources_1.values[3])):
            return True
        else:
            return False
    def IsReqForPlanet_2(self):
        if (self.GetCurrentHuman() >= int(self.resources_2.values[0])) and (self.GetCurrentFood() >= int(self.resources_2.values[1])) and (self.GetCurrentEnergy() >= int(self.resources_2.values[2])) and (self.GetCurrentMaterial() >= int(self.resources_2.values[3])):
            return True
        else:
            return False
    def SpeedFood(self, *args):
        self.food_speed.text = str(args[1] * 3)
    def SpeedEnergy(self, *args):
        self.energy_speed.text = str(round(args[1] / 100 * 3, 2))
    def SpeedMaterial(self, *args):
        self.material_speed.text = str(round(args[1] / 13 * 2, 2))
    def SpeedPhysonium(self, *args):
        self.physonium_speed.text = str(round(args[1] / 100, 2))


    def TryToColonize(self, value):
        if value == 1:
            if self.IsReqForPlanet_1():
                self.planet_1_colonize.source = "images/planet_1_256_light.png"
        if value == 2:
            if self.IsReqForPlanet_2():
                self.planet_2_colonize.source = "images/planet_2_256_light.png"
        print(self.GetCurrentPhysonium())


class DropBut(Button):
    def __init__(self, **kwargs):
        super(DropBut, self).__init__(**kwargs)
        self.drop_list = None
        self.drop_list = DropDown()

        types = ['Food', 'Materials', 'People', 'Energy', 'Phusonium']

        for i in types:

            if i == "Food":
                btn = Button( size_hint_x=None, width=64 , size_hint_y=None, height=64,
                              background_normal="images/food_Icon.png")

            if i == "Materials":
                btn = Button(size_hint_x=None, width=64, size_hint_y=None, height=64,
                             background_normal="images/material_Icon.png")
            if i == "People":
                btn = Button(size_hint_x=None, width=64, size_hint_y=None, height=64,
                             background_normal="images/human_Icon2.png")
            if i == "Energy":
                btn = Button(size_hint_x=None, width=64, size_hint_y=None, height=64,
                             background_normal="images/energy_Icon.png")
            if i == "Phusonium":
                btn = Button(size_hint_x=None, width=64, size_hint_y=None, height=64,
                             background_normal="images/physonium_Icon.png")


            self.drop_list.add_widget(btn)

            tx = Label(text="1203")
            self.drop_list.add_widget(tx)


        self.bind(on_release=self.drop_list.open)


        #self.drop_list.bind(on_select=lambda instance, x: setattr(self, 'text', x))

def PlaySound(sound):
    sound.play()
class SettingsWindow(Screen):
    def __init__(self, **kwds):
        # music
        self.music = SoundLoader.load('music/ebackground.wav')
        self.music.volume = 0
        self.music.bind(on_stop=PlaySound)
        self.music.play()
        # click
        self.sound_click = SoundLoader.load('sounds/ckick.wav')
        self.sound_click.volume = 0.1
        super().__init__(**kwds)

    def ChangeMainVolume(self, *args ):
        self.slide_main_volume.text = str(int(args[1]))
        # print(args[1])

        self.sound_click.volume = args[1] / 100

    def ChangeMusicVolume(self, *args):
        self.slide_music_volume.text = str(int(args[1]))
        # print(args[1])

        self.music.volume = args[1] / 100 * 0.1

    def ButtonClicked(self):
        self.sound_click.play()
        return

class MyDropDown(DropDown):
    pass

class WindowManager(ScreenManager):
    pass

