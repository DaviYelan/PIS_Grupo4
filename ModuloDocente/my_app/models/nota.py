from datetime import date


class Nota:
    def __init__(self, id: int, nota: float, notaFinalUnidad: float, fecha: date):
        self.id = id
        self.nota = nota
        self.notaFinalUnidad = notaFinalUnidad
        self.fecha = fecha

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_nota(self):
        return self.nota

    def set_nota(self, value):
        self.nota = value

    def get_notaFinalUnidad(self):
        return self.notaFinalUnidad

    def set_notaFinalUnidad(self, value):
        self.notaFinalUnidad = value

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, value):
        self.fecha = value
