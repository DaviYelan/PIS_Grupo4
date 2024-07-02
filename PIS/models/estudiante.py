# estudiante.py
from models.enumEstadoEstudiante import EnumEstadoEstudiante
from models.persona import Persona

class Estudiante(Persona):
    def __init__(self):
        super().__init__()
        self.__estado = EnumEstadoEstudiante
        self.__matricula = ""

    @property
    def _estado(self):
        return self.__estado

    @_estado.setter
    def _estado(self, value):
        self.__estado = value

    @property
    def _matricula(self):
        return self.__matricula

    @_matricula.setter
    def _matricula(self, value):
        self.__matricula = value

    @property
    def serializable(self):
        return {
            "estado": self._estado,
            "matricula": self._matricula
        }

    def deserializar(self, data):
        estudiante = Estudiante()
        estudiante._estado = data["estado"]
        estudiante._matricula = data["matricula"]
        return estudiante
    
    def __str__(self):
        return f"{super().__str__()} Estado: {self._estado} Matricula: {self._matricula}"
