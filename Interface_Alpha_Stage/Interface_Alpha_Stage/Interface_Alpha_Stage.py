import sys
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
kivy.require('1.0.6') # replace with your current kivy version !


class carloangui(BoxLayout):
    pass

    def __init__(self, **kwargs):
        super(carloangui,self).__init__(**kwargs)
        print('The button <%s> is being pressed')

        btn1 = Button(text='Hello world 1',
                      background_color=(0, 0, 1, 1))
        btn1.bind(on_press=self.clk)
        self.add_widget(btn1)
        btn2 = Button(text='Kill')
        btn2.bind(on_press=self.quit)
        self.add_widget(btn2)
    def clk(self,obj):
        print("Hello,World")
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
