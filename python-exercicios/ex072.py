from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class Principal(App):
    def build(self):
        box = BoxLayout()
        button = Button(text='Botão 1')
        label = Label(text='Texto 1')
        box.add_widge(button)
        box.add_widget(label)
        return box


Principal().run()
