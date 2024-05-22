
from typing import Type
from controls.dao.daoAdapter import DaoAdapter
from models.estudiante import Estudiante

class PersonaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Estudiante)
        self.__persona = None
        

    @property
    def _persona(self):
        if self.__persona == None:
            self.__persona = Estudiante()
        return self.__persona

    @_persona.setter
    def _persona(self, value):
        self.__persona = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._persona._id = self._lista._length + 1
        self._save(self._persona)
        
    
    def merge(self,pos):
        self._merge(self._persona, pos)