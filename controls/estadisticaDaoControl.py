from controls.dao.daoAdapter import DaoAdapter
from models.estadistica import Estadistica

class EstadisticaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Estadistica)
        self.__estadistica = None

    @property
    def _estadistica(self):
        if self.__estadistica == None:
            self.__estadistica = Estadistica()   
        return self.__estadistica

    @_estadistica.setter
    def _estadistica(self, value):
        self.__estadistica = value

    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._estadistica._id = self._lista + 1
        self._save(self._estadistica)
    
    def merge(self, pos):
        self._merge(self._estadistica, pos)