class Malla:
    def __init__(self):
        self.__id = 0
        self.__nombre = ""
        self.__estado = True 

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
    def _estado(self):
        return self.__estado

    @_estado.setter
    def _estado(self, value):
        self.__estado = value

    @property
    def serializable(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "estado": self._estado
        }
    
    def deserializar(data):
        malla = Malla()
        malla._id = data["id"]
        malla._nombre = data["nombre"]
        malla._estado = data["estado"]
        return malla
    
    def __str__(self):
        return f"Malla: {self._nombre}"