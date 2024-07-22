
class Cursa:
    def __init__(self):
        self.__id = 0
        self.__paralelo = ""
    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _paralelo(self):
        return self.__paralelo

    @_paralelo.setter
    def _paralelo(self, value):
        self.__paralelo = value

    @property
    def _idEstudiante(self):
        return self.__idEstudiante

    @_idEstudiante.setter
    def _idEstudiante(self, value):
        self.__idEstudiante = value

    @property
    def _idAsignacion(self):
        return self.__idAsignacion

    @_idAsignacion.setter
    def _idAsignacion(self, value):
        self.__idAsignacion = value
   
    @property
    def serializable(self):
        return {
            "id": self._id,
            "paralelo": self._paralelo,
        }

    @classmethod
    def deserializar(cls, data):
        cursa = Cursa()
        cursa._id = data.get("ID", 0)
        cursa._paralelo = data.get("PARALELO", "")
        return cursa
    
    def __str__(self):
        return f"{self._id} {self._paralelo}"