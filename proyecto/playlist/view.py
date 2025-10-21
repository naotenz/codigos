# view.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from lista_estudiantes import ListaEstudiantes
from model import Estudiante

class GestionEstudiantesView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.lista = ListaEstudiantes()
        self.siguiente_id = 1  # ID automático

        # Label de estado
        self.estado_label = Label(text='Sistema de Gestión de Estudiantes', size_hint_y=None, height=30)
        self.add_widget(self.estado_label)

        # Formulario (sin campo de ID)
        form = BoxLayout(size_hint_y=None, height=30)
        self.nombre_input = TextInput(hint_text='Nombre', multiline=False)
        self.apellido_input = TextInput(hint_text='Apellido', multiline=False)
        self.calif_input = TextInput(hint_text='Calificaciones (3 notas 1-100)', multiline=False)
        form.add_widget(self.nombre_input)
        form.add_widget(self.apellido_input)
        form.add_widget(self.calif_input)
        self.add_widget(form)

        # Botones
        botones = BoxLayout(size_hint_y=None, height=50)
        btn_agregar = Button(text='Inscribir')
        btn_agregar.bind(on_press=self.inscribir)
        btn_eliminar = Button(text='Dar de Baja')
        btn_eliminar.bind(on_press=self.dar_de_baja)
        btn_actualizar = Button(text='Actualizar Calificaciones')
        btn_actualizar.bind(on_press=self.actualizar_calificaciones)
        btn_promedio = Button(text='Calcular Promedio')
        btn_promedio.bind(on_press=self.calcular_promedio)
        btn_reporte = Button(text='Generar Reporte')
        btn_reporte.bind(on_press=self.generar_reporte)
        botones.add_widget(btn_agregar)
        botones.add_widget(btn_eliminar)
        botones.add_widget(btn_actualizar)
        botones.add_widget(btn_promedio)
        botones.add_widget(btn_reporte)
        self.add_widget(botones)

        # ScrollView para reporte
        self.scroll = ScrollView()
        self.grid = GridLayout(cols=1, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scroll.add_widget(self.grid)
        self.add_widget(self.scroll)

    # Actualizar estado
    def actualizar_estado(self, texto):
        self.estado_label.text = texto

    # Actualizar reporte
    def actualizar_lista(self, reporte_texto):
        self.grid.clear_widgets()
        for line in reporte_texto.split('\n'):
            lbl = Label(text=line, size_hint_y=None, height=30)
            self.grid.add_widget(lbl)

    # Funciones de botones
    def inscribir(self, instance):
        try:
            nombre = self.nombre_input.text
            apellido = self.apellido_input.text
            calificaciones = list(map(int, self.calif_input.text.split()))

            if len(calificaciones) != 3:
                self.actualizar_estado("Error: Debes ingresar exactamente 3 calificaciones")
                return
            if any(c < 1 or c > 100 for c in calificaciones):
                self.actualizar_estado("Error: Las calificaciones deben estar entre 1 y 100")
                return

            id = self.siguiente_id
            self.siguiente_id += 1

            estudiante = Estudiante(id, nombre, apellido, calificaciones)
            self.lista.inscribir(estudiante)
            self.actualizar_estado(f'Estudiante {nombre} inscrito con ID {id}')
            self.generar_reporte(None)
        except Exception as e:
            self.actualizar_estado(f'Error: {e}')

    def dar_de_baja(self, instance):
        try:
            id = int(input("Ingrese ID del estudiante a dar de baja: "))
            if self.lista.dar_de_baja(id):
                self.actualizar_estado(f'Estudiante con ID {id} eliminado')
                self.generar_reporte(None)
            else:
                self.actualizar_estado('Estudiante no encontrado')
        except Exception as e:
            self.actualizar_estado(f'Error: {e}')

    def actualizar_calificaciones(self, instance):
        try:
            id = int(input("Ingrese ID del estudiante a actualizar: "))
            calificaciones = list(map(int, self.calif_input.text.split()))
            if len(calificaciones) != 3:
                self.actualizar_estado("Error: Debes ingresar exactamente 3 calificaciones")
                return
            if any(c < 1 or c > 100 for c in calificaciones):
                self.actualizar_estado("Error: Las calificaciones deben estar entre 1 y 100")
                return
            if self.lista.actualizar_calificaciones(id, calificaciones):
                self.actualizar_estado('Calificaciones actualizadas')
                self.generar_reporte(None)
            else:
                self.actualizar_estado('Estudiante no encontrado')
        except Exception as e:
            self.actualizar_estado(f'Error: {e}')

    def calcular_promedio(self, instance):
        try:
            id = int(input("Ingrese ID del estudiante: "))
            promedio = self.lista.promedio_estudiante(id)
            if promedio is not None:
                self.actualizar_estado(f'Promedio del estudiante: {promedio:.2f}')
            else:
                self.actualizar_estado('Estudiante no encontrado')
        except Exception as e:
            self.actualizar_estado(f'Error: {e}')

    def generar_reporte(self, instance):
        reporte = self.lista.generar_reporte()
        self.actualizar_lista(reporte)
