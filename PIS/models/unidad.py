class Unidad:
    def __init__(self):
        self.__id = 0
        self.__nombre = ''
        self.__duracionSemanas = 0

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
    def _duracionSemanas(self):
        return self.__duracionSemanas

    @_duracionSemanas.setter
    def _duracionSemanas(self, value):
        self.__duracionSemanas = value

    @property
    def serializable(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "duracionSemanas": self._duracionSemanas
        }
    
    def deserializar(data):
        unidad = Unidad()
        unidad._id = data["id"]
        unidad._nombre = data["nombre"]
        unidad._duracionSemanas = data["duracionSemanas"]
        return unidad
    
    def __str__(self):
        return f"{self._id} {self._nombre} {self._duracionSemanas}"