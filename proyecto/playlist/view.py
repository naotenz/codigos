from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from controller import EstudianteController
from model import Estudiante


class GestionEstudiantesView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.controller = EstudianteController()
        self.siguiente_id = 1

        # Label de estado
        self.estado_label = Label(text='Sistema de Gestión de Estudiantes', size_hint_y=None, height=30)
        self.add_widget(self.estado_label)

        # Formulario
        form = BoxLayout(size_hint_y=None, height=30)
        self.nombre_input = TextInput(hint_text='Nombre', multiline=False)
        self.apellido_input = TextInput(hint_text='Apellido', multiline=False)
        self.calif_input = TextInput(hint_text='Calificaciones (3 notas 1-100)', multiline=False)
        form.add_widget(self.nombre_input)
        form.add_widget(self.apellido_input)
        form.add_widget(self.calif_input)
        self.add_widget(form)

        # Botones principales
        botones = BoxLayout(size_hint_y=None, height=50)
        btn_agregar = Button(text='Inscribir')
        btn_agregar.bind(on_press=self.inscribir)
        btn_eliminar = Button(text='Dar de Baja')
        btn_eliminar.bind(on_press=self.dar_de_baja)
        btn_actualizar = Button(text='Actualizar Calificaciones')
        btn_actualizar.bind(on_press=self.actualizar_calificaciones)
        btn_promedio = Button(text='Calcular Promedio')
        btn_promedio.bind(on_press=self.calcular_promedio)
        botones.add_widget(btn_agregar)
        botones.add_widget(btn_eliminar)
        botones.add_widget(btn_actualizar)
        botones.add_widget(btn_promedio)
        self.add_widget(botones)

        # Buscar estudiante
        buscar_box = BoxLayout(size_hint_y=None, height=30)
        self.buscar_input = TextInput(hint_text='ID a buscar', size_hint_x=0.3, multiline=False)
        self.buscar_btn = Button(text='Buscar Estudiante', size_hint_x=0.7)
        self.buscar_btn.bind(on_press=self.buscar_estudiante)
        buscar_box.add_widget(self.buscar_input)
        buscar_box.add_widget(self.buscar_btn)
        self.add_widget(buscar_box)

        # Reporte (scroll)
        self.scroll = ScrollView()
        self.grid = GridLayout(cols=1, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scroll.add_widget(self.grid)
        self.add_widget(self.scroll)

    # --- Métodos auxiliares ---
    def actualizar_estado(self, texto):
        self.estado_label.text = texto

    def actualizar_lista(self, texto):
        self.grid.clear_widgets()
        for linea in texto.split('\n'):
            lbl = Label(text=linea, size_hint_y=None, height=30)
            self.grid.add_widget(lbl)

    # --- Funciones principales ---
    def inscribir(self, instance):
        try:
            nombre = self.nombre_input.text.strip()
            apellido = self.apellido_input.text.strip()
            calificaciones = list(map(int, self.calif_input.text.split()))

            if not nombre or not apellido:
                self.actualizar_estado("Error: Nombre y apellido son obligatorios")
                return
            if len(calificaciones) != 3:
                self.actualizar_estado("Error: Ingresa exactamente 3 calificaciones")
                return
            if any(c < 0 or c > 100 for c in calificaciones):
                self.actualizar_estado("Error: Calificaciones entre 0 y 100")
                return

            estudiante = Estudiante(self.siguiente_id, nombre, apellido, calificaciones)
            self.controller.inscribir_estudiante(estudiante)
            self.actualizar_estado(f"Estudiante {nombre} inscrito con ID {self.siguiente_id}")
            self.siguiente_id += 1
            self.actualizar_lista(self.controller.generar_reporte())
        except Exception as e:
            self.actualizar_estado(f"Error: {e}")

    def dar_de_baja(self, instance):
        try:
            id = int(self.buscar_input.text)
            if self.controller.dar_de_baja(id):
                self.actualizar_estado(f"Estudiante con ID {id} eliminado")
            else:
                self.actualizar_estado(f"Estudiante con ID {id} no encontrado")
            self.actualizar_lista(self.controller.generar_reporte())
        except ValueError:
            self.actualizar_estado("Error: ID inválido")

    def actualizar_calificaciones(self, instance):
        try:
            id = int(self.buscar_input.text)
            calificaciones = list(map(int, self.calif_input.text.split()))
            if len(calificaciones) != 3:
                self.actualizar_estado("Error: Ingresa exactamente 3 calificaciones")
                return
            if any(c < 0 or c > 100 for c in calificaciones):
                self.actualizar_estado("Error: Calificaciones entre 0 y 100")
                return
            if self.controller.actualizar_calificaciones(id, calificaciones):
                self.actualizar_estado(f"Calificaciones del estudiante con ID {id} actualizadas")
            else:
                self.actualizar_estado(f"Estudiante con ID {id} no encontrado")
            self.actualizar_lista(self.controller.generar_reporte())
        except ValueError:
            self.actualizar_estado("Error: ID o calificaciones inválidas")

    def calcular_promedio(self, instance):
        id_txt = self.buscar_input.text.strip()
        if not id_txt.isdigit():
            Popup(title="Error",
                  content=Label(text="Por favor ingresa un ID válido"),
                  size_hint=(0.6, 0.4)).open()
            return
        id_num = int(id_txt)
        estudiante = self.controller.buscar_estudiante(id_num)
        if not estudiante:
            Popup(title="Error",
                  content=Label(text=f"Estudiante con ID {id_num} no encontrado"),
                  size_hint=(0.6, 0.4)).open()
            return
        promedio = estudiante.promedio()
        Popup(title="📘 Promedio del estudiante",
              content=Label(text=f"El promedio de {estudiante.nombre} {estudiante.apellido} (ID {id_num}) es: {promedio:.2f}"),
              size_hint=(0.7, 0.4)).open()

    def buscar_estudiante(self, instance):
        try:
            id = int(self.buscar_input.text)
            estudiante = self.controller.buscar_estudiante(id)
            if estudiante:
                self.actualizar_estado(str(estudiante))
                self.calif_input.text = ' '.join(map(str, estudiante.calificaciones))
            else:
                self.actualizar_estado(f"Estudiante con ID {id} no encontrado")
                self.calif_input.text = ''
        except ValueError:
            self.actualizar_estado("Error: ID inválido")


