from control.dao.daoAdapter import DaoAdapter
from model.docente import Docente
import json

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

#class personaDaoCOntrol(DaoAdapter, metaclass=Singleton):
class docenteDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Docente)
        self.__docente = None

    @property
    def _docente(self):
        if self.__docente == None:
            self.__docente = Docente()
        return self.__docente

    @ _docente.setter
    def _docente(self, value):
        self.__docente = value

    @property
    def _lista(self):
        return self._list
    
    
    @property
    def save(self):
        self._docente._id = self.lista._length + 1
        self._save(self._docente)
    
    def merge(self, pos):
        self._merge(self._docente, pos)
    
    def delete(self, pos):
        self._delete(self._docente, pos)


    def load_docente(self):
            with open('data/docente.json', 'r') as f:
                data = json.load(f)
            for docente_data in data:
                docente = Docente()  
                docente._nombre = docente_data['nombre']
                docente._apellido = docente_data['apellido']
                docente._direccion = docente_data['direccion']
                docente._fechaNacimiento = docente_data['fechaNacimiento']
                docente._genero = docente_data['genero']
                docente._telefono = docente_data['telefono']
                docente._tipoIdentificacion = docente_data['tipoIdentificacion']
                docente._cedula = docente_data['cedula']
                
                self.lista.__addLast__(docente)

