class Grafico:
    def __init__(self):
        self.__id = 0
        self.__tipoGrafico = ''

    @property
    def _tipoGrafico(self):
        return self.__tipoGrafico

    @_tipoGrafico.setter
    def _tipoGrafico(self, value):
        self.__tipoGrafico = value

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
            "tipoGrafico": self.__tipoGrafico
        }
    
    def deserializar(data):
        grafico = Grafico()
        grafico._id = data["id"]
        grafico._tipoGrafico = data["tipoGrafico"]
        return grafico
    
    def __str__(self):
        return f"ID: {self._id}, Tipo de Grafico: {self._tipoGrafico}"
        