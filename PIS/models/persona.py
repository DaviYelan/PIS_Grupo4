class Persona:
    def __init__(self):
        self.__id = 0
        self.__nombre= ""
        self.__apellido= ""
        self.__direccion= ""
        self.__fechaNacimiento= ""
        self.__genero = ""
        self.__telefono = ""
        self.__tipoIdentificacion = ""
        self.__cedula = ""

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
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _fechaNacimiento(self):
        return self.__fechaNacimiento

    @_fechaNacimiento.setter
    def _fechaNacimiento(self, value):
        self.__fechaNacimiento = value

    @property
    def _genero(self):
        return self.__genero

    @_genero.setter
    def _genero(self, value):
        self.__genero = value

    @property
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value

    @property
    def _tipoIdentificacion(self):
        return self.__tipoIdentificacion

    @_tipoIdentificacion.setter
    def _tipoIdentificacion(self, value):
        self.__tipoIdentificacion = value

    @property
    def _cedula(self):
        return self.__cedula

    @_cedula.setter
    def _cedula(self, value):
        self.__cedula = value


    @property
    def serializable(self):
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
        persona = Persona()
        persona._id = data["id"]
        persona._nombre = data["nombre"]
        persona._apellido = data["apellido"]
        persona._direccion = data["direccion"]
        persona._fechaNacimiento = data["fechaNacimiento"]
        persona._genero = data["genero"]
        persona._telefono = data["telefono"]
        persona._tipoIdentificacion = data["tipoIdentificacion"]
        persona._cedula = data["cedula"]
        return persona
    
    def __str__(self):
        return f"ID: {self._id} Nombre: {self._nombre} Apellido: {self._apellido} Direccion: {self._direccion} Fecha de Nacimiento: {self._fechaNacimiento} Genero: {self._genero} Telefono: {self._telefono} Tipo de Identificacion: {self._tipoIdentificacion} Cedula: {self._cedula}"