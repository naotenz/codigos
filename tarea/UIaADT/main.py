# main.py
from kivy.app import App
from view import MainView
from controller import Controller

class PolinomioApp(App):
    def build(self):
        view = MainView()
        self.controller = Controller(view)
        view.controller = self.controller
        return view

if __name__ == "__main__":
    PolinomioApp().run()
