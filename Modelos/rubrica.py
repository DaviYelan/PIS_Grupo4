from models.componenteRubrica import ComponenteRubrica

class Rubrica:
    def __init__(self, id: int, componente: ComponenteRubrica, idInstrumentoEvaluacion: int, idNota: int, ponderacion: str):
        self.id = id
        self.componente = componente
        self.idInstrumentoEvaluacion = idInstrumentoEvaluacion
        self.idNota = idNota
        self.ponderacion = ponderacion

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
    def componente(self):
        return self._componente

    @componente.setter
    def componente(self, value):
        if isinstance(value, ComponenteRubrica):
            self._componente = value
        else:
            raise ValueError("Componente debe ser una instancia de ComponenteRubrica")

    @property
    def idInstrumentoEvaluacion(self):
        return self._idInstrumentoEvaluacion

    @idInstrumentoEvaluacion.setter
    def idInstrumentoEvaluacion(self, value):
        if isinstance(value, int) and value > 0:
            self._idInstrumentoEvaluacion = value
        else:
            raise ValueError("ID del Instrumento de Evaluación debe ser un entero positivo")

    @property
    def idNota(self):
        return self._idNota

    @idNota.setter
    def idNota(self, value):
        if isinstance(value, int) and value > 0:
            self._idNota = value
        else:
            raise ValueError("ID de la Nota debe ser un entero positivo")

    @property
    def ponderacion(self):
        return self._ponderacion

    @ponderacion.setter
    def ponderacion(self, value):
        if isinstance(value, str) and value:
            self._ponderacion = value
        else:
            raise ValueError("Ponderación debe ser una cadena no vacía")
