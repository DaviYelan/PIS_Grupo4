class Materia:
    def __init__(self):
        self.__id = 0  
        self.__nombre = ""
        self.__numeroHoraSemana = 0

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
    def _numeroHoraSemana(self):
        return self.__numeroHoraSemana

    @_numeroHoraSemana.setter
    def _numeroHoraSemana(self, value):
        self.__numeroHoraSemana = value

    @property
    def serializable(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "numeroHoraSemana": self._numeroHoraSemana
        }
    
    def deserializar(data):
        materia = Materia()
        materia._id = data["id"]
        materia._nombre = data["nombre"]
        materia._numeroHoraSemana = data["numeroHoraSemana"]
        return materia