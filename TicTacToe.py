import kivy
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
#from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import time
import random
from kivy.graphics import Color, Line
from kivy.properties import ListProperty
from kivy.factory import Factory
from kivy.lang import Builder
#import sys

Builder.load_string("""
<LabelB>:
  bcolor: 1, 1, 1, 1
  canvas.before:
    Color:
      rgba: self.bcolor
    Rectangle:
      pos: self.pos
      size: self.size
""")

class LabelB(Label):
  bcolor = ListProperty([1,0,0,1])

Factory.register('KivyB', module='LabelB')

class MainPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.last_button = []
        self.white = []
        self.black = []
        self.count = 0
        self.victory = [
                [1, 4, 7],
                [2, 5, 8],
                [3, 6, 9],
                [1, 5, 9],
                [3, 5, 7],
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                ]
        buttons = [
                ["1", "2", "3"],
                ["4", "5", "6"],
                ["7", "8", "9"],
                ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                self.btn = Button(text=label, pos_hint = {'center_x' : 0.5, 'center_y' : 0.5}, color = (0, 0, 0, 0))
                self.btn.bind(on_press = self.on_press_button)
                h_layout.add_widget(self.btn)
            self.add_widget(h_layout)        
        self.label_1 = Label(text=f"{myapp.first_page.lab1} starts first!!", font_size = 45)
        self.add_widget(self.label_1)
    def on_press_button(self, instance):
        if instance.text in self.last_button:
            self.count = self.count + 1
            if self.count > 2 and self.count <= 4:
                self.label_1.text = "Quit Messing Around!"
            elif self.count > 5 and self.count < 9:
                self.label_1.text = "Stop it!!"
            elif self.count >= 9:
                self.label_1.text = "Screw this!!"
            return
        self.last_button.append(instance.text)
        if len(self.last_button)%2 != 0:
            self.label_1.text = f"{myapp.first_page.lab2}'s Turn!"
 #           instance.background_color = (255, 255, 255, 1)
            with self.canvas:
                Color(*self.parent.parent.a)
            self.canvas.add(Line(circle=(instance.center_x, instance.center_y, (Window.size[0]+Window.size[1])/32), width = 10)) 
            self.white.append(int(instance.text))
            if len(self.last_button) >= 5:
                for row in self.victory:
                    if(all(x in self.white for x in row)):
                        time.sleep(1)
                        myapp.screen_manager.current = "White"
                        return
                    elif(len(self.last_button) == 9):
                        myapp.screen_manager.current = "Draw"
            return
        else:
#            instance.background_color = (0, 0, 0, 0)
#            print(Window.size[0])   
            with self.canvas:
                Color(*self.parent.parent.b)
            self.canvas.add(Line(points=[instance.center_x-Window.size[0]/8+Window.size[0]/32,instance.center_y+Window.size[1]/8-Window.size[1]/32,instance.center_x+Window.size[0]/8-Window.size[0]/32,instance.center_y-Window.size[1]/8+Window.size[1]/32], width = 10))
            self.canvas.add(Line(points=[instance.center_x-Window.size[0]/8+Window.size[0]/32,instance.center_y-Window.size[1]/8+Window.size[1]/32,instance.center_x+Window.size[0]/8-Window.size[0]/32,instance.center_y+Window.size[1]/8-Window.size[1]/32], width = 10))
            self.label_1.text = f"{myapp.first_page.lab1}'s Turn!"
            self.black.append(int(instance.text))
            if len(self.last_button) >= 5:
                for row in self.victory:
                    if(all(x in self.black for x in row)):
                        time.sleep(1)
                        myapp.screen_manager.current = "Black"
                        return
                    elif(len(self.last_button) == 9):
                        myapp.screen_manager.current = "Draw"
            return
        
class WhitePage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.label = Label(text = f"{myapp.first_page.lab1} Wins!", font_size = 75, height = Window.size[1] * 0.8, size_hint_y = None)
        self.add_widget(self.label)
        
        h_layout = BoxLayout()
        self.btn = Button(text = "Play Again?", font_size = 30)
        self.btn.bind(on_press = self.main)
        h_layout.add_widget(self.btn)
        
        self.btn1 = Button(text = "Try Another Color?", font_size = 30)
        self.btn1.bind(on_press = self.main1)
        h_layout.add_widget(self.btn1)
        
        self.add_widget(h_layout)
        return
    
    def main(self, instance):
        self.i = 1
        myapp.first_page.a=f"{random.sample(range(1, 1000000), 3)}"
        New = MainPage()
        self.parent.parent.screen = Screen(name=f"Main{myapp.first_page.a[1:7]}")
        self.parent.parent.screen.add_widget(New)
        self.parent.parent.add_widget(self.parent.parent.screen)
        myapp.screen_manager.current = f"Main{myapp.first_page.a[1:7]}"
        return
    
    def main1(self, instance):
        self.i = 1
        myapp.first_page.a=f"{random.sample(range(1, 1000000), 3)}"
        self.New = MainPage()
#        print(self.New.label_1.text)
        self.parent.parent.screen = Screen(name=f"Main{myapp.first_page.a[1:7]}")
        self.parent.parent.screen.add_widget(self.New)
        self.parent.parent.add_widget(self.parent.parent.screen)
        myapp.first_page.prev_page = "White"
        myapp.screen_manager.current = "First"
        return
           
class BlackPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.label = Label(text = f"{myapp.first_page.lab2} Wins!", font_size = 75, height = Window.size[1] * 0.8, size_hint_y = None)
        self.add_widget(self.label)
        
        h_layout = BoxLayout()
        
        self.btn = Button(text = "Play Again?", font_size = 30)
        self.btn.bind(on_press = self.main)
        h_layout.add_widget(self.btn)
        
        self.btn1 = Button(text = "Try Another Color?", font_size = 30)
        self.btn1.bind(on_press = self.main1)
        h_layout.add_widget(self.btn1)
        
        self.add_widget(h_layout)
        return

    def main(self, instance):
        self.i = 1
        myapp.first_page.a=f"{random.sample(range(1, 1000000), 3)}"
        New = MainPage()
        self.parent.parent.screen = Screen(name=f"Main{myapp.first_page.a[1:7]}")
        self.parent.parent.screen.add_widget(New)
        self.parent.parent.add_widget(self.parent.parent.screen)
        myapp.screen_manager.current = f"Main{myapp.first_page.a[1:7]}"
        return
    
    def main1(self, instance):
        self.i = 1
        myapp.first_page.a=f"{random.sample(range(1, 1000000), 3)}"
        self.New = MainPage()
        self.parent.parent.screen = Screen(name=f"Main{myapp.first_page.a[1:7]}")
        self.parent.parent.screen.add_widget(self.New)
        self.parent.parent.add_widget(self.parent.parent.screen)
        myapp.first_page.prev_page = "Black"
        myapp.screen_manager.current = "First"
        return
    
class DrawPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.label = Label(text = "Draw!", font_size = 75, height = Window.size[1] * 0.8, size_hint_y = None)
        self.add_widget(self.label)
        
        h_layout = BoxLayout()
        
        self.btn = Button(text = "Play Again?", font_size = 30)
        self.btn.bind(on_press = self.main)
        h_layout.add_widget(self.btn)
        
        self.btn1 = Button(text = "Try Another Color?", font_size = 30)
        self.btn1.bind(on_press = self.main1)
        h_layout.add_widget(self.btn1)
        
        self.add_widget(h_layout)
        return
    
    def main(self, instance):
        self.i = 1
        myapp.first_page.a=f"{random.sample(range(1, 1000000), 3)}"
        New = MainPage()
        self.parent.parent.screen = Screen(name=f"Main{myapp.first_page.a[1:7]}")
        self.parent.parent.screen.add_widget(New)
        self.parent.parent.add_widget(self.parent.parent.screen)
        myapp.screen_manager.current = f"Main{myapp.first_page.a[1:7]}"
        return
    
    def main1(self, instance):
        self.i = 1
        myapp.first_page.a=f"{random.sample(range(1, 1000000), 3)}"
        self.New = MainPage()
        self.parent.parent.screen = Screen(name=f"Main{myapp.first_page.a[1:7]}")
        self.parent.parent.screen.add_widget(self.New)
        self.parent.parent.add_widget(self.parent.parent.screen)
        myapp.first_page.prev_page = "Draw"
        myapp.screen_manager.current = "First"
        return

class FirstPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.lab1 = ""
        self.lab2 = ""
        self.count = 0
        self.prev_page = ""
        self.a = 0
        
        box = BoxLayout(height = Window.size[1]*0.275, size_hint_y = None)
        
        self.lbl1 = LabelB(bcolor=(1, 0, 0, 1))
        box.add_widget(self.lbl1)
        
        self.lbl2 = LabelB(bcolor=(0, 0, 1, 1))
        box.add_widget(self.lbl2)
        
        self.lbl3 = LabelB(bcolor=(0, 0, 0, 0))
        box.add_widget(self.lbl3)
        
        self.lbl4 = LabelB(bcolor=(1, 1, 1, 1))
        box.add_widget(self.lbl4)
        
        self.add_widget(box)
        
        box = BoxLayout()
        
        self.btn1 = Button(text = "Red/Blue", font_size = 30)
        self.btn1.bind(on_press = self.on_button_press)
        box.add_widget(self.btn1)
        
        self.btn2 = Button(text = "Black/White", font_size = 30)
        self.btn2.bind(on_press = self.on_button_press)
        box.add_widget(self.btn2)
        
        self.add_widget(box)
        
        box = BoxLayout(height = Window.size[1]*0.275, size_hint_y = None)
        
        self.lbl5 = LabelB(bcolor=(0, 1, 1, 1))
        box.add_widget(self.lbl5)
        
        self.lbl6 = LabelB(bcolor=(0, 0, 1, 1))
        box.add_widget(self.lbl6)
        
        self.lbl7 = LabelB(bcolor=(1, 1, 1, 1))
        box.add_widget(self.lbl7)
        
        self.lbl8 = LabelB(bcolor=(0, 0, 0, 0))
        box.add_widget(self.lbl8)
        
        self.add_widget(box)
        
        box = BoxLayout()
        
        self.btn3 = Button(text = "Cyan/Blue", font_size= 30)
        self.btn3.bind(on_press = self.on_button_press)
        box.add_widget(self.btn3)
        
        self.btn4 = Button(text = "White/Black", font_size = 30)
        self.btn4.bind(on_press = self.on_button_press)
        box.add_widget(self.btn4)
        
        self.add_widget(box)
        
        self.label = Label(text = "Select the colors!!", height = Window.size[1]*0.25, size_hint_y=None, font_size = 50)
        self.add_widget(self.label)
        
    def on_button_press(self, instance):
        self.count = self.count + 1
        if instance.text == "Red/Blue":
            self.lab1 = instance.text[0:3]
            self.lab2 = instance.text[4:]            
            self.parent.parent.a = [1, 0, 0, 1]
            self.parent.parent.b = [0, 0, 1, 1]
        elif instance.text == "Black/White":
            self.lab1 = instance.text[0:5]
            self.lab2 = instance.text[6:]            
            self.parent.parent.a = [0, 0, 0, 1]
            self.parent.parent.b = [1, 1, 1, 1]
        elif instance.text == "Cyan/Blue":
            self.lab1 = instance.text[0:4]
            self.lab2 = instance.text[5:]
            self.parent.parent.a = [0, 1, 1, 1]
            self.parent.parent.b = [0, 0, 1, 1]
        elif instance.text == "White/Black":
            self.lab1 = instance.text[0:5]
            self.lab2 = instance.text[6:]
            self.parent.parent.a = [1, 1, 1, 1]
            self.parent.parent.b = [0, 0, 0, 1]
#        print(self.lab1)    
        if self.count > 1 and self.prev_page == "White" :    
            myapp.white_page.New.label_1.text = f"{self.lab1} starts first!!"
        elif self.count > 1 and self.prev_page == "Black":
            myapp.black_page.New.label_1.text = f"{self.lab1} starts first!!"
        elif self.count > 1 and self.prev_page == "Draw":
            myapp.draw_page.New.label_1.text = f"{self.lab1} starts first!!"    
        myapp.main_page.label_1.text = f"{self.lab1} starts first!!"
        myapp.white_page.label.text = f"{self.lab1} Wins!"
        myapp.black_page.label.text = f"{self.lab2} Wins!"    
        if self.count < 2:
            myapp.screen_manager.current = "Main"
        elif self.prev_page == "White":
            myapp.screen_manager.current = f"Main{self.a[1:7]}"
        elif self.prev_page == "Black":
            myapp.screen_manager.current = f"Main{self.a[1:7]}"
        elif self.prev_page == "Draw":
            myapp.screen_manager.current = f"Main{self.a[1:7]}"
        return
    
class MainApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        
        self.first_page = FirstPage()
        self.main_page = MainPage()
        self.white_page = WhitePage()
        self.black_page = BlackPage()
        self.draw_page = DrawPage()
        
        screen = Screen(name="First")
        screen.add_widget(self.first_page)
        self.screen_manager.add_widget(screen)
        
        screen = Screen(name="Main")
        screen.add_widget(self.main_page)
        self.screen_manager.add_widget(screen)
        
        screen = Screen(name="White")
        screen.add_widget(self.white_page)
        self.screen_manager.add_widget(screen)
        
        screen = Screen(name="Black")
        screen.add_widget(self.black_page)
        self.screen_manager.add_widget(screen)
        
        screen = Screen(name="Draw")
        screen.add_widget(self.draw_page)
        self.screen_manager.add_widget(screen)
        
        return self.screen_manager
    
if __name__ == "__main__":
    myapp = MainApp()
    myapp.run()    