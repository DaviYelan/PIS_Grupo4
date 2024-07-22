from controllers.tda.linked.node import Node
from controllers.exception.lindekEmpty import LinkedEmpty
from controllers.exception.arrayPositionException import ArrayPositionException
from numbers import Number
from controllers.tda.linked.busqueda.burbuja import Burbuja
from controllers.tda.linked.busqueda.insercion import Insercion
from controllers.tda.linked.busqueda.quicksort import QuickSort
from controllers.tda.linked.busqueda.mergesort import MergeSort
from controllers.tda.linked.busqueda.shellsort import ShellSort

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
        return self.__head == None or self._length == 0
    
    def _getFirst_(self, poss):
        if not self.isEmpty:
            return self.__head
        else:
            return "List is Empty"
    
    def _getLast_(self, poss):
        if not self.isEmpty:
            return self.__last
        else:
            return "List is Empty"
        
    def getNode(self, poss):
        if self.isEmpty:
           raise LinkedEmpty("List is Empty")
        elif poss < 0 or poss >= self.__length:
            raise ArrayPositionException("Index out of range")
        elif poss == 0:
            return self.__head._data
        elif poss == (self.__length - 1):
            return self.__last._data
        else:
            node = self.__head
            cont = 0
            while cont < poss:
                cont += 1
                node = node._next
            return node._data
        

    def get(self, poss):
        if self.isEmpty:
           raise LinkedEmpty("List is Empty")
        elif poss < 0 or poss >= self.__length:
            raise ArrayPositionException("Index out of range")
        elif poss == 0:
            return self.__head
        elif poss == (self.__length - 1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < poss:
                cont += 1
                node = node._next
            return node
            
        
    
    def addFirst(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node
            self.__last = node
            self.__length += 1
        else:
            headOld = self.__head #guarada toda la lista hara ahora
            node = Node(data, headOld)  
            self.__head = node
            self.__length += 1

    def addLast(self, data):
        if self.isEmpty:
            self.addFirst(data)
        else:
            node = Node(data)
            self.__last._next = node 
            self.__last = node
            self.__length += 1

    
    def addNode(self, data, poss = 0):
        if poss == 0:
            self.addFirst(data)
        elif poss == self.__length:
            self.addLast(data)
        else:
            node_preview = self.get(poss - 1)
            node_actuality = node_preview._next
            node = Node(data, node_actuality)
            node_preview._next = node
            self.__length += 1
    
    def add(self, data, pos = 0):
        if pos == 0:
            self.addFirst(data)
        elif pos == self.__length:
            self.addLast(data)
        else:
            node_preview = self.get(pos - 1)
            node_last = node_preview._next #self.getNode(pos)
            node = Node(data, node_last)
            node_preview._next = node
            self.length += 1


    def edit (self, data, poss = 0):
        if poss == 0:
            self.__head._data = data
        elif poss == (self.__length - 1):
            self.__last._data = data
        else:
            node = self.get(poss)
            node._data = data


    # @property
    # def toArray (self):
    #     array = TDAArray(self.__length)
    #     if not self.isEmpty:
    #         node = self.__head
    #         cont = 0
    #         while cont < self.__length:
    #             array.insert(node._data, cont) #array[cont] = node._data
    #             cont += 1
    #             node = node._next
    #     return array
    
    
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
            self.addLast(array[i])
            
            
    def sort(self, type = 1):
        if self.isEmpty:
            raise LinkedEmpty("List is Empty")
        else:  
            array = self.toArray
            #datos primitivos
            if isinstance(array[0], Number) or isinstance(array[0], str):
                #order = Burbuja()
                order = Insercion()
                if type == 1:
                    #array = order.sort_burbuja_number_ascent(array)
                    array = order.sort_primitive_ascent(array)
                else:
                    #array = order.sort_burbuja_number_descent(array)
                    array = order.sort_primitive_descent(array)
          
            self.toList(array)
            
    def  sort_models(self, atribute ,type = 1 ):
        if self.isEmpty:
            raise LinkedEmpty("List is Empty")
        else:  
            array = self.toArray
            if isinstance(array[0], object): 
                #order = Burbuja()
                order = Insercion()
                if type == 1:                  
                    #array = order.sort_burbuja_atribute_ascent(array, atribute)
                    array = order.sort_models_ascent(array, atribute)
                else:
                    #array = order.sort_burbuja_atribute_descent(array, atribute)
                    array = order.sort_models_descent(array, atribute)
            self.toList(array)
        return self
      
    def search_equals(self, data):
        list = Linked_List()
        if self.isEmpty:
            raise LinkedEmpty("List is Empty")
        else:  
            array = self.toArray
            for i in range(0, len(array)):
                if array[i].lower().__contains__(data.lower()):  # < > <= >= !=  == startswith() endswith()
                    list.addNode(array[i], list._length)
        return list  
   
        


    def dicToList(self, array_dict):
        for i in range(0, len(array_dict)):
            node = Node(array_dict[i])
            self.addLast(node)
            
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
            aux = self.get(self._length - 2)

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

    
    def delete(self, pos):
        pos = pos 
        if self.isEmpty:
            raise LinkedEmpty("List is Empty")
        elif pos < 0 or pos >= self._length:
            raise ArrayPositionException("Position is out of range")
        elif pos == 0:
            self.__head = self.__head._next
            self.__length -= 1
            
        elif pos == self._length -1:
            self.__last = self.getNode(pos-1)
            #restarId
            self.__length -= 1
        else:
            node_preview = self.getNode(pos-1)
            node_last = node_preview._next._next
            node_preview._next = node_last
            self.__length -= 1
        for i in range(pos, self._length):
            self.getNode(i)._data._id = i+1
   
    #serializable
    @property
    def serializable(self):
        array = self.toArray
        array_dict = []
        for i in range(0, len(array)):
            array_dict.append(array[i].__dict__)
        return array_dict
    
    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    def __str__(self) -> str: #metodo toString    #cometar ctrl+k+c   / ctrl+k+u
        out = ""
        if self.isEmpty:
            out = "List is Empty"
        else:
            node = self.__head
            while node != None:
                out += str(node._data) + " -> "
                node = node._next
        return out
    
    @property
    def print(self):
        node = self.__head
        data = ""
        while node != None :
            data += str(node._data) + "   "
            node = node._next
        print("Lista de datos")
        print(data)
        
    def sort(self, type = 1, method = 3):
        if self.isEmpty:
            raise LinkedEmpty("List is Empty")
        else:  
            array = self.toArray
            self.clear
            #datos primitivos
            if isinstance(array[0], Number) or isinstance(array[0], str):
                if type == 1:
                    if method == 1:
                        order = Burbuja()
                        array = order.sort_burbuja_number_ascent(array)
                    elif method == 2:
                        order = Insercion()
                        array = order.sort_primitive_ascent(array)
                    elif method == 3:
                        order = QuickSort()
                        array = order.quicksort_numbers_ascent(array, 0, len(array) - 1)
                    elif method == 4:
                        order = MergeSort()
                        array = order.mergeSort_number_ascent(array)
                    elif method == 5:
                        order = ShellSort()
                        array = order.shell_number_ascent(array)

                else:
                    if method == 1:
                        order = Burbuja()
                        array = order.sort_burbuja_number_descent(array)
                    elif method == 2:
                        order = Insercion()
                        array = order.sort_primitive_descent(array)
                    elif method == 3:
                        order = QuickSort()
                        array = order.quicksort_numbers_descent(array, 0, len(array) - 1)
                    elif method == 4:
                        order = MergeSort()
                        array = order.mergeSort_number_descent(array)
                    elif method == 5:
                        order = ShellSort()
                        array = order.shell_number_descent(array)
          
            self.toList(array)

            
    def  sort_models(self, atribute ,type = 1, method = 3):
        if self.isEmpty:
            raise LinkedEmpty("List is Empty")
        else:  
            array = self.toArray
            self.clear
            if isinstance(array[0], object): 
                if type == 1:
                    if method == 1:
                        order = Burbuja()
                        array = order.sort_burbuja_atribute_ascent(array, atribute)                  
                    elif method == 2:
                        order = Insercion()
                        array = order.sort_models_ascent(array, atribute)
                    elif method == 3:
                        order = QuickSort()
                        array = order.quicksort_models_ascent(array, 0, len(array) - 1, atribute)
                    elif method == 4:
                        order = MergeSort()
                        array = order.mergeSort_models_ascent(array, atribute)
                    elif method == 5:
                        order = ShellSort()
                        array = order.shell_models_ascent(array, atribute)
                else:
                    if method == 1:
                        order = Burbuja()
                        array = order.sort_burbuja_atribute_descent(array, atribute)
                    elif method == 2:
                        order = Insercion()
                        array = order.sort_models_descent(array, atribute)
                    elif method == 3:
                        order = QuickSort()
                        array = order.quicksort_models_descent(array, 0, len(array) - 1, atribute)
                    elif method == 4:
                        print("entro en merge descent")
                        order = MergeSort()
                        array = order.mergeSort_models_descent(array, atribute)
                    elif method == 5:
                        order = ShellSort()
                        array = order.shell_models_descent(array, atribute)
            self.toList(array)
       
      
    def search_equals(self, data):
        list = Linked_List()
        if self.isEmpty:
            raise LinkedEmpty("List is Empty")
        else:  
            array = self.toArray
            for i in range(0, len(array)):
                if array[i].lower().__contains__(data.lower()):  
                    list.addNode(array[i], list._length)
        return list  
    
    
    def binary_search_number(self, data):
        self.sort()
        arr = self.toArray
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == data:
                return arr[mid] 
            elif arr[mid] < data:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def lineal_binary_search_number(self, data):
        self.sort()
        arr = self.toArray
        left = 0
        right = len(arr) - 1
        list = Linked_List()
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == data:
                for i in range(left, len(arr)):
                    if arr[i] == data:
                        list.addNode(arr[i], list._length)
                break
            elif arr[mid] < data:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    
    #busqueda binaria
    def binary_search_models(self, data, attribute):
        self.sort_models(attribute)
        arr = self.toArray
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if str(getattr(arr[mid], attribute)).lower() == str(data).lower():
                return arr[mid]
            elif str(getattr(arr[mid], attribute)).lower() < str(data).lower():
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    
    #busqueda lineal-binaria
    def lineal_binary_search_models(self, data, atribute):       
        self.sort_models(atribute)
        arr = self.toArray
        left = 0
        right = len(arr) - 1
        list = Linked_List()
        
        
        while left <= right:
            mid = (left + right) // 2
            if str(getattr(arr[mid], atribute)).lower() == str(data).lower():  
                for i in range(left, len(arr)):
                    if str(getattr(arr[i], atribute)).lower() == str(data).lower():  
                        list.addNode(arr[i], list._length)         
                break                  
            elif str(getattr(arr[mid], atribute)).lower() < data.lower():
                left = mid + 1
            else:
                right = mid - 1
        return list
    
        

        