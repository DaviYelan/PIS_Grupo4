from models.componenteRubrica import ComponenteRubrica

class Rubrica:
    def __init__(self, id: int, componente: ComponenteRubrica, idInstrumentoEvaluacion: int, idNota: int, ponderacion: str):
        self.id = id
        self.componente = componente
        self.idInstrumentoEvaluacion = idInstrumentoEvaluacion
        self.idNota = idNota
        self.ponderacion = ponderacion

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_componente(self):
        return self.componente

    def set_componente(self, value):
        self.componente = value

    def get_idInstrumentoEvaluacion(self):
        return self.idInstrumentoEvaluacion

    def set_idInstrumentoEvaluacion(self, value):
        self.idInstrumentoEvaluacion = value

    def get_idNota(self):
        return self.idNota

    def set_idNota(self, value):
        self.idNota = value

    def get_ponderacion(self):
        return self.ponderacion

    def set_ponderacion(self, value):
        self.ponderacion = value
