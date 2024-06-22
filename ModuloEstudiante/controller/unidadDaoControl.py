from typing import Type
from controller.dao.daoAdapter import DaoAdapter
from models.unidad import Unidad

class unidadDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Unidad)
        self.__unidad = None

    @property
    def _unidad(self):
        if self.__unidad is None:
            self.__unidad = Unidad()
        return self.__unidad

    @_unidad.setter
    def _unidad(self, value):
        self.__unidad = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._unidad._id = self._lista._lenght + 1
        self._save(self._unidad)
    
    def merge(self, pos):
        self._merge(self._unidad, pos)
    
    def delete(self, pos):
        self._delete(self._unidad, pos)