from datetime import date

class Nota:
    def __init__(self, id: int, nota: float, notaFinalUnidad: float, fecha: date):
        self.id = id
        self.nota = nota
        self.notaFinalUnidad = notaFinalUnidad
        self.fecha = fecha

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if isinstance(value, int) and value > 0:
            self._id = value
        else:
            raise ValueError("ID debe ser un entero positivo")

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, value):
        if 0 <= value <= 10:  
            self._nota = value
        else:
            raise ValueError("Nota debe estar entre 0 y 10")

    @property
    def notaFinalUnidad(self):
        return self._notaFinalUnidad

    @notaFinalUnidad.setter
    def notaFinalUnidad(self, value):
        if 0 <= value <= 10:  
            self._notaFinalUnidad = value
        else:
            raise ValueError("Nota final debe estar entre 0 y 10")

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        if isinstance(value, date):
            self._fecha = value
        else:
            raise ValueError("Fecha debe ser un objeto de tipo date")
