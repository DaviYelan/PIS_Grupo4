from typing import Type
from controllers.dao.daoAdapter import DaoAdapter
from models.facultad import Facultad

class FacultadDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Facultad)
        self.__facultad = None

    @property
    def _facultad(self):
        if self.__facultad is None:
            self.__facultad = Facultad()
        return self.__facultad

    @_facultad.setter
    def _facultad(self, value):
        self.__facultad = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._save(self._facultad)
    
    def merge(self, pos):
        self._merge(self._facultad, pos)
    
    def delete(self, pos):
        self._delete(self._facultad, pos)