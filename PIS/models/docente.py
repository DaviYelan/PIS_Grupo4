from models.persona import Persona

class Docente(Persona):
    def __init__(self):
        super().__init__()
        self.__id = 0
        self.__tituloCuartoNivel = ""
        self.__especialidad = ""
        self.__cubiculo = ""

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _tituloCuartoNivel(self):
        return self.__tituloCuartoNivel

    @_tituloCuartoNivel.setter
    def _tituloCuartoNivel(self, value):
        self.__tituloCuartoNivel = value

    @property
    def _especialidad(self):
        return self.__especialidad

    @_especialidad.setter
    def _especialidad(self, value):
        self.__especialidad = value

    @property
    def _cubiculo(self):
        return self.__cubiculo

    @_cubiculo.setter
    def _cubiculo(self, value):
        self.__cubiculo = value
    @property
    def serializable(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "apellido": self._apellido,
            "fecha": self._fecha,
            "telefono": self._telefono,
            "genero": self._genero,
            "correo": self._correo,
            "tipoIdentificacion": self._tipoIdentificacion,
            "tituloCuartoNivel": self._tituloCuartoNivel,
            "especialidad": self._especialidad,
            "cubiculo": self._cubiculo
       
        }

    @classmethod
    def deserializar(self, data):
        docente = Docente()
        docente._id = data["id"]
        docente._nombre = data["nombre"]
        docente._apellido = data["apellido"]
        docente._fecha = data["fecha"]
        docente._telefono = data["telefono"]
        docente._genero = data["genero"]
        docente._correo = data["correo"]
        docente._tipoIdentificacion = data["tipoIdentificacion"]
        docente._tituloCuartoNivel = data["tituloCuartoNivel"]
        docente._especialidad = data["especialidad"]
        docente._cubiculo = data["cubiculo"]
        return docente
    
    def __str__(self):
        return f"{super().__str__()} Titulo de cuarto nivel: {self._tituloCuartoNivel} Especialidad: {self._especialidad} Cubiculo: {self._cubiculo}"