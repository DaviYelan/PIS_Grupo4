class Cuenta:
    def __init__(self):
        self.__id = 0
        self.__correo = ""
        self.__clave = ""
        self.__estado = True

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _correo(self):
        return self.__correo

    @_correo.setter
    def _correo(self, value):
        self.__correo = value

    @property
    def _clave(self):
        return self.__clave

    @_clave.setter
    def _clave(self, value):
        self.__clave = value

    @property
    def _estado(self):
        return self.__estado

    @_estado.setter
    def _estado(self, value):
        self.__estado = value

    @property
    def serializable(self):
        return {
            "id": self.__id,
            "correo": self.__correo,
            "clave": self.__clave,
            "estado": self.__estado
        }
    
    def deserializar(data):
        cuenta = Cuenta()
        cuenta._id = data["id"]
        cuenta._correo = data["correo"]
        cuenta._clave = data["clave"]
        cuenta._estado = data["estado"]  # True or False
        return cuenta

    def __str__(self):
        return f"{self.__id} - {self.__correo} - {self.__clave} - {self.__estado}"