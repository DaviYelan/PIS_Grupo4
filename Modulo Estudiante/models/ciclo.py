class Ciclo:
    def __init__(self):
        self.__id = 0
        self.__numeroCiclos = 0

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _numeroCiclos(self):
        return self.__numeroCiclos

    @_numeroCiclos.setter
    def _numeroCiclos(self, value):
        self.__numeroCiclos = value

    @property
    def serializable(self):
        return {
            "id": self._id,
            "numeroCiclos": self._numeroCiclos
        }
    
    def deserializar(data):
        ciclo = Ciclo()
        ciclo._id = data["id"]
        ciclo._numeroCiclos = data["numeroCiclos"]
        return ciclo
    
    def __str__(self):
        return f"Ciclo: {self._numeroCiclos}"