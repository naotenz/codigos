# main.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# Importar las clases del Modelo y el Controlador
from model import ContadorModel
from controller import ContadorController

# La clase de la Vista principal que Kivy cargará desde el archivo .kv
class ContadorView(BoxLayout):
    pass

class ContadorApp(App):
    """
    Clase principal de la aplicación Kivy.
    """
    def build(self):
        # Crear las instancias de MVC
        model = ContadorModel()
        view = ContadorView()
        self.controller = ContadorController(model, view)

        # Devolver la vista principal para que Kivy la muestre
        return view

if __name__ == '__main__':
    ContadorApp().run()