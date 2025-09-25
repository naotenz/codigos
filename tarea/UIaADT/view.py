from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class MainView(BoxLayout):
    input_p1 = ObjectProperty()
    input_p2 = ObjectProperty()
    input_x = ObjectProperty()
    output_label = ObjectProperty()
    controller = None

    def mostrar_resultado(self, texto):
        self.output_label.text = texto
