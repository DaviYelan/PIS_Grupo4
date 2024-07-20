from controllers.dao.daoAdapter import DaoAdapter
from models.alumno import Alumno
class AlumnoDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Alumno)
        self.__alumno = None

    @property
    def _alumno(self):
        if self.__alumno == None:
            self.__alumno = Alumno()
        return self.__alumno

    @ _alumno.setter
    def _alumno(self, value):
        self.__alumno = value

    @property
    def _lista(self):
        return self._list
    
    @property
    def save(self):
        self._save(self._alumno)
    
    def merge(self, pos):
        self._merge(self._alumno, pos)
    
    def delete(self, pos):
        self._delete(self._alumno, pos)




