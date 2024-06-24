from controls.tda.linked.binarySearch import BinarySearch
from controls.tda.linked.linearSearch import LinearSearch
from controls.tda.linked.node import Node
from controls.exception.linkedEmpty import LinkedEmpty
from controls.exception.arrayPositionException import ArrayPositionException
from numbers import Number
from controls.tda.linked.burbuja import Burbuja
from controls.tda.linked.insercion import Insercion
from controls.tda.linked.merge import Merge
from controls.tda.linked.quick import QuickSort
from controls.tda.linked.shell import ShellSort

class Linked_List(object):
    def __init__(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    @property
    def _length(self):
        return self.__length

    @_length.setter
    def _length(self, value):
        self.__length = value

    @property
    def isEmpty(self):
        return self.__head == None or self.__length == 0

    def __addFirst__(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node
            self.__last = node            
        else:
            headOld = self.__head
            node = Node(data, headOld)
            self.__head = node
        
        self.__length += 1

    def __addLast__(self, data):
        if self.isEmpty:
            self.__addFirst__(data)            
        else:            
            node = Node(data)
            self.__last._next = node
            self.__last = node        
            self.__length += 1

    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    def add(self, data, pos = 0):
        if pos == 0:
            self.__addFirst__(data)
        elif pos == self.__length:            
            self.__addLast__(data)
        else:            
            node_preview = self.getNode(pos-1)
            node_last = node_preview._next#self.getNode(pos) 
            node = Node(data, node_last)
            node_preview._next = node
            self.__length += 1
    
    def edit(self, data, pos = 0):
        if pos == 0:
            self.__head._data = data
        elif pos == self.__length:            
            self.__last._data = data
        else:                        
            node = self.getNode(pos)            
            node._data = data
            
    @property
    def toArray(self):
        #TODO
        pass
    
    def deleteFirst(self):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            element = self.__head._data
            aux = self.__head._next
            self.__head = aux
            if self.__length == 1:
                self.__last = None
            self._length = self._length - 1
            return element
        
    def deleteLast(self):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            element = self.__last._data
            aux = self.getNode(self._length - 2)

            #self.__head = aux
            if aux == None:
                self.__last = None
                if self.__length == 2:
                    self.__last = self.__head
                else:
                    self.__head = None
            else:
                self.__last = None
                self.__last = aux
                self.__last._next = None
            self._length = self._length - 1
            return element

    
    def delete(self, pos = 0):
        
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self.__length:
            raise ArrayPositionException("Position out range")
        elif pos == 0:
            return self.deleteFirst()
        elif pos == (self.__length - 1):
            return self.deleteLast()
        else:
            preview = self.getNode(pos - 1)
            actually = self.getNode(pos)
            element = preview._data
            next = actually._next
            actually = None
            preview._next = next
            self._length = self._length - 1
            return element

    """Obtiene el objeto nodo"""
    def getNode(self, pos):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._length:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            return self.__head
        elif pos == (self.__length - 1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node
        
    """Obtiene el objeto nodo"""
    def get(self, pos):
        try:
            return self.getNode(pos)._data
        except Exception as error:
            return None

    def __str__(self) -> str:
        out = ""
        if self.isEmpty:
            out = "List is Empty"
        else:
            node = self.__head
            while node != None:
                out += str(node._data)+ "\t"
                node = node._next
        return out
    @property
    def print(self):
        node = self.__head
        data = ""    
        while node != None:
            data += str(node._data)+"    "            
            node = node._next
        print("Lista de datos")
        print(data)

    #Pasar la lista a arreglo
    @property
    def toArray(self):
        array = []
        if not self.isEmpty:
            node = self.__head
            cont = 0
            while cont < self._length:
                array.append(node._data)
                cont += 1
                node = node._next

        return array
        
    def toList(self, array):
        self.clear
        for i in range(0, len(array)):
            self.__addLast__(array[i])

    def sort(self, type):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            #datos primitivos
            if isinstance(array[0], Number) or isinstance(array[0], str):
                #order = Burbuja()
                #order = Insercion()
                #order = QuickSort()
                #order = ShellSort()
                order = Merge()
                if type == 1:
                    #array = order.sort_burbuja_number_ascendent(array) #burbuja
                    #array = order.sort_primitive_ascendent(array) #insercion
                    #array = order.sort_primitive_ascendent(array) #quick
                    #array = order.sort_primitive_ascendent(array) #shell
                    array = order.sort_primitive_ascendent(array) #merge
                else:
                    #array = order.sort_burbuja_number_descendent(array) #burbuja
                    #array = order.sort_primitive_descendent(array) #insercion
                    #array = order.sort_primitive_descendent(array) #quick
                    #array = order.sort_primitive_descendent(array) #shell
                    array = order.sort_primitive_descendent(array) #merge
            
            self.toList(array)

    def sort_models(self, attribute, type = 1):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            if isinstance(array[0], object):
                #order = Burbuja()
                #order = Insercion()
                #order = QuickSort()
                #order = ShellSort()
                order = Merge()
                if type == 1:
                    #array = order.sort_burbuja_attribute_ascendent(array, attribute)
                    array = order.sort_merge_attribute_ascendent(array, attribute)
                else:
                    #array = order.sort_burbuja_attribute_descendent(array, attribute)
                    array = order.sort_merge_attribute_descendent(array, attribute)
                
                #cls = getattr(array[0], attribute)
                #print(cls)
            self.toList(array)
        return self

    def search_equals(self, data):
        list = Linked_List()
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            #print(array[i])
            for i in range(0, len(array)):
                #print(type(array[i]))
                if(array[i].lower().__contains__ (data.lower())):    #startswith
                    list.add(array[i], list._length)
        return list
    
    #Metodos de busqueda numeros
    def binary_search(self, query, attribute=None, starts_with=False):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            if attribute is not None:
                return BinarySearch.search(array, attribute, query, starts_with)
            else:
                return BinarySearch.search(array, None, query, starts_with)
    
    def linear_search(self, query, attribute=None, starts_with=False):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            if attribute is not None:
                return LinearSearch.search(array, attribute, query, starts_with)
            else:
                return LinearSearch.search(array, None, query, starts_with)