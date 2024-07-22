class Asignacion:
    def __init__(self):
        self.__id = 0
        self.__idMateria = None
        self.__idDocente = None

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _idMateria(self):
        return self.__idMateria

    @_idMateria.setter
    def _idMateria(self, value):
        self.__idMateria = value

    @property
    def _idDocente(self):
        return self.__idDocente

    @_idDocente.setter
    def _idDocente(self, value):
        self.__idDocente = value

    @property
    def serializable(self):
        return {
            "id": self._id,
            "idMateria": self._idMateria,
            "idDocente": self._idDocente
        }

    @classmethod
    def deserializar(cls, data):
        asignacion = Asignacion()
        asignacion._id = data.get("id", 0)
        asignacion._idMateria = data.get("idMateria")
        asignacion._idDocente = data.get("idDocente")
        return asignacion
