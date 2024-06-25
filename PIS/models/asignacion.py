class Asignacion:
    def __init__(self, id: int, idCurso: int, idMateria: int, idDocente: int, idRubrica: int):
        self.id = id
        self.idCurso = idCurso
        self.idMateria = idMateria
        self.idDocente = idDocente
        self.idRubrica = idRubrica

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_idCurso(self):
        return self.idCurso

    def set_idCurso(self, value):
        self.idCurso = value

    def get_idMateria(self):
        return self.idMateria

    def set_idMateria(self, value):
        self.idMateria = value

    def get_idDocente(self):
        return self.idDocente

    def set_idDocente(self, value):
        self.idDocente = value

    def get_idRubrica(self):
        return self.idRubrica

    def set_idRubrica(self, value):
        self.idRubrica = value
