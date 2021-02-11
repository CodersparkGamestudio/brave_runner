import kivy
from kivy import Config
from kivy.app import App
from kivy.uix.label import Label

kivy.require('2.0.0')

class SimpleKivy(App): 
    def build(self):
        return Label(text="Hello World!")

SimpleKivy().run()