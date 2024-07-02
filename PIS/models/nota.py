from datetime import date


class Nota:
    def __init__(self):
        self.__id = 0
        self.__nota = 0.0
        self.__notaFinalUnidad = 0.0
        self.__fecha = date

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nota(self):
        return self.__nota

    @_nota.setter
    def _nota(self, value):
        self.__nota = value

    @property
    def _notaFinalUnidad(self):
        return self.__notaFinalUnidad

    @_notaFinalUnidad.setter
    def _notaFinalUnidad(self, value):
        self.__notaFinalUnidad = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def serializable(self):
        return {
            "id": self._id,
            "nota": self._nota,
            "notaFinalUnidad": self._notaFinalUnidad,
            "fecha": self._fecha
        }
    
    def deserializar(self, data):
        nota = Nota()
        nota._id = data["id"]
        nota._nota = data["nota"]
        nota._notaFinalUnidad = data["notaFinalUnidad"]
        nota._fecha = data["fecha"]
        return nota
    
    def __str__(self):
        return f"ID: {self._id} Nota: {self._nota} Nota final de la unidad: {self._notaFinalUnidad} Fecha: {self._fecha}"