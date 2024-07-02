from models.enumComponenteRubrica import EnumComponenteRubrica
from models.nota import Nota

class Rubrica:
    def __init__(self):
        self.__id = 0
        self.__componente = EnumComponenteRubrica
        self.__idInstrumentoEvaluacion = 0
        self.__idNota = Nota()
        self.__ponderacion = 0.0


    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _componente(self):
        return self.__componente

    @_componente.setter
    def _componente(self, value):
        self.__componente = value

    @property
    def _idInstrumentoEvaluacion(self):
        return self.__idInstrumentoEvaluacion

    @_idInstrumentoEvaluacion.setter
    def _idInstrumentoEvaluacion(self, value):
        self.__idInstrumentoEvaluacion = value

    @property
    def _idNota(self):
        return self.__idNota

    @_idNota.setter
    def _idNota(self, value):
        self.__idNota = value

    @property
    def _ponderacion(self):
        return self.__ponderacion

    @_ponderacion.setter
    def _ponderacion(self, value):
        self.__ponderacion = value

    @property
    def serializable(self):
        return {
            "id": self._id,
            "componente": self._componente,
            "idInstrumentoEvaluacion": self._idInstrumentoEvaluacion,
            "idNota": self._idNota.serializable,
            "ponderacion": self._ponderacion
        }
    
    def deserializar(self, data):
        rubrica = Rubrica()
        rubrica._id = data["id"]
        rubrica._componente = data["componente"]
        rubrica._idInstrumentoEvaluacion = data["idInstrumentoEvaluacion"]
        rubrica._idNota = data["idNota"]
        rubrica._ponderacion = data["ponderacion"]
        return rubrica