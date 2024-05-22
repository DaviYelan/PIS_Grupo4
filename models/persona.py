class Persona:
    def __init__(self):
        self._id = 0
        self._nombre = ""
        self._apellido = ""
        self._dni = 0
        self._direccion = ""
        self._fecha_nacimiento = ""
        self._genero = ""
        self._telefono = 0

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, value):
        self._dni = value

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, value):
        self._direccion = value

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):
        self._fecha_nacimiento = value

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        self._genero = value

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, value):
        self._telefono = value


        
'''    @property
    def serializable(self):
        return {
            "id": self.id,
            "apellido": self.apellido,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "dni": self.DNI,
            "telefono": self.telefono,
            "genero": self.genero,
            "fechaNacimiento": self.fechaNacimiento
        }
        
    def deserializar(data): 
        persona = Persona()
        persona.id = data["id"]
        persona.apellido = data["apellido"]
        persona.nombre = data["nombre"]
        persona.direccion = data["direccion"]
        persona.DNI = data["dni"]
        persona.telefono = data["telefono"]
        persona.fechaNacimiento = data["fechaNacimiento"]
        return persona'''