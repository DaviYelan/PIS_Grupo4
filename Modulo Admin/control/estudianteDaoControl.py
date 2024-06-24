from control.dao.daoAdapter import DaoAdapter
from model.estudiante import Estudiante
import json

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

#class personaDaoCOntrol(DaoAdapter, metaclass=Singleton):
class estudianteDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Estudiante)
        self.__estudiante = None

    @property
    def _estudiante(self):
        if self.__estudiante == None:
            self.__estudiante = Estudiante()
        return self.__estudiante

    @ _estudiante.setter
    def _estudiante(self, value):
        self.__estudiante = value

    @property
    def _lista(self):
        return self._list
    
    
    @property
    def save(self):
        self._estudiante._id = self.lista._length + 1
        self._save(self._estudiante)
    
    def merge(self, pos):
        self._merge(self._estudiante, pos)
    
    def delete(self, pos):
        self._delete(self._estudiante, pos)

    
    def load_estudiante(self):
            with open('data/estudiante.json', 'r') as f:
                data = json.load(f)
            for estudiante_data in data:
                estudiante = Estudiante()  
                estudiante._nombre = estudiante_data['nombre']
                estudiante._apellido = estudiante_data['apellido']
                estudiante._direccion = estudiante_data['direccion']
                estudiante._fechaNacimiento = estudiante_data['fechaNacimiento']
                estudiante._genero = estudiante_data['genero']
                estudiante._telefono = estudiante_data['telefono']
                estudiante._tipoIdentificacion = estudiante_data['tipoIdentificacion']
                estudiante._cedula = estudiante_data['cedula']
                
                self.lista.__addLast__(estudiante)
