from control.dao.daoAdapter import DaoAdapter
from model.materia import Materia
import json

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

#class personaDaoCOntrol(DaoAdapter, metaclass=Singleton):
class materiaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Materia)
        self.__materia = None

    @property
    def _materia(self):
        if self.__materia == None:
            self.__materia = Materia()
        return self.__materia

    @ _materia.setter
    def _materia(self, value):
        self.__materia = value

    @property
    def _lista(self):
        return self._list
    
    
    @property
    def save(self):
        self._materia._id = self.lista._length + 1
        self._save(self._materia)
    
    def merge(self, pos):
        self._merge(self._materia, pos)
    
    def delete(self, pos):
        self._delete(self._materia, pos)

    
    def load_estudiante(self):
            with open('data/estudiante.json', 'r') as f:
                data = json.load(f)
            for materia_data in data:
                materia = Materia()  
                materia._nombre = materia_data['nombre']
                materia._codigo = materia_data['codigo']
                materia._horaSemanal = materia_data['horaSemanal']
                materia._nombCiclo = materia_data['nombCiclo']
                
                
                self.lista.__addLast__(materia)
