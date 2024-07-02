class Factura:
    def __init__(self):
        self.__idChat = 0
        self.__emisor = 0
        self.__receptor = 0
        self.__mensaje = 0
        self.__fechaMensaje = 0
        self.__estadoMensaje = True

    @property
    def _idChat(self):
        return self.__idChat

    @_idChat.setter
    def _idChat(self, value):
        self.__idChat = value

    @property
    def _emisor(self):
        return self.__emisor

    @_emisor.setter
    def _emisor(self, value):
        self.__emisor = value

    @property
    def _receptor(self):
        return self.__receptor

    @_receptor.setter
    def _receptor(self, value):
        self.__receptor = value

    @property
    def _mensaje(self):
        return self.__mensaje

    @_mensaje.setter
    def _mensaje(self, value):
        self.__mensaje = value

    @property
    def _fechaMensaje(self):
        return self.__fechaMensaje

    @_fechaMensaje.setter
    def _fechaMensaje(self, value):
        self.__fechaMensaje = value

    @property
    def _estadoMensaje(self):
        return self.__estadoMensaje

    @_estadoMensaje.setter
    def _estadoMensaje(self, value):
        self.__estadoMensaje = value
