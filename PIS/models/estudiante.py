# estudiante.py
from models.persona import Persona

class Estudiante(Persona):
    def __init__(self):
        super().__init__()

    @property
    def serialize(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "apellido": self._apellido,
            "direccion": self._direccion,
            "fechaNacimiento": self._fechaNacimiento,
            "genero": self._genero,
            "telefono": self._telefono,
            "tipoIdentificacion": self._tipoIdentificacion,
            "cedula": self._cedula
        }

    def deserializar(self, data):
        estudiante = Estudiante()
        estudiante._id = data["id"]
        estudiante._nombre = data["nombre"]
        estudiante._apellido = data["apellido"]
        estudiante._direccion = data["direccion"]
        estudiante._fechaNacimiento = data["fechaNacimiento"]
        estudiante._genero = data["genero"]
        estudiante._telefono = data["telefono"]
        estudiante._tipoIdentificacion = data["tipoIdentificacion"]
        estudiante._cedula = data["cedula"]
        return estudiante
    
    def __str__(self) -> str:
        return "Usuario: " + self._nombre + " " + self._fechaNacimiento + " Monto:" + str(self._cedula) + "\n"
    
    __repr__ = __str__
