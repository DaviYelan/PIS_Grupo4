class Rubrica:
    def __init__(self, ID, componente, instrumentoEvaluacion, ponderacion):
        self.ID = ID
        self.componente = componente
        self.instrumentoEvaluacion = instrumentoEvaluacion
        self.ponderacion = ponderacion

    def get_ID(self):
        return self.ID

    def set_ID(self, value):
        self.ID = value

    def get_componente(self):
        return self.componente

    def set_componente(self, value):
        self.componente = value

    def get_instrumentoEvaluacion(self):
        return self.instrumentoEvaluacion

    def set_instrumentoEvaluacion(self, value):
        self.instrumentoEvaluacion = value

    def get_ponderacion(self):
        return self.ponderacion

    def set_ponderacion(self, value):
        self.ponderacion = value

