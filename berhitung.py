from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

class Math(Screen):
    pass

class Berhitung(Screen):
    pass

class Pengaturan(Screen):
    pass

class MathApp(MDApp):
    def build(self):

        sm = ScreenManager()
        sm.add_widget(Math(name='math'))
        sm.add_widget(Berhitung(name='berhitung'))
        sm.add_widget(Pengaturan(name='pengaturan'))

        return sm
    
if __name__ == "__main__":
    MathApp().run()
