from controller.tda.queque.quequeOperation import QuequeOperation
class Queque():
    def __init__(self, top):
            print(top)
            self.__queque = QuequeOperation(top)

    def queque (self, data):
        self.__queque.queque(data)

    def dequeque(self):
        return self.__queque.dequeque
    
    def print(self):
        self.__queque.print
    
    def verify(self):
        return self.__queque.verifyTop