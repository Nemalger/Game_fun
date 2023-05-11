from dataclasses import dataclass

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen

# from kivy.properties import NumericProperty, ObjectProperty

FPS = 60


class GameApp(App):
    def on_start(self):
        self.time = 0

    def update(self, dt):
        self.time += dt
        self.root.ids.planet_window.update(dt)


class WindowManager(ScreenManager):
    pass


class MenuWindow(Screen):
    pass


class PlanetWindow(Screen):
    # planet = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.planet = Planet(name="Earth")

    def update(self, dt):
        self.planet.update(dt)
        self.ids.population_count.text = f"Population: {self.planet.population}"
        self.ids.food.text = f"Food amount: {self.planet.food_amount}"
        self.ids.energy.text = f"Energy amount: {self.planet.energy_amount}"
        self.ids.materials.text = f"Materials amount: {self.planet.material_amount}"


@dataclass
class Planet:
    name: str
    food_amount: int = 0
    energy_amount: int = 0
    material_amount: int = 0
    physonium_amount: int = 0
    population: int = 0  # NumericProperty(0)

    def update(self, dt):
        self.population += max(1, int(self.dp_dt(self.population) * dt))
        self.food_amount += max(1, int(self.dp_dt(self.food_amount) * dt))
        self.energy_amount += max(1, int(self.dp_dt(self.energy_amount) * dt))
        self.material_amount += max(1, int(self.dp_dt(self.material_amount) * dt))
        self.physonium_amount += max(1, int(self.dp_dt(self.physonium_amount) * dt))

    def dp_dt(self, p):
        return p // 100


app = GameApp()
Clock.schedule_interval(app.update, 1 / FPS)
app.run()
