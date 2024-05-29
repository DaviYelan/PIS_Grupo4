class PeriodoAcademico:
    def __init__(self, nombre, fechaInicio, fechaFin):
        self.__id = 0
        self.__nombre = nombre
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin
        self.__estadoPa = True

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
    def _estadoPa(self):
        return self.__estadoPa

    @_estadoPa.setter
    def _estadoPa(self, value):
        self.__estadoPa = value

    @property
    def serializable(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "fechaInicio": self._fechaInicio,
            "fechaFin": self._fechaFin,
            "estadoPa": self._estadoPa
        }
    
    def deserializar(data):
        periodoAcademico = PeriodoAcademico(data["nombre"], data["fechaInicio"], data["fechaFin"])
        periodoAcademico._id = data["id"]
        periodoAcademico._estadoPa = data["estadoPa"]
        return periodoAcademico
    
    def __str__(self):
        return f"Periodo Académico: {self._nombre} ({self._fechaInicio} - {self._fechaFin})"