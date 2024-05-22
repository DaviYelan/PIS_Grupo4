class Cursa:
    def __init__(self):
        self.__id = 0
        self.__paralelo = ""

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _paralelo(self):
        return self.__paralelo

    @_paralelo.setter
    def _paralelo(self, value):
        self.__paralelo = value

    @property
    def serializable(self):
        return {
            "id": self._id,
            "paralelo": self._paralelo
        }

    def deserializar(data):
        cursa = Cursa()
        cursa._id = data["id"]
        cursa._paralelo = data["paralelo"]
        return cursa
    
    def __str__(self):
        return f"Cursa: {self._paralelo}"