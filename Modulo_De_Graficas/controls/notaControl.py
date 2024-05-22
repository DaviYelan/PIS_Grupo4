from controls.tda.linked.linkedList import Linked_List
from models.nota import Nota

class NotaControl:
    def __init__(self):
        self.__nota = None
        self.__id_counter = 0
        self.__lista = Linked_List()
        
    @property
    def _nota(self):
        if self.__nota == None:
            self.__nota = Nota()
        return self.__nota

    @_nota.setter
    def _nota(self, value):
        self.__nota = value
        
    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value 
    
    def save(self):
        self._nota._id = self.__id_counter
        self._lista.add(self._nota, self._lista._lenght)
        
    def eliminar(self, pos):
        self._lista.delete(pos)

    def modificar(self, pos, tiempo):
        self._lista.edit(pos, tiempo)