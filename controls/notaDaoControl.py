from controls.dao.daoAdapter import DaoAdapter
from models.nota import Nota

class NotaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Nota)
        self.__nota = None

    @property
    def _nota(self):
        if self.__nota == None:
            self.__nota = Nota()   
        return self.__nota

    @_nota.setter
    def _nota(self, value):
        self.__nota = value

    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._nota._id = self._lista + 1
        self._save(self._nota)
    
    def merge(self, pos):
        self._merge(self._nota, pos)