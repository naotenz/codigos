import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.filechooser import FileChooserListView

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty
from kivy.uix.videoplayer import VideoPlayer as KivyVideoPlayer
from kivy.uix.boxlayout import BoxLayout
<<<<<<< HEAD
from kivy.core.window import Window
from kivy.properties import NumericProperty, StringProperty
=======

from kivy.core.window import Window
>>>>>>> 00e2c97 (cambios)

class CancionButton(ButtonBehavior, BoxLayout):
    titulo = StringProperty()

    def __init__(self, cancion, controller, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.cancion = cancion
        self.controller = controller
        self.titulo = cancion.titulo
        self.label = Label(text=self.titulo, halign='left', size_hint_x=0.9)
        self.add_widget(self.label)
        self.play_btn = Button(text="▶", size_hint_x=0.1)
        self.play_btn.bind(on_press=self.reproducir)
        self.add_widget(self.play_btn)
        self.bind(on_press=self.reproducir)

    def reproducir(self, instance=None):
        nodo = self.controller.lista.cabeza
        while nodo:
            if nodo.cancion == self.cancion:
                self.controller.lista.actual = nodo
                break
            nodo = nodo.siguiente
        self.controller.cargar_cancion(self.cancion)
<<<<<<< HEAD
        self.controller.repro_play_pause()

=======
        self.controller.reproducir()
>>>>>>> 00e2c97 (cambios)


class MusicaView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = None
<<<<<<< HEAD
        self.audio_widget = None 
        self.video_widget = None
=======
>>>>>>> 00e2c97 (cambios)
        self.last_path = os.path.expanduser("~")
        self.orientation = "vertical"
        self.padding = 5
        self.spacing = 5

        # Link YouTube
        self.link_input = TextInput(hint_text="Ingresa link de YouTube", multiline=False, size_hint_y=None, height=30)
        self.add_widget(self.link_input)
        self.agregar_btn = Button(text="Descargar Audio", size_hint_y=None, height=40)
        self.add_widget(self.agregar_btn)
        self.agregar_video_btn = Button(text="Descargar Video", size_hint_y=None, height=40)
        self.add_widget(self.agregar_video_btn)
        self.agregar_video_btn.bind(on_press=lambda x: self.controller.agregar_cancion_yt(x, tipo="mp4"))
        # Local
        self.agregar_local_btn = Button(text="Agregar Audio local", size_hint_y=None, height=40)
        self.add_widget(self.agregar_local_btn)
        self.agregar_local_btn.bind(on_press=self.abrir_popup_arrastrar)
        # Agregar video local
        self.agregar_video_local_btn = Button(text="Agregar video local", size_hint_y=None, height=40)
        self.add_widget(self.agregar_video_local_btn)
        self.agregar_video_local_btn.bind(on_press=self.abrir_filechooser_video)

        # Cancelar descarga
        self.cancel_btn = Button(text="Cancelar descarga", size_hint_y=None, height=40)
        self.add_widget(self.cancel_btn)

        # Canción actual
        self.cancion_label = Label(text="No hay canción seleccionada", size_hint_y=None, height=30)
        self.add_widget(self.cancion_label)

        # Controles
<<<<<<< HEAD
        # Controles
        controls = BoxLayout(size_hint_y=None, height=50, spacing=5)
        self.anterior_btn = Button(text="⏮ Anterior")
        self.play_btn = Button(text="▶️ / ⏸️")
        self.siguiente_btn = Button(text="⏭ Siguiente")
        self.eliminar_btn = Button(text="🗑 Eliminar")

        controls.add_widget(self.anterior_btn)
        controls.add_widget(self.play_btn)
        controls.add_widget(self.siguiente_btn)
        controls.add_widget(self.eliminar_btn)
        self.add_widget(controls)


=======
        controls = BoxLayout(size_hint_y=None, height=50)
        self.anterior_btn = Button(text="<< Anterior")
        self.play_btn = Button(text="Play/Pause")
        self.siguiente_btn = Button(text="Siguiente >>")
        controls.add_widget(self.anterior_btn)
        controls.add_widget(self.play_btn)
        controls.add_widget(self.siguiente_btn)
        self.add_widget(controls)

>>>>>>> 00e2c97 (cambios)
        # Barra de progreso reproducción
        self.progress = ProgressBar(max=100, value=0, size_hint_y=None, height=20)
        self.add_widget(self.progress)

        # Barra de descarga
        self.descarga_label = Label(text="", size_hint_y=None, height=30)
        self.add_widget(self.descarga_label)
        self.descarga_progress = ProgressBar(max=100, value=0, size_hint_y=None, height=20)
        self.add_widget(self.descarga_progress)

        # Biblioteca
        self.biblioteca_scroll = ScrollView(size_hint=(1, 1))
        self.biblioteca_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.biblioteca_layout.bind(minimum_height=self.biblioteca_layout.setter('height'))
        self.biblioteca_scroll.add_widget(self.biblioteca_layout)
        self.add_widget(self.biblioteca_scroll)

        # Drag & drop
        Window.bind(on_dropfile=self.on_dropfile)

        


    # ----------------------------
<<<<<<< HEAD
    def init_binds(self):        
=======
    def init_binds(self):
>>>>>>> 00e2c97 (cambios)
        self.agregar_btn.bind(on_press=self.controller.agregar_cancion_yt)
        self.play_btn.bind(on_press=self.controller.repro_play_pause)
        self.siguiente_btn.bind(on_press=self.controller.repro_siguiente)
        self.anterior_btn.bind(on_press=self.controller.repro_anterior)
<<<<<<< HEAD
        self.eliminar_btn.bind(on_press=self.controller.repro_eliminar)
        self.cancel_btn.bind(on_press=self.controller.cancelar_descarga)


=======
        self.cancel_btn.bind(on_press=self.controller.cancelar_descarga)

>>>>>>> 00e2c97 (cambios)
    def abrir_popup_arrastrar(self, instance):
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(
            text="Arrastra aquí un archivo de audio (MP3, WAV, FLAC, AAC, OGG)\nO haz clic aquí para buscar",
            halign='center',
            valign='middle',
            size_hint_y=0.8
        )
        label.bind(on_touch_down=self.abrir_filechooser_audio)
        box.add_widget(label)
        popup = Popup(title="Agregar canción local", content=box, size_hint=(0.8, 0.5))
        popup.open()

    def on_dropfile(self, window, file_path):
        ruta = file_path.decode("utf-8")
        if self.controller:
            self.controller.agregar_cancion_local(ruta)
    
    def actualizar_biblioteca(self):
        # Limpiar la lista actual
        self.biblioteca_layout.clear_widgets()

        if not self.controller:
            return

        # Agregar cada canción como botón
        nodo = self.controller.lista.cabeza
        while nodo:
            cancion_btn = CancionButton(nodo.cancion, self.controller)
            self.biblioteca_layout.add_widget(cancion_btn)
            nodo = nodo.siguiente

    def abrir_filechooser_audio(self, instance, touch=None):
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        filechooser = FileChooserListView(path=self.last_path, filters=["*.mp3", "*.wav", "*.flac", "*.aac", "*.ogg"])
        box.add_widget(filechooser)

        btn = Button(text="Agregar audio", size_hint_y=None, height=40)
        box.add_widget(btn)

        popup = Popup(title="Seleccionar audio local", content=box, size_hint=(0.8, 0.8))
        btn.bind(on_press=lambda x: self._agregar_audio_desde_filechooser(filechooser, popup))
        popup.open()


    def _agregar_audio_desde_filechooser(self, filechooser, popup):
        if filechooser.selection:
            ruta = filechooser.selection[0]
            if self.controller:
                self.controller.agregar_cancion_local(ruta)
        popup.dismiss()
    
    def abrir_filechooser_video(self, instance):
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        filechooser = FileChooserListView(path=self.last_path, filters=["*.mp4", "*.mkv", "*.avi"])
        box.add_widget(filechooser)

        btn = Button(text="Agregar video", size_hint_y=None, height=40)
        box.add_widget(btn)

        popup = Popup(title="Seleccionar video local", content=box, size_hint=(0.8, 0.8))
        btn.bind(on_press=lambda x: self._agregar_video_desde_filechooser(filechooser, popup))
        popup.open()

    def _agregar_video_desde_filechooser(self, filechooser, popup):
        if filechooser.selection:
            ruta = filechooser.selection[0]
            if self.controller:
                self.controller.agregar_cancion_local(ruta)  # Usa el mismo método que MP3
        popup.dismiss()





class VideoPlayer(BoxLayout):
    position = NumericProperty(0)   # <-- necesaria para KV y bindings
    duration = NumericProperty(1)   # <-- necesaria para KV y bindings
    state = StringProperty('stop')  # opcional, para controlar play/pause
    volume = NumericProperty(1)
    # Iconos de control de reproducción
    image_play = StringProperty("play.png")
    image_pause = StringProperty("pause.png")
    image_stop = StringProperty("stop.png")

    # Iconos de volumen
    image_volumemuted = StringProperty("vol_mute.png")
    image_volumelow = StringProperty("vol_low.png")
    image_volumemedium = StringProperty("vol_medium.png")
    image_volumehigh = StringProperty("vol_high.png")

    def __init__(self, source, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        # --- Video ---
        self.video = Video(source=source, state='play', options={'eos': 'loop'})
        self.video.allow_stretch = True
        self.video.keep_ratio = True
        # Hace que el video ocupe casi toda la pantalla y esté centrado
        self.video.size = Window.size 
        self.video.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        # Si quieres pantalla completa real, puedes activar esto:
        # from kivy.core.window import Window
        # self.video.size = Window.size
        self.add_widget(self.video)

        # --- Controles ---
        self.controls = BoxLayout(size_hint_y=0.2)
        self.btn_back = Button(text="⏪ -5s")
        self.btn_play = Button(text="⏯️")
        self.btn_forward = Button(text="+30s ⏩")
        self.btn_speed = Button(text="x1")
        self.vol_slider = Slider(min=0, max=1, value=1)
        self.progress = Slider(min=0, max=1, value=0)
        self.lbl_time = Label(text="0:00 / 0:00", size_hint_x=0.3)

        self.controls.add_widget(self.btn_back)
        self.controls.add_widget(self.btn_play)
        self.controls.add_widget(self.btn_forward)
        self.controls.add_widget(self.btn_speed)
        self.controls.add_widget(Label(text="🔊", size_hint_x=0.1))
        self.controls.add_widget(self.vol_slider)

        self.add_widget(self.progress)
        self.add_widget(self.controls)
        self.add_widget(self.lbl_time)

        # --- Binds ---
        self.btn_back.bind(on_release=lambda _: self.seek(-5))
        self.btn_forward.bind(on_release=lambda _: self.seek(30))
        self.btn_play.bind(on_release=lambda _: self.toggle_play())
        self.btn_speed.bind(on_release=lambda _: self.change_speed())
        self.vol_slider.bind(value=self.set_volume)
        self.progress.bind(on_touch_up=self.seek_to)

        Clock.schedule_interval(self.update_progress, 0.5)

        self.speeds = [1.0, 2.0, 3.0, 4.0]
        self.speed_index = 0

    def toggle_play(self):
        if self.video.state == 'play':
            self.video.state = 'pause'
            self.btn_play.text = "▶️"
        else:
            self.video.state = 'play'
            self.btn_play.text = "⏸️"

    def seek(self, seconds):
        if self.video.duration:
            new_pos = max(0, min(self.video.position + seconds, self.video.duration))
            self.video.seek(new_pos / self.video.duration)

    def seek_to(self, instance, touch):
        if instance.collide_point(*touch.pos):
            if self.video.duration:
                self.video.seek(instance.value)

    def update_progress(self, dt):
        if self.video.duration:
            self.position = self.video.position
            self.duration = self.video.duration
            self.progress.value = self.position / self.duration
            self.lbl_time.text = f"{self.format_time(self.position)} / {self.format_time(self.duration)}"


    def format_time(self, seconds):
        minutes = int(seconds // 60)
        sec = int(seconds % 60)
        return f"{minutes}:{sec:02}"

    def change_speed(self):
        self.speed_index = (self.speed_index + 1) % len(self.speeds)
        new_speed = self.speeds[self.speed_index]
        self.video.volume = self.vol_slider.value
        self.video._ffplayer.set_speed(new_speed)
        self.btn_speed.text = f"x{new_speed}"

    def set_volume(self, instance, value):
        self.video.volume = value
        self.volume = value

    def _update_position(self, instance, value):
        self.position = value

    def _update_duration(self, instance, value):
        self.duration = value

    def _update_state(self, instance, value):
        self.state = value

    def _update_props(self, dt):
        # fallback en caso de que bind no se actualice
        self.position = self.video.position
        self.duration = self.video.duration
        self.state = self.video.state

<<<<<<< HEAD
=======



class AudioPlayer(BoxLayout):
    def __init__(self, source, **kwargs):
        # Llama a super correctamente, pasando solo kwargs
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (1, None)
        self.height = 150

        # --- Audio ---
        self.audio = SoundLoader.load(source)
        if not self.audio:
            print(f"No se pudo cargar el audio: {source}")

        # --- Controles ---
        controls = BoxLayout(size_hint_y=None, height=50)
        self.btn_play = Button(text="▶️")
        self.btn_play.bind(on_release=self.toggle_play)
        controls.add_widget(self.btn_play)

        self.add_widget(controls)

    def toggle_play(self, instance=None):
        if self.audio:
            if self.audio.state == 'play':
                self.audio.stop()
                self.btn_play.text = "▶️"
            else:
                self.audio.play()
                self.btn_play.text = "⏸️"
>>>>>>> 00e2c97 (cambios)
