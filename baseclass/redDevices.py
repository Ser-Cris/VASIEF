from  kivymd.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from  kivy.uix.screenmanager import ScreenManager,Screen
class redDevices(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.add = MDApp.get_running_app()
        self.sub_title = "Dispositivos de Red conectados"
        self.crearCards()

    def crearCards(self,**kwargs):
        for i in range(10):
            self.raul = str(i)
            print (i)

