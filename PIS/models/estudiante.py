from models.persona import Persona

class Estudiante(Persona):
    def __init__(self):
        super().__init__()
        self.__id = ""
        self.__orden = ""
        self.__ciclo = 0

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _orden(self):
        return self.__orden

    @_orden.setter
    def _orden(self, value):
        self.__orden = value

    @property
    def _ciclo(self):
        return self.__ciclo

    @_ciclo.setter
    def _ciclo(self, value):
        self.__ciclo = value

    @property
    def serializable(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "apellido": self._apellido,
            "fecha": self._fecha,
            "genero": self._genero,
            "telefono": self._telefono,
            "correo": self._correo,
            "orden": self._orden,
            "ciclo": self._ciclo
       
        }

    @classmethod
    def deserializar(self, data):
        docente = Estudiante()
        docente._id = data["id"]
        docente._nombre = data["nombre"]
        docente._apellido = data["apellido"]
        docente._fecha = data["fecha"]
        docente._genero = data["genero"]
        docente._telefono = data["telefono"]
        docente._correo = data["correo"]
        docente._orden = data["orden"]
        docente._ciclo = data["ciclo"]
        return docente
    
    def __str__(self):
        return f"{super().__str__()} Tipo: {self._tipo} Orden: {self._orden} Ciclo: {self._ciclo}"