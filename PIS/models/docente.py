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
    def deserializar(cls, data):
        docente = Docente()
        docente._id = data.get("ID", 0)  
        docente._nombre = data.get("NOMBRE", "")
        docente._apellido = data.get("APELLIDO", "")
        docente._fecha = data.get("FECHA", "")
        docente._telefono = data.get("TELEFONO", "")
        docente._genero = data.get("GENERO", "")
        docente._correo = data.get("CORREO", "")
        docente._tipoIdentificacion = data.get("TIPOIDENTIFICACION", "")
        docente._tituloCuartoNivel = data.get("TITULOCUARTONIVEL", "")
        docente._especialidad = data.get("ESPECIALIDAD", "")
        docente._cubiculo = data.get("CUBICULO", "")
        return docente


    def __str__(self):
        return f"{super().__str__()} Titulo de cuarto nivel: {self._tituloCuartoNivel} Especialidad: {self._especialidad} Cubiculo: {self._cubiculo}"
