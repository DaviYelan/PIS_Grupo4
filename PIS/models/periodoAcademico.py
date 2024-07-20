from models.enumEstadoPeriodo import EnumEstadoPeriodo
import datetime
class PeriodoAcademico:
    def __init__(self):
        self.__id = 0
        self.__nombre = ''
        self.__fechaInicio = datetime
        self.__fechaFin = datetime
        self.__tipoEstado = EnumEstadoPeriodo

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _fechaInicio(self):
        return self.__fechaInicio

    @_fechaInicio.setter
    def _fechaInicio(self, value):
        self.__fechaInicio = value

    @property
    def _fechaFin(self):
        return self.__fechaFin

    @_fechaFin.setter
    def _fechaFin(self, value):
        self.__fechaFin = value

    @property
    def _tipoEstado(self):
        return self.__tipoEstado

    @_tipoEstado.setter
    def _tipoEstado(self, value):
        self.__tipoEstado = value



    @property
    def serializable(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "fechaInicio": self._fechaInicio,
            "fechaFin": self._fechaFin,
            "tipoEstado": self._tipoEstado
        }
    @classmethod
    def deserializar(data):
        periodo = PeriodoAcademico()
        periodo._id = data["id"]
        periodo._nombre = data["nombre"]
        periodo._fechaInicio = data["fechaInicio"]
        periodo._fechaFin = data["fechaFin"]
        periodo._tipoEstado = data["tipoEstado"]
        return periodo

    def __str__(self):
        return f"{self._id} {self._nombre} {self._fechaInicio} {self._fechaFin} {self._tipoEstado}"