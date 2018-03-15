import sys
import math
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.image import Image
kivy.require('1.0.6') # replace with your current kivy version !

class FullImage(Image):
    pass

class carloangui(BoxLayout):
    pass

    def __init__(self, **kwargs):
        super(carloangui,self).__init__(**kwargs)
        print('The button <%s> is being pressed')
        wimg= Image(source='C:\\Users\\SIM\\Desktop\\3.jpg')
        self.add_widget(wimg)
        btn1 = Button(text='Hello world 1',
                      background_color=(0, 0, 1, 1),
                      pos=(200,50),
                      size_hint=(.1,.1))
        btn1.bind(on_press=self.clk)
        self.add_widget(btn1)
        btn2 = Button(text='Kill',
                      pos=(50,200),
                      size_hint=(.1,.1))
        btn2.bind(on_press=self.quit)
        self.add_widget(btn2)
        
        
    def clk(self,obj):
        print("Hello,World")
        popup=Popup(title="Test",
               content=Label(text="Hello,world"),
               size_hint=(None,None),
               size=(400,400))
        popup.open()
    def quit(self,obj):
        sys.exit()



class open(App):
    def build(self):
        cl=carloangui()
        return cl

if __name__ == '__main__':
    open().run()
print("***************************************************************** \n" + " \n\n                         Car Loan Calculator                               ")
print("\n \n \n*****************************************************************")
