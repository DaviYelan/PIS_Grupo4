from typing import Type
from controllers.dao.daoAdapter import DaoAdapter
from models.persona import Persona
from controllers.connecction.connection import Connection  # Asegúrate de importar la clase Connection

class PersonaDaoControl(DaoAdapter):
    def __init__(self):
        self.db_connection = Connection()
        self.db_connection.connect()
        super().__init__(Persona, self.db_connection)
        self.__persona = None

    @property
    def _persona(self):
        if self.__persona is None:
            self.__persona = Persona()
        return self.__persona

    @_persona.setter
    def _persona(self, value):
        self.__persona = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._save(self._persona)
    
    def merge(self, pos):
        self._merge(self._persona, pos)
    
    def delete(self, pos):
        self._delete(pos)
    
    def __del__(self):
        self.db_connection.close()
