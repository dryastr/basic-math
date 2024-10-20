from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.lang import Builder

class HomeGame(Screen):
    pass

class MathGame(Screen):
    pass

class BerhitungGame(Screen):
    pass

class PengaturanGame(Screen):
    pass

class MathApp(MDApp):
    def build(self):
        self.backsound = SoundLoader.load('opening.wav')
        if self.backsound:
            self.backsound.loop = True
            self.backsound.play()

        return Builder.load_file('math.kv')

if __name__ == "__main__":
    MathApp().run()
