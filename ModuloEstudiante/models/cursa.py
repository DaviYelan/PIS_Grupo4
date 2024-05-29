class Cursa:
    def __init__(self):
        self.__id = 0
        self.__paralelo = ""
        self.__codigoAula = ""
        self.__idEstudiante = 0
        self.__idAsignacion = 0


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
    def _codigoAula(self):
        return self.__codigoAula

    @_codigoAula.setter
    def _codigoAula(self, value):
        self.__codigoAula = value

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
            "codigoAula": self._codigoAula,
            "idEstudiante": self._idEstudiante,
            "idAsignacion": self._idAsignacion
        }

    def deserializar(data):
        cursa = Cursa()
        cursa._id = data["id"]
        cursa._paralelo = data["paralelo"]
        cursa._codigoAula = data["codigoAula"]
        cursa._idEstudiante = data["idEstudiante"]
        cursa._idAsignacion = data["idAsignacion"]
        return cursa
    
    def __str__(self):
        return f"Cursa: {self._paralelo} {self._codigoAula} {self._idEstudiante} {self._idAsignacion}"