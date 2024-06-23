class InstrumentoEvaluacion:
    def __init__(self, id: int, descripcion: str):
        self.id = id
        self.descripcion = descripcion

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, value):
        self.descripcion = value
