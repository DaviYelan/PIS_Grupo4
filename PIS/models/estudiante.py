from models.enumEstadoEstudiante import EnumEstadoEstudiante

class Estudiante:
    def __init__(self):
        self.__id = 0  
        self.__tipo = ""
        self.__estado = EnumEstadoEstudiante.PRIMERA

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _tipo(self):
        return self.__tipo

    @_tipo.setter
    def _tipo(self, value):
        self.__tipo = value

    @property
    def _estado(self):
        return self.__estado

    @_estado.setter
    def _estado(self, value):
        self.__estado = value

    @property
    def serializable(self):
        return {
            "id": self.__id,
            "estado": self.__estado,
            "tipo": self.__tipo
            
        }
    
    @staticmethod
    def deserializar(data):
        edc = Estudiante()
        edc._id = data["id"]
        edc._estado = data["estado"] 
        edc._tipo = data["tipo"]
        return edc


      