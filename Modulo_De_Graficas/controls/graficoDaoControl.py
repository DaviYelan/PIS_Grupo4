from controls.dao.daoAdapter import DaoAdapter
from models.grafico import Grafico

class GraficoDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Grafico)
        self.__grafico = None

    @property
    def _grafico(self):
        if self.__grafico == None:
            self.__grafico = Grafico()   
        return self.__grafico

    @_grafico.setter
    def _grafico(self, value):
        self.__grafico = value

    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._grafico._id = self._lista + 1
        self._save(self._grafico)
    
    def merge(self, pos):
        self._merge(self._grafico, pos)