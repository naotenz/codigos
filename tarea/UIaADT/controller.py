# controller.py

class ContadorController:
    """
    El Controlador conecta la Vista con el Modelo.
    Maneja las interacciones del usuario y actualiza la vista
    cuando los datos en el modelo cambian.
    """
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def manejar_incremento(self):
        """
        Esta función es llamada desde la Vista (el botón).
        Le pide al Modelo que se actualice y luego actualiza la Vista.
        """
        # 1. Actualizar el Modelo
        self.model.incrementar()

        # 2. Actualizar la Vista con los nuevos datos del Modelo
        self.actualizar_vista()

    def actualizar_vista(self):
        """
        Obtiene los datos del modelo y los muestra en la vista.
        """
        self.view.ids.etiqueta_numero.text = str(self.model.contador)