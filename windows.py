
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader

class MenuWindow(Screen):
    def __init__(self, **kwds):
        self.sound_click = SoundLoader.load('venv/sounds/ckick.wav')
        self.sound_click.volume = 0.1
        super().__init__(**kwds)
    def ButtonClicked(self):
        self.sound_click.play()
        return
class GameWindow(Screen):
    def __init__(self, **kwds):
        self.sound_click = SoundLoader.load('venv/sounds/ckick.wav')
        self.sound_click.volume = 0.1
        super().__init__(**kwds)
    def ButtonClicked(self):
        self.sound_click.play()
        return
    def ChangeSource(self):
        if (self.colonized_source_1.source == "venv/images/planet_1_256_light.png"):
            if (self.colonized_source_2.source == "venv/images/planet_2_256_light.png"):
                if (self.colonized_source_3.source != "venv/images/planet_1_256_light.png"):
                    self.colonized_source_3.source = "venv/images/planet_1_256_light.png"
            else:
                self.colonized_source_2.source = "venv/images/planet_2_256_light.png"
        else:
            self.colonized_source_1.source = "venv/images/planet_1_256_light.png"


def PlaySound(sound):
    sound.play()
class SettingsWindow(Screen):
    def __init__(self, **kwds):
        # music
        self.music = SoundLoader.load('venv/music/ebackground.wav')
        self.music.volume = 0
        self.music.bind(on_stop=PlaySound)
        self.music.play()
        # click
        self.sound_click = SoundLoader.load('venv/sounds/ckick.wav')
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


class WindowManager(ScreenManager):
    pass

