from kivy.app import App
from kivy.lang import Builder
from windows import *
kv = Builder.load_file('windows.kv')

class GameApp(App):
    def build(self, **kwargs):
        return kv

if __name__ == '__main__':
    GameApp().run();