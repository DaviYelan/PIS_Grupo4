class Asignacion:
    def __init__(self, id: int, idCurso: int, idMateria: int, idDocente: int, idRubrica: int):
        self.id = id
        self.idCurso = idCurso
        self.idMateria = idMateria
        self.idDocente = idDocente
        self.idRubrica = idRubrica

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
    def idCurso(self):
        return self._idCurso

    @idCurso.setter
    def idCurso(self, value):
        if isinstance(value, int) and value > 0:
            self._idCurso = value
        else:
            raise ValueError("ID del Curso debe ser un entero positivo")

    @property
    def idMateria(self):
        return self._idMateria

    @idMateria.setter
    def idMateria(self, value):
        if isinstance(value, int) and value > 0:
            self._idMateria = value
        else:
            raise ValueError("ID de la Materia debe ser un entero positivo")

    @property
    def idDocente(self):
        return self._idDocente

    @idDocente.setter
    def idDocente(self, value):
        if isinstance(value, int) and value > 0:
            self._idDocente = value
        else:
            raise ValueError("ID del Docente debe ser un entero positivo")

    @property
    def idRubrica(self):
        return self._idRubrica

    @idRubrica.setter
    def idRubrica(self, value):
        if isinstance(value, int) and value > 0:
            self._idRubrica = value
        else:
            raise ValueError("ID de la Rúbrica debe ser un entero positivo")

    def __str__(self):
        return (f"Asignacion(id={self.id}, idCurso={self.idCurso}, idMateria={self.idMateria}, "
                f"idDocente={self.idDocente}, idRubrica={self.idRub
