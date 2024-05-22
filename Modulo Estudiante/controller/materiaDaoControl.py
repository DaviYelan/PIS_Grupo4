from typing import Type
from controller.dao.daoAdapter import DaoAdapter
from models.materia import Materia

class MateriaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Materia)
        self.__materia = None
    

    @property
    def _materia(self):
        if self.__materia is None:
            self.__materia = Materia()
        return self.__materia

    @_materia.setter
    def _materia(self, value):
        self.__materia = value

    @property
    def _lista(self):
        return self._list()
    

    @property
    def save(self):
        self._materia._id = self._lista._lenght + 1
        self._save(self._materia)
    def merge(self, pos):
        self._merge(self._materia, pos)
    
    def delete(self, pos):
        self._delete(self._materia, pos)