# view.py
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class MainView(BoxLayout):
    input_p1 = ObjectProperty(None)
    input_p2 = ObjectProperty(None)
    input_x = ObjectProperty(None)
    output_label = ObjectProperty(None)

    def mostrar_resultado(self, texto):
        self.output_label.text = texto
