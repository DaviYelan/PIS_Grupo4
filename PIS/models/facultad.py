class Facultad:
    def __init__(self):
        self.__id = 0
        self.__nombre = ''

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
    def serializable(self):
        return {
            "id": self._id,
            "nombre": self._nombre
        }

    def deserializar(data):
        facultad = Facultad()
        facultad._id = data["id"]
        facultad._nombre = data["nombre"]
        return facultad
        
    def __str__(self):
        return f"{self._id} {self._nombre}"