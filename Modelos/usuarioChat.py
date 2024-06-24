class UsuarioChat:
    def __init__(self):
        self.__id = 0
        self.__fotouser = ''
        self.__estadoUsuario = bool = False 

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

