# audio_widget.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty

class AudioPlayer(BoxLayout):
    position = NumericProperty(0)
    duration = NumericProperty(1)
    state = StringProperty('stop')
    volume = NumericProperty(1)

    def __init__(self, source=None, autoplay=False, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.sound = None
        self.source = None

        # --- Controles ---
        controls = BoxLayout(size_hint_y=None, height=50)
        self.play_btn = Button(text="Play")
        self.stop_btn = Button(text="Stop")
        self.vol_slider = Slider(min=0, max=1, value=1)
        self.progress = Slider(min=0, max=1, value=0)
        self.lbl_time = Label(text="0:00 / 0:00", size_hint_x=0.3)

        controls.add_widget(self.play_btn)
        controls.add_widget(self.stop_btn)
        controls.add_widget(Label(text="🔊", size_hint_x=0.1))
        controls.add_widget(self.vol_slider)

        self.add_widget(self.progress)
        self.add_widget(controls)
        self.add_widget(self.lbl_time)

        # --- Binds ---
        self.play_btn.bind(on_release=self.toggle_play)
        self.stop_btn.bind(on_release=self.stop)
        self.vol_slider.bind(value=self.set_volume)
        self.progress.bind(on_touch_up=self.seek_to)

        # Actualizar progreso cada 0.5 seg
        Clock.schedule_interval(self.update_progress, 0.5)
        if source:
            self.load(source, autoplay=autoplay)


    # Cargar una canción nueva
    def load(self, source, autoplay=False):
        # Detener sonido anterior
        if self.sound:
            self.sound.stop()
        self.source = source
        self.sound = SoundLoader.load(source)
        if self.sound:
            self.duration = self.sound.length
            self.position = 0
            self.state = 'stop'
            self.play_btn.text = "Play"
            self.progress.value = 0
            self.lbl_time.text = f"0:00 / {int(self.duration//60)}:{int(self.duration%60):02}"
            if autoplay:
                self.sound.play()

    def toggle_play(self, instance=None):
        if not self.sound:
            return
        if self.sound.state == 'play':
            self.sound.stop()
            self.state = 'stop'
            self.play_btn.text = "Play"
        else:
            self.sound.play()
            self.state = 'play'
            self.play_btn.text = "Pause"

    def stop(self, instance=None):
        if self.sound:
            self.sound.stop()
            self.state = 'stop'
            self.play_btn.text = "Play"
            self.position = 0
            self.progress.value = 0
            self.lbl_time.text = f"0:00 / {int(self.duration//60)}:{int(self.duration%60):02}"

    def set_volume(self, instance, value):
        if self.sound:
            self.sound.volume = value
        self.volume = value

    def seek_to(self, instance, touch):
        if instance.collide_point(*touch.pos) and self.sound and self.sound.length:
            pos = instance.value * self.sound.length
            self.sound.seek(pos)
            self.position = pos

    def update_progress(self, dt):
        if self.sound and self.sound.length and self.sound.state == 'play':
            self.position = self.sound.get_pos()
            self.progress.value = self.position / self.duration if self.duration else 0
            self.lbl_time.text = f"{int(self.position//60)}:{int(self.position%60):02} / {int(self.duration//60)}:{int(self.duration%60):02}"
