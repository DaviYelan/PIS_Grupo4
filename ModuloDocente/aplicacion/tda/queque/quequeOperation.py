from controls.tda.linked.linkedList import Linked_List
from controls.exception.linkedEmpty import LinkedEmpty
class QuequeOperation(Linked_List):
    def __init__(self, tope):
        super().__init__()
        self.__tope = tope

    @property
    def _tope(self):
        return self.__tope

    @_tope.setter
    def _tope(self, value):
        self.__tope = value

    @property
    def verifyTop(self):
        print(self._lenght)
        return self._lenght < self.__tope
    
    def queque(self, data):
        if self.verifyTop:
            self.add(data, self._lenght)
        else:
            raise LinkedEmpty("Queque full")
    
    @property
    def dequeque(self):
        if self.isEmpty:
            raise LinkedEmpty("Queque empty")
        else:
            return self.delete(0)
        
    