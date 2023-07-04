from kivy.clock import Clock
from kivy.app import App
from kivy.lang import Builder
from Mathematics.transformations import Physics
from windows import WindowManager
from windows import DataBase
# from windows import PlanetData
kv = Builder.load_file('windows.kv')
phys = Physics()
FPS = 60


class GameApp(App):
    # planet_data = DataBase
    first_planet = DataBase.planet_1
    second_planet = DataBase.planet_2
    third_planet = DataBase.planet_3
    # manager = WindowManager

    def build(self, **kwargs):
        return kv

    def on_start(self):
        self.time = 0

    def update(self, dt):
        self.time += dt
        self.root.ids['MapOfPlanets_window'].ids['clock'].text = f"{self.time: .0f}"
        # self.manager.update_info(self, dt)
        self.first_planet.update(dt)
        self.second_planet.update(dt)
        self.third_planet.update(dt)
        # window_manager's update

       # self.root.ids['game_window'].ids['food_amount'].text =  str(int(self.root.ids['game_window'].ids['food_amount'].text) +int(phys.get_function('food', t = self.time, p = int(self.root.ids['game_window'].ids['food/humans'].value), P= int(self.root.ids['game_window'].ids['humans_amount'].text))))
       #self.root.ids['game_window'].ids['energy_amount'].text = str(int(self.root.ids['game_window'].ids['energy_amount'].text) + int(phys.get_function('energy', t=self.time, p=int(self.root.ids['game_window'].ids['energy/humans'].value))))
       # self.root.ids['game_window'].ids['humans_amount'].text = str(int(phys.get_function('population', t = self.time, food=int(self.root.ids['game_window'].ids['food_amount'].text), energy=int(self.root.ids['game_window'].ids['energy_amount'].text))))
       # self.root.ids['game_window'].ids['material_amount'].text = str(int(self.root.ids['game_window'].ids['material_amount'].text) + int(phys.get_function('resources', t=self.time, people=int(self.root.ids['game_window'].ids['material/humans'].value), energy=int(self.root.ids['game_window'].ids['energy_amount'].text))))


if __name__ == '__main__':
    app = GameApp()
    Clock.schedule_interval(app.update, 1/FPS)
    app.run()
