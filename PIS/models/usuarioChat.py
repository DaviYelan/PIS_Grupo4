class UsuarioChat:
    def __init__(self):
        self.__id = 0
        self.__fotouser = ''
        self.__estadoUsuario = False 

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _fotouser(self):
        return self.__fotouser

    @_fotouser.setter
    def _fotouser(self, value):
        self.__fotouser = value

    @property
    def _estadoUsuario(self):
        return self.__estadoUsuario

    @_estadoUsuario.setter
    def _estadoUsuario(self, value):
        self.__estadoUsuario = value

    @property
    def serializable(self):
        return {
            "id": self._id,
            "fotouser": self._fotouser,
            "estadoUsuario": self._estadoUsuario
        }
    
    def deserializar(self, data):
        usuarioChat = UsuarioChat()
        usuarioChat._id = data["id"]
        usuarioChat._fotouser = data["fotouser"]
        usuarioChat._estadoUsuario = data["estadoUsuario"]
        return usuarioChat

    def __str__(self):
        return f"Id: {self._id} Fotouser: {self._fotouser} EstadoUsuario: {self._estadoUsuario}"