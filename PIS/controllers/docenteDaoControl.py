from controllers.dao.daoAdapter import DaoAdapter
from models.docente import Docente

class DocenteDaoControl(DaoAdapter):
    def __init__(self, connection):
        super().__init__(Docente, connection)
        self.__docente = None

    @property
    def _docente(self):
        if self.__docente is None:
            self.__docente = Docente()
        return self.__docente

    @_docente.setter
    def _docente(self, value):
        self.__docente = value

    @property
    def _lista(self):
        docentes = self._list()
        for docente in docentes:
            print(f"Docente: {docente._id}, {docente._nombre} {docente._apellido}")
        return docentes
    @property
    def save(self):
        self._save(self._docente)
    
    def merge(self, pos):
        self._merge(self._docente, pos)
    
    def delete(self, pos):
        self._delete(self._docente, pos)
