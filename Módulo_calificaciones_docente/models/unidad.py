class Unidad:
    def __init__(self, ID, actividade, tema):
        self.ID = ID
        self.actividade = actividade
        self.tema = tema

    def get_ID(self):
        return self.ID

    def set_ID(self, value):
        self.ID = value

    def get_actividade(self):
        return self.actividade

    def set_actividade(self, value):
        self.actividade = value

    def get_tema(self):
        return self.tema

    def set_tema(self, value):
        self.tema = value
