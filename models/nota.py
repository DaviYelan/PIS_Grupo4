class Nota:
    def __init__(self):
        self.__id = 0
        self.__notaFinal = 0
        self.__fecha = ''


    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _notaFinal(self):
        return self.__notaFinal

    @_notaFinal.setter
    def _notaFinal(self, value):
        self.__notaFinal = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

        
    @property
    def serializable(self):
        return {
            "id": self.__id,
            "notaFinal": self.__notaFinal,
            "fecha": self.__fecha
        }
    
    def deserializar(data):
        nota = Nota()
        nota._id = data["id"]
        nota._notaFinal = data["notaFinal"]
        nota._fecha = data["fecha"]
        return nota
    
    def __str__(self):
        return f"ID: {self._id}, Nota Final: {self._notaFinal}, Fecha : {self._fecha}"