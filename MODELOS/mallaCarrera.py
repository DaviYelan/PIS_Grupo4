class MallaCarrera:
    def __init__(self) -> None:
        self.__id= 0
        self.__nombre = ""

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
    def serialize(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            
            
        }

    def deserializar(self, data):
        malla = MallaCarrera()
        malla._id = data["id"]
        malla._nombre = data["nombre"]
        
    
    def __str__(self) -> str:
        return "Usuario: " + self._nombre + " " + self._id  + "\n"
    
    __repr__ = __str__