from models.persona import Persona

class Estudiante:
    def __init__(self):
        super.__init__(Persona)
        self.matricula = 0
        self.estado= bool

    def get_matricula(self):
        return self.matricula

    def set_matricula(self, value):
        self.matricula = value

    def get_estado(self):
        return self.estado

    def set_estado(self, value):
        self.estado = value