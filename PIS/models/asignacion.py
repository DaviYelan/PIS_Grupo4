from models.cursa import Cursa
from models.docente import Docente
from models.materia import Materia
from models.rubrica import Rubrica


class Asignacion:
    def __init__(self):
        self.__id = 0
        self.__idCurso = Cursa()
        self.__idMateria = Materia()
        self.__idDocente = Docente()
        self.__idRubrica = Rubrica()

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _idCurso(self):
        return self.__idCurso

    @_idCurso.setter
    def _idCurso(self, value):
        self.__idCurso = value

    @property
    def _idMateria(self):
        return self.__idMateria

    @_idMateria.setter
    def _idMateria(self, value):
        self.__idMateria = value

    @property
    def _idDocente(self):
        return self.__idDocente

    @_idDocente.setter
    def _idDocente(self, value):
        self.__idDocente = value

    @property
    def _idRubrica(self):
        return self.__idRubrica

    @_idRubrica.setter
    def _idRubrica(self, value):
        self.__idRubrica = value


    @property
    def serializable(self):
        return {
            "id": self._id,
            "idCurso": self._idCurso.serializable,
            "idMateria": self._idMateria.serializable,
            "idDocente": self._idDocente.serializable,
            "idRubrica": self._idRubrica.serializable
        }