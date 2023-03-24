from kivy.clock import Clock
from kivy.app import App
from kivy.lang import Builder
from windows import *
kv = Builder.load_file('windows.kv')

FPS = 60

class GameApp(App):
    def build(self, **kwargs):
        return kv
    def on_start(self):
        self.time = 0

    def update(self, dt):
        self.time += dt / 5
        self.root.ids['game_window'].ids['clock'].text = f"{self.time: .0f}"



if __name__ == '__main__':
    app = GameApp()
    Clock.schedule_interval(app.update, 1/FPS)
    app.run()
