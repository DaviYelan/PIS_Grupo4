from controls.tda.linked.linkedList import Linked_List
from models.grafico import Grafico

class GraficoControl:
    def __init__(self):
        self.__grafico = None
        self.__id_counter = 0
        self.__lista = Linked_List()
        
    @property
    def _grafico(self):
        if self.__grafico == None:
            self.__grafico = Grafico()
        return self.__grafico

    @_grafico.setter
    def _grafico(self, value):
        self.__grafico = value
        
    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value 
    
    def save(self):
        self._grafico._id = self.__id_counter
        self._lista.add(self._grafico, self._lista._lenght)
        
    def eliminar(self, pos):
        self._lista.delete(pos)

    def modificar(self, pos, tiempo):
        self._lista.edit(pos, tiempo)