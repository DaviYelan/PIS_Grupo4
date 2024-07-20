from models.persona import Persona

class Alumno(Persona):
    def __init__(self):
        super().__init__()
        self.__tipo = ""
        self.__orden = ""
        self.__ciclo = ""

    @property
    def _tipo(self):
        return self.__tipo

    @_tipo.setter
    def _tipo(self, value):
        self.__tipo = value

    @property
    def _orden(self):
        return self.__orden

    @_orden.setter
    def _orden(self, value):
        self.__orden = value

    @property
    def _ciclo(self):
        return self.__ciclo

    @_ciclo.setter
    def _ciclo(self, value):
        self.__ciclo = value

    @property
    def serializable(self):
        return {
            "tipo": self._tipo,
            "orden": self._orden,
            "ciclo": self._ciclo
       
        }

    @classmethod
    def deserializar(self, data):
        docente = Alumno()
        docente._tipo = data["tipo"]
        docente._orden = data["orden"]
        docente._ciclo = data["ciclo"]
        return docente
    
    def __str__(self):
        return f"{super().__str__()} Tipo: {self._tipo} Orden: {self._orden} Ciclo: {self._ciclo}"