from models.enumTipoIdentificacion import EnumTipoIdentificacion
class Persona:
    def __init__(self):
        self.__id = 0  
        self.__nombres = ""
        self.__apellidos = ""
        self.__dni = ""
        self.__telefono = ""
        self.__correo = ""
        self.__fecha = ""
        self.__genero = ""
        self.__tipoIdentificacion = EnumTipoIdentificacion.CEDULA

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
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _dni(self):
        return self.__dni

    @_dni.setter
    def _dni(self, value):
        self.__dni = value

    @property
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value
    
    @property
    def _correo(self):
        return self.__correo

    @_correo.setter
    def _correo(self, value):
        self.__correo = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def _genero(self):
        return self.__genero

    @_genero.setter
    def _genero(self, value):
        self.__genero = value

    @property
    def _tipoIdentificacion(self):
        return self.__tipoIdentificacion

    @_tipoIdentificacion.setter
    def _tipoIdentificacion(self, value):
        self.__tipoIdentificacion = value
   
    
    @property
    def serializable(self): 
        return {
            "id": self.__id,
            "apellido": self.__apellido,
            "nombre": self.__nombre,
            "telefono": self.__telefono,
            "correo": self.__correo,
            "fecha": self.__fecha,
            "genero": self.__genero,
            "tipo": self.__tipoIdentificacion
        }
    

    def deserializar(data):
        persona = Persona()
        persona._id = data["id"]
        persona._apellido = data["apellido"]
        persona._nombre = data["nombre"]
        persona._telefono = data["telefono"]
        persona.__correo = data["correo"]
        persona.__fecha = data["fecha"]
        persona.__genero = data["genero"]
        persona._tipoIdentificacion = data["tipo"] 

        return persona

    def __str__(self) -> str:
        return "{" + str(self.__id) + ": " + self.__apellidos + " " + self.__nombres + "}"
 
    
