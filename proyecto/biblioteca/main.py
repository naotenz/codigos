import os
# Forzar que Kivy use ffpyplayer como backend de video
os.environ['KIVY_VIDEO'] = 'ffpyplayer'

from kivy.app import App
from view import MusicaView
from controller import MusicaController


class MusicaApp(App):
    def build(self):
        view = MusicaView()
        MusicaController(view)
        return view


if __name__ == "__main__":
    MusicaApp().run()

