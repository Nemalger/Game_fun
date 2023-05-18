from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import NumericProperty, StringProperty
#
# class Resources():
#     def __init__(self, humans, food, energy, materials, physonium):
#         self.humans = humans
#         self.materials = materials
#         self.food = food
#         self.energy = energy
#         self.physonium = physonium
class Planet(BoxLayout):
    number_of_planet = NumericProperty()

    status = StringProperty()
    humans = NumericProperty()
    food = NumericProperty()
    energy = NumericProperty()
    materials = NumericProperty()
    physonium = NumericProperty()
    im_source = StringProperty()

    pos_x = NumericProperty()
    pos_y = NumericProperty()


class PlanetData:
    def __init__(self, num, status, humans, food, energy, materials, physonium, food_factory, energy_factory, materials_factory, physonium_factory):
        self.num_of_planet = num
        self.status = status
        self.humans = humans
        self.food = food
        self.energy = energy
        self.materials = materials
        self.physonium = physonium
        self.food_factory = food_factory
        self.energy_factory = energy_factory
        self.materials_factory = materials_factory
        self.physonium_factory = physonium_factory

    def update(self, dt):
        pass

class DataBase:

    planet_1 = PlanetData(1, "Colonized", 2000, 3000, 200, 40, 0, 1, 0, 0, 0)
    planet_2 = PlanetData(2, "Not colonized", 0, 4000, 1000, 160, 23, 0, 0, 0, 0)
    planet_3 = PlanetData(3, "Not colonized", 0, 8000, 2000, 520, 80, 0, 0, 0, 0)
    def get_planet(self, index):
        if index == 1:
            return self.planet_1
        elif index == 2:
            return self.planet_2
        elif index == 3:
            return self.planet_3

class PlanetInfoWindow(Screen):
    def __init__(self, **kwds):
        self.sound_click = SoundLoader.load('sounds/ckick.wav')
        self.sound_click.volume = 0.1
        self.current_planet = 1
        super().__init__(**kwds)
    def ButtonClicked(self):
        self.sound_click.play()
        return
    def update_planet(self, num):

        current = self.parent.planets_data.get_planet(num)
        self.ids['showing_planet'].number_of_planet = num
        self.ids['showing_planet'].status = current.status
        self.ids['showing_planet'].humans = current.humans
        self.ids['showing_planet'].food = current.food
        self.ids['showing_planet'].energy = current.energy
        self.ids['showing_planet'].materials = current.materials
        self.ids['showing_planet'].physonium = current.physonium
        self.ids['food_factory'].text = str(current.food_factory)
        self.ids['energy_factory'].text = str(current.energy_factory)
        self.ids['materials_factory'].text = str(current.materials_factory)
        self.ids['physonium_factory'].text = str(current.physonium_factory)
        if current.status == "Colonized":
            self.ids['showing_planet'].im_source = f"images/planet_{num}_256_light.png"
        elif current.status == "Not colonized":
            self.ids['showing_planet'].im_source = f"images/planet_{num}_256_dark.png"


class MenuWindow(Screen):
    def __init__(self, **kwds):

        self.sound_click = SoundLoader.load('sounds/ckick.wav')
        self.sound_click.volume = 0.1
        super().__init__(**kwds)

    def ButtonClicked(self):
        self.sound_click.play()
        return
class MapOfPlanetsWindow(Screen):
    def __init__(self, **kwds):
        self.drop_down_But1 = DropBut()
        self.sound_click = SoundLoader.load('sounds/ckick.wav')
        self.sound_click.volume = 0.1
        super().__init__(**kwds)

    # def to_planet_info(self, number_of_planet):
    #     planet = self.root.parent.planets_data.get_planet(number_of_planet)

    def ButtonClicked(self):
        self.sound_click.play()
        return
    # def ChangeSource(self):
    #     if (self.colonized_source_1.source == "images/planet_1_256_light.png"):
    #         if (self.colonized_source_2.source == "images/planet_2_256_light.png"):
    #             if (self.colonized_source_3.source != "images/planet_1_256_light.png"):
    #                 self.colonized_source_3.source = "images/planet_1_256_light.png"
    #         else:
    #             self.colonized_source_2.source = "images/planet_2_256_light.png"
    #     else:
    #         self.colonized_source_1.source = "images/planet_1_256_light.png"


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
        # self.drop_list.container = BoxLayout()§
        # self.drop_list.on_container(self.drop_list, self.drop_list.container)
        self.drop_list.bind(container=BoxLayout)


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

# class ShuttleWindow(Screen):
#     def __init__(self, **kwds):
#         self.sound_click = SoundLoader.load('sounds/ckick.wav')
#         self.sound_click.volume = 0.1
#         super().__init__(**kwds)


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
    current_planet = 1
    planets_data = DataBase()

    def to_planet_info(self, number):
        #self.ids["PlanetInfo"].current_planet = number
        self.current_planet = number

