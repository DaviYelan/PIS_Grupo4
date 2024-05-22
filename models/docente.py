from models.persona import Persona

class Docente(Persona):
    def __init__(self):
        super().__init__()
        self._credencial = 0

    @property
    def credencial(self):
        return self._credencial

    @credencial.setter
    def credencial(self, value):
        self._credencial = value