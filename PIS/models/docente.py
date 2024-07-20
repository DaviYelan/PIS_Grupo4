from models.persona import Persona

class Docente(Persona):
    def __init__(self):
        super().__init__()
        self.__tituloCuartoNivel = ""
        self.__especialidad = ""
        self.__cubiculo = ""


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
            "tituloCuartoNivel": self._tituloCuartoNivel,
            "especialidad": self._especialidad,
            "cubiculo": self._cubiculo
       
        }

    @classmethod
    def deserializar(self, data):
        docente = Docente()
        docente._tituloCuartoNivel = data["tituloCuartoNivel"]
        docente._especialidad = data["especialidad"]
        docente._cubiculo = data["cubiculo"]
        return docente
    
    def __str__(self):
        return f"{super().__str__()} Titulo de cuarto nivel: {self._tituloCuartoNivel} Especialidad: {self._especialidad} Cubiculo: {self._cubiculo}"