from kivymd.app import MDApp
from kivy.lang import Builder
from  kivy.uix.screenmanager import ScreenManager,Screen
from  kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from baseclass.principal import Principal
from baseclass.redDevices import redDevices


class MyApp(MDApp):
    def build(self):
        self.title="VASIEF-SNMP"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file("main.kv")

MyApp().run()