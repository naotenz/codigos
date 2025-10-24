# archivo: audio_widget.py
class AudioPlayer:
    def __init__(self, ruta):
        self.ruta = ruta

    def play(self):
        print(f"Reproduciendo {self.ruta}")
