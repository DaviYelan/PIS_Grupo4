class Materia:
    def __init__(self):
        self.__id = ""
        self.__nombre =""
        self.__codigo= ""
        self.__horaSemanal= 0.0
        self.__nombCiclo= ""

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _codigo(self):
        return self.__codigo

    @_codigo.setter
    def _codigo(self, value):
        self.__codigo = value

    @property
    def _horaSemanal(self):
        return self.__horaSemanal

    @_horaSemanal.setter
    def _horaSemanal(self, value):
        self.__horaSemanal = value

    @property
    def _nombCiclo(self):
        return self.__nombCiclo

    @_nombCiclo.setter
    def _nombCiclo(self, value):
        self.__nombCiclo = value

    

    @property
    def serialize(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "codigo": self._codigo,
            "horaSemanal": self._horaSemanal,
            "nombCiclo": self._nombCiclo
            
        }

    def deserializar(self, data):
        materia = Materia()
        materia._id = data["id"]
        materia._nombre = data["nombre"]
        materia._codigo = data["codigo"]
        materia._horaSemanal = data["horaSemanal"]
        materia._nombCiclo = data["nombCiclo"]
        
        return materia
    
    def __str__(self) -> str:
        return "Usuario: " + self._nombre + " " + self._codigo + " Monto:" + str(self._horaSemanal) + "Ciclo:" +self._nombCiclo+"\n"
    
    __repr__ = __str__
