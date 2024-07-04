class Universidad:
    def __init__(self):
        self.__id = 0
        self.__nombre = ''
        self.__ciudad = ''
        self.__direccion = ''
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
    def _ciudad(self):
        return self.__ciudad

    @_ciudad.setter
    def _ciudad(self, value):
        self.__ciudad = value

    @property
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _pais(self):
        return self.__pais

    @_pais.setter
    def _pais(self, value):
        self.__pais = value

    @property
    def serializable(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "ciudad": self._ciudad,
            "direccion": self._direccion,
        }
    
    def deserializar(data):
        universidad = Universidad()
        universidad._id = data["id"]
        universidad._nombre = data["nombre"]
        universidad._ciudad = data["ciudad"]
        universidad._direccion = data["direccion"]
        return universidad
    
    def __str__(self):
        return f"{self._id} {self._nombre} {self._ciudad} {self._direccion}"