import os
import re
import threading
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from model import Cancion, ListaMusica
import yt_dlp
from kivy.uix.video import Video
from kivy.uix.slider import Slider
from view import VideoPlayer 
from kivy.uix.videoplayer import VideoPlayer
from audio_widget import AudioPlayer





# Logger personalizado
class MyLogger:
    def debug(self, msg): pass
    def warning(self, msg): print("WARNING:", msg)
    def error(self, msg): print("ERROR:", msg)

class MusicaController:
    def __init__(self, view):
        self.view = view
        self.lista = ListaMusica()
        self.sonido = None
        self.descarga_thread = None
        self.cancel_event = threading.Event()
        self.output_dir = os.path.join(os.getcwd(), "descargas")
        os.makedirs(self.output_dir, exist_ok=True)

        self.view.controller = self
        self.view.init_binds()

    # ----------------------------
    # Popups
    def mostrar_popup(self, titulo, mensaje):
        box = BoxLayout(orientation="vertical", padding=10, spacing=10)
        label = Label(text=mensaje)
        btn = Button(text="Cerrar", size_hint_y=None, height=40)
        box.add_widget(label)
        box.add_widget(btn)
        popup = Popup(title=titulo, content=box, size_hint=(0.5, 0.3))
        btn.bind(on_press=popup.dismiss)
        popup.open()

    # ----------------------------
    # Agregar canción desde YouTube
    def agregar_cancion_yt(self, instance, tipo="mp3"):
        url = self.view.link_input.text.strip()
        if not url:
            self.mostrar_popup("Error", "Por favor ingresa un enlace de YouTube.")
            return

        self.cancel_event.clear()
        self.view.descarga_progress.value = 0
        self.view.descarga_label.text = f"Iniciando descarga ({tipo.upper()})..."

        self.descarga_thread = threading.Thread(target=self._descargar_en_hilo, args=(url, tipo))
        self.descarga_thread.start()


    def _descargar_en_hilo(self, url, tipo="mp3"):
        def progreso_hook(d):
            if d['status'] == 'downloading':
                porcentaje = d.get('_percent_str', '0.0%').strip()
                try:
                    porcentaje_val = float(porcentaje.replace('%', ''))
                except:
                    porcentaje_val = 0
                Clock.schedule_once(lambda dt: self.actualizar_barra_descarga(porcentaje_val, d.get('filename', 'Descargando')))
            elif d['status'] == 'finished':
                Clock.schedule_once(lambda dt: self.actualizar_barra_descarga(100, "Descarga completada"))

        # -------------------
        # 📁 Crear carpetas según tipo
        base_dir = os.path.join(os.getcwd(), "descargas")
        if tipo == "mp3":
            carpeta_destino = os.path.join(base_dir, "Audios")
        else:
            carpeta_destino = os.path.join(base_dir, "Videos")

        os.makedirs(carpeta_destino, exist_ok=True)

        # -------------------
        # 🎵 Configurar opciones de descarga según tipo
        if tipo == "mp3":
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(self.output_dir, '%(title)s.%(ext)s'),
                'quiet': True,
                'noplaylist': True,
                'logger': MyLogger(),
                'progress_hooks': [progreso_hook],
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        elif tipo == "mp4":
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': os.path.join(self.output_dir, '%(title)s.%(ext)s'),
                'quiet': True,
                'noplaylist': True,
                'logger': MyLogger(),
                'progress_hooks': [progreso_hook],
            }


        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                # Después de ydl.extract_info
                titulo = re.sub(r'[\\/*?:"<>|]', "", info.get("title", "Desconocido"))
                extension = "mp3" if tipo == "mp3" else "mp4"
                archivo = ydl.prepare_filename(info) 
                real_ext = os.path.splitext(archivo)[1].lower()

                print("Archivo esperado:", archivo)

                if os.path.exists(archivo) and os.path.getsize(archivo) > 0:
                    print("Archivo generado correctamente")
                    
                    if real_ext in [".mp4", ".mkv", ".webm"]:
                        Clock.schedule_once(lambda dt: self.reproducir_video_en_popup(archivo, titulo))                      
                    else:
                        def reproducir_audio(dt):
                            # Quitar audio previo si existe
                            if hasattr(self, "audio_widget") and self.audio_widget:
                                self.view.remove_widget(self.audio_widget)
                            # Crear y reproducir audio usando AudioPlayer
                            self.audio_widget = AudioPlayer(archivo)
                            self.view.add_widget(self.audio_widget)
                            self.view.cancion_label.text = f"Reproduciendo audio: {titulo}"

                        Clock.schedule_once(reproducir_audio)

                else:
                    print("ERROR: No se pudo generar el archivo o está vacío")
                    Clock.schedule_once(lambda dt: self.mostrar_popup(
                        "Error",
                        f"No se pudo generar el archivo de {tipo}.\nVerifica que ffmpeg esté instalado y en el PATH."
                    ))


        except Exception as e:
            Clock.schedule_once(lambda dt, err=e: self.mostrar_popup("Error", f"No se pudo descargar: {err}"))

    # ----------------------------
    def actualizar_barra_descarga(self, porcentaje, texto):
        self.view.descarga_progress.value = porcentaje
        self.view.descarga_label.text = texto


    def cancelar_descarga(self, instance):
        if self.descarga_thread and self.descarga_thread.is_alive():
            self.cancel_event.set()
            self.mostrar_popup("Cancelado", "La descarga fue cancelada.")
            self.view.descarga_progress.value = 0
            self.view.descarga_label.text = ""

    # ----------------------------
    # Agregar canción local
    def agregar_cancion_local(self, ruta):
        if not os.path.exists(ruta):
            self.mostrar_popup("Error", "El archivo no existe.")
            return

        titulo = os.path.splitext(os.path.basename(ruta))[0]  # nombre sin extensión
        extension = os.path.splitext(ruta)[1].lower()

        if extension in [".mp3", ".wav", ".flac", ".aac", ".ogg"]:
            tipo = "audio"
        elif extension in [".mp4", ".mkv", ".avi"]:
            tipo = "video"
        else:
            print("Formato no soportado")
            return

        nueva_cancion = Cancion(titulo, ruta, tipo=tipo)
        self.lista.agregar(nueva_cancion)
        self.view.actualizar_biblioteca()

    # ----------------------------
    # Reproducción
    def cargar_cancion(self, cancion):
        if self.sonido:
            self.sonido.stop()
        self.sonido = SoundLoader.load(cancion.archivo)
        self.view.cancion_label.text = f"Reproduciendo: {cancion.titulo}"

    def reproducir(self):
        if self.sonido:
            self.sonido.play()

    def repro_play_pause(self, instance):
        if not self.sonido:
            cancion = self.lista.cancion_actual()
            if cancion:
                self.cargar_cancion(cancion)
                self.sonido.play()
        else:
            if self.sonido.state == 'play':
                self.sonido.stop()
            else:
                self.sonido.play()

    def repro_siguiente(self, instance):
        siguiente = self.lista.siguiente_cancion()
        if siguiente:
            self.cargar_cancion(siguiente)
            self.reproducir()

    def repro_anterior(self, instance):
        anterior = self.lista.anterior_cancion()
        if anterior:
            self.cargar_cancion(anterior)
            self.reproducir()

    def _procesar_descarga_exitosa(self, titulo, archivo):
        # Crear objeto Cancion
        nueva = Cancion(titulo, archivo)

        # Agregar a la lista
        self.lista.agregar(nueva)

        # Actualizar biblioteca en la interfaz
        self.view.actualizar_biblioteca()

        # Mostrar popup de éxito
        self.mostrar_popup("Éxito", f"'{titulo}' descargada correctamente.")

        # Reiniciar barra de descarga
        self.view.descarga_progress.value = 0
        self.view.descarga_label.text = ""
        # -------------------
        # Reproducir video automáticamente si es mp4
        if archivo.endswith(".mp4"):
            if hasattr(self, "video_widget") and self.video_widget:
                self.view.remove_widget(self.video_widget)
            self.video_widget = VideoPlayer(archivo)
            self.view.add_widget(self.video_widget)
            self.view.cancion_label.text = f"Reproduciendo video: {titulo}"

                # -----------------------------
                # Reproducir automáticamente
        self.cargar_cancion(nueva)
        self.reproducir()
        

    def cargar_cancion(self, cancion):
        if hasattr(self.view, "video_widget"):
            self.view.remove_widget(self.view.video_widget)
        if hasattr(self.view, "audio_widget"):
            self.view.remove_widget(self.view.audio_widget)

        if cancion.tipo == "audio":
            self.view.audio_widget = AudioPlayer(cancion.archivo)
            self.view.add_widget(self.view.audio_widget)
        elif cancion.tipo == "video":
            self.view.video_widget = VideoPlayer(cancion.archivo)
            self.view.add_widget(self.view.video_widget)

    def reproducir_video_en_popup(self, archivo, titulo):
        # Cerrar popup anterior si existe
        if hasattr(self, "video_popup") and self.video_popup:
            self.video_popup.dismiss()
    
        # Crear VideoPlayer
        video_widget = VideoPlayer(archivo)
        video_widget.size_hint = (1, 1)
    
        # Crear y abrir popup
        from kivy.uix.popup import Popup
        self.video_popup = Popup(
            title=f"Reproduciendo: {titulo}",
            content=video_widget,
            size_hint=(0.9, 0.9)
        )
        self.video_popup.open()


