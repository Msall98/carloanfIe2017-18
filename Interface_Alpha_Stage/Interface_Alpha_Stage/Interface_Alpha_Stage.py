import sys
import math
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
kivy.require('1.0.6') # replace with your current kivy version !
Builder.load_string('''
<CustomLayout>
    canvas.before:
        BorderImage:
            # BorderImage behaves like the CSS BorderImage
            border: 00, 00, 00, 00
            texture: self.background_image.texture
            pos: self.pos
            size: self.size

<RootWidget>
    CustomLayout:

        pos_hint: {'center_x': .5, 'center_y': .5}
        rows:1         
                      

<TextInput>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
''')

class CustomLayout(GridLayout):

    background_image = ObjectProperty(Image(source='C:\\Users\\SIM\\Desktop\\3.jpg'))
class RootWidget(FloatLayout):
    pass
class carloangui(BoxLayout):
    pass

    def __init__(self, **kwargs):
        
        global wimg
        super(carloangui,self).__init__(**kwargs)
        print('The button <%s> is being pressed')
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
        
    def quit(self,obj):
        sys.exit()



class open(App):
    def build(self):
        cl=carloangui()
        return RootWidget()

if __name__ == '__main__':
    open().run()
print("***************************************************************** \n" + " \n\n                         Car Loan Calculator                               ")
print("\n \n \n*****************************************************************")
