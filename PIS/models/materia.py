class Materia:
    def __init__(self):
        self.__id = 0  
        self.__nombre = ""
        self.__codigo = ""
        self.__numeroHoraSemanal = 0
        self.__ciclo = 0

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
    def _codigo(self):
        return self.__codigo

    @_codigo.setter
    def _codigo(self, value):
        self.__codigo = value

    @property
    def _numeroHoraSemanal(self):
        return self.__numeroHoraSemanal

    @_numeroHoraSemanal.setter
    def _numeroHoraSemanal(self, value):
        self.__numeroHoraSemanal = value

    @property
    def _ciclo(self):
        return self.__ciclo

    @_ciclo.setter
    def _ciclo(self, value):
        self.__ciclo = value

    @property
    def serializable(self):
        return {
            "nombre": self._nombre,
            "codigo": self._codigo,
            "numeroHoraSemanal": self._numeroHoraSemanal,
            "ciclo": self._ciclo
        }

    @classmethod
    def deserializar(cls, data):
        materia = Materia()
        materia._id = data.get("ID", 0)
        materia._nombre = data.get("NOMBRE", "")
        materia._codigo = data.get("CODIGO", "")
        materia._numeroHoraSemanal = data.get("NUMEROHORASEMANAL", 0)
        materia._ciclo = data.get("CICLO", 0)
        return materia

    def __str__(self):
        return f"{self._id} {self._nombre} {self._codigo} {self._numeroHoraSemanal} {self._ciclo}"
