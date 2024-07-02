class InstrumentoEvaluacion:
    def __init__(self):
        self.__id = 0
        self.__descripcion = ""

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _descripcion(self):
        return self.__descripcion

    @_descripcion.setter
    def _descripcion(self, value):
        self.__descripcion = value

    @property
    def serializable(self):
        return {
            "id": self._id,
            "descripcion": self._descripcion
        }

    def deserializar(self, data):
        instrumentoEvaluacion = InstrumentoEvaluacion()
        instrumentoEvaluacion._id = data["id"]
        instrumentoEvaluacion._descripcion = data["descripcion"]
        return instrumentoEvaluacion

    def __str__(self):
        return f"Id: {self._id} Descripcion: {self._descripcion}"
