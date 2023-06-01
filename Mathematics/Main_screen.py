from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
)
from kivy.vector import Vector
from kivy.clock import Clock

from transformations import Physics
from main import GameApp

phys = Physics()

class Dynamics (Widget):
    image_source = StringProperty("")
    velocity_x = NumericProperty(0.2)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):

        self.pos = Vector(*self.velocity) + self.pos


class Scene_2(Screen):
    def update(self, dt):
        pass
class Scene (Screen):
    planet1 = ObjectProperty('planet1')
    planet2 = ObjectProperty('planet2')
    star = ObjectProperty('star')
    def update (self, dt):
        ax = phys.get_function('Ax', x=self.planet1.pos[0], y=self.planet1.pos[1], x0=self.center_x, y0=self.center_y)
        self.planet1.velocity_x += ax * dt
        ay = phys.get_function('Ay', x=self.planet1.pos[0], y=self.planet1.pos[1], x0=self.center_x, y0=self.center_y)
        self.planet1.velocity_y += ay * dt
        self.planet1.move()
        ax = phys.get_function('Ax', x=self.planet2.pos[0], y=self.planet2.pos[1], x0=self.center_x, y0=self.center_y)
        self.planet2.velocity_x += ax * dt
        ay = phys.get_function('Ay', x=self.planet2.pos[0], y=self.planet2.pos[1], x0=self.center_x, y0=self.center_y)
        self.planet2.velocity_y += ay * dt
        self.planet2.move()


class Main_sApp(App):

    def build(self):
        game = GameManager()
        game.add_widget(Scene())
        game.add_widget(Scene_2())
        Clock.schedule_interval(game.update, 1.0/60)

        return game

class GameManager(ScreenManager):
    def update(self, dt):
        self.current_screen.update(dt)



if __name__ == '__main__':
    Main_sApp().run()