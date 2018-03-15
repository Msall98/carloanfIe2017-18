import sys
import math
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.lang.builder import Builder
kivy.require('1.0.6') # replace with your current kivy version !
Builder.load_string('''
<-FullImage>:
    canvas:
        Color:
            rgb: (1, 1, 1)
        Rectangle:
            texture: self.texture
            size: self.width + 20, self.height + 20
            pos: self.x - 10, self.y - 10
''')

class FullImage(Image):
    pass
class carloangui(BoxLayout):
    pass

    def __init__(self, **kwargs):
        
        global wimg
        super(carloangui,self).__init__(**kwargs)
        print('The button <%s> is being pressed')
        wimg= Image(source='C:\\Users\\SIM\\Desktop\\3.jpg',
                    )
        self.add_widget(wimg)
        btn1 = Button(text='Hello world 1',
                      background_color=(0, 0, 1, 1),
                      pos=(500,50),
                      size_hint=(.1,.1))
        btn1.bind(on_press=self.clk)
        self.add_widget(btn1)
        btn2 = Button(text='Kill',
                      pos=(50,200),
                      size_hint=(.1,.1))
        btn2.bind(on_press=self.quit)
        self.add_widget(btn2)
        self.txt1 = TextInput(text='', multiline=False)
        self.add_widget(self.txt1)
        btn3 =Button(text='Show',
                      pos=(300,200),
                      size_hint=(.1,.1))
        btn3.bind(on_press=self.gclk)
        self.add_widget(btn3)
        
    def gclk(self,btn):
        print(self.txt1.text)
        popup=Popup(title="Test",
               content=Label(text=self.txt1.text),
               size_hint=(None,None),
               size=(400,400))
        popup.open()
        
    def clk(self,obj):
        print("Hello,World")
        popup=Popup(title="Test",
               content=Label(text="Hello,world"),
               size_hint=(None,None),
               size=(400,400))
        popup.open()
        popup2=Popup(title="test",
                     content=Label(text="Hi"),
                     size_hint=(None,None),
                     size=(400,400))
        popup2.open()
        btn1 = Button(text='Testing',
                      background_color=(0, 0, 1, 1),
                      pos=(500,50),
                      size_hint=(.1,.1))
        btn1.bind(on_press=self.clk)
        self.remove_widget(wimg)
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
