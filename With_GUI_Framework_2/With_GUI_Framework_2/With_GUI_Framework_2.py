import sys
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_string('''
<Kill>
    Button:
        text: 'Quit'
        background_color: 0,0,1,1
        
<Calculation>
    Button:
        text: 'Calculate'
        background_color: 1,1,1,1
''')