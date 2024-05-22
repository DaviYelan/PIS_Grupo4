from controls.tda.linked.linkedList import Linked_List
from models.estadistica import Estadistica

class EstadisticaControl:
    def __init__(self):
        self.__estadistica = None
        self.__id_counter = 0
        self.__lista = Linked_List()
        
    @property
    def _estadistica(self):
        if self.__estadistica == None:
            self.__estadistica = Estadistica()
        return self.__estadistica

    @_estadistica.setter
    def _estadistica(self, value):
        self.__estadistica = value
        
    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value 
    
    def save(self):
        self._estadistica._id = self.__id_counter
        self._lista.add(self._estadistica, self._lista._lenght)
        
    def eliminar(self, pos):
        self._lista.delete(pos)

    def modificar(self, pos, tiempo):
        self._lista.edit(pos, tiempo)
    