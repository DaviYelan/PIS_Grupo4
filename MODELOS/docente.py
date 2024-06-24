from model.persona import Persona

class Docente(Persona):
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
        docente = Docente()
        docente._id = data["id"]
        docente._nombre = data["nombre"]
        docente._apellido = data["apellido"]
        docente._direccion = data["direccion"]
        docente._fechaNacimiento = data["fechaNacimiento"]
        docente._genero = data["genero"]
        docente._telefono = data["telefono"]
        docente._tipoIdentificacion = data["tipoIdentificacion"]
        docente._cedula = data["cedula"]
        return docente
    
    def __str__(self) -> str:
        return "Usuario: " + self._nombre + " " + self._fechaNacimiento + " Monto:" + str(self._cedula) + "\n"
    
    __repr__ = __str__
