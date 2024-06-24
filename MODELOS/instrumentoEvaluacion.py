class InstrumentoEvaluacion:
    def __init__(self, id: int, descripcion: str):
        self.id = id
        self.descripcion = descripcion

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if isinstance(value, int) and value > 0:
            self._id = value
        else:
            raise ValueError("ID debe ser un entero positivo")

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        if isinstance(value, str) and value:
            self._descripcion = value
        else:
            raise ValueError("Descripción debe ser una cadena no vacía")

    def __str__(self):
        return f"InstrumentoEvaluacion(id={self.id}, descripcion={self.descripcion})"
