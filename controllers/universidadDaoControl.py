from typing import Type
from controllers.dao.daoAdapter import DaoAdapter
from models.universidad import Universidad

class universidadDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Universidad)
        self.__universidad = None

    @property
    def _universidad(self):
        if self.__universidad is None:
            self.__universidad = Universidad()
        return self.__universidad

    @_universidad.setter
    def _universidad(self, value):
        self.__universidad = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._universidad._id = self._lista._lenght + 1
        self._save(self._universidad)
    
    def merge(self, pos):
        self._merge(self._universidad, pos)
    
    def delete(self, pos):
        self._delete(self._universidad, pos)