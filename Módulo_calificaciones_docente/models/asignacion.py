class Asignacion:
    def __init__(self, ID, IdMateria, IdDocente):
        self.ID = ID
        self.IdMateria = IdMateria
        self.IdDocente = IdDocente

    def get_ID(self):
        return self.ID

    def set_ID(self, value):
        self.ID = value

    def get_IdMateria(self):
        return self.IdMateria

    def set_IdMateria(self, value):
        self.IdMateria = value

    def get_IdDocente(self):
        return self.IdDocente

    def set_IdDocente(self, value):
        self.IdDocente = value
