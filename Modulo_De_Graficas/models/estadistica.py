class Estadistica:
    def __init__(self):
        self.__id = 0
        self.__tiempo = ''

    @property
    def _tiempo(self):
        return self.__tiempo

    @_tiempo.setter
    def _tiempo(self, value):
        self.__tiempo = value

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value
        
    @property
    def serializable(self):
        return {
            "id": self.__id,
            "tiempo": self.__tiempo
        }
    
    def deserializar(data):
        estadistica = Estadistica()
        estadistica._id = data["id"]
        estadistica._tiempo = data["tiempo"]
        return estadistica
    
    def __str__(self):
        return f"ID: {self._id}, Tiempo: {self._tiempo}"