from control.dao.daoAdapter import DaoAdapter
from model.mallaCarrera import MallaCarrera
import json

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

#class personaDaoCOntrol(DaoAdapter, metaclass=Singleton):
class mallaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(MallaCarrera)
        self.__malla = None

    @property
    def _malla(self):
        if self.__malla == None:
            self.__malla = MallaCarrera()
        return self.__malla

    @ _malla.setter
    def _malla(self, value):
        self.__malla = value

    @property
    def _lista(self):
        return self._list
    
    
    @property
    def save(self):
        self._malla._id = self.lista._length + 1
        self._save(self._malla)
    
    def merge(self, pos):
        self._merge(self._malla, pos)
    
    def delete(self, pos):
        self._delete(self._malla, pos)

    
    def load_malla(self):
            with open('data/malla.json', 'r') as f:
                data = json.load(f)
            for malla_data in data:
                malla = MallaCarrera()  
                malla._nombre = malla_data['nombre']
                
                self.lista.__addLast__(malla)
