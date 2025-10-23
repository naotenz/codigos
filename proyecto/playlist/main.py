# main.py
from kivy.app import App
from view import GestionEstudiantesView

class GestionEstudiantesApp(App):
    def build(self):
        return GestionEstudiantesView()

if __name__ == '__main__':
    GestionEstudiantesApp().run()


