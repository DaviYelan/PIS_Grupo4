from typing import Type
from controller.dao.daoAdapter import DaoAdapter
from models.malla import Malla
class mallaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Malla)
        self.__malla = None
    

    @property
    def _malla(self):
        if self.__malla is None:
            self.__malla = Malla()
        return self.__malla

    @_malla.setter
    def _malla(self, value):
        self.__malla = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._malla._id = self._lista._lenght + 1
        self._save(self._malla)
    
    def merge(self, pos):
        self._merge(self._malla, pos)
    
    def delete(self, pos):
        self._delete(self._malla, pos)