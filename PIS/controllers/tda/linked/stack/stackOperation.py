from controller.tda.linked.linkedList import Linked_List
from controller.exception.linkedEmpty import LinkedEmpty

class StackOperation(Linked_List):
    def __init__(self, tope):
        super().__init__()
        self.__tope= tope

    @property
    def _tope(self):
        return self.__tope

    @_tope.setter
    def _tope(self, value):
        self.__tope = value
