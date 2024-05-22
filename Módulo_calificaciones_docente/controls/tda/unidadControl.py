from controls.exception.duplicateEntryException import DuplicateEntryException
from controls.exception.notFoundException import NotFoundException
from controls.tda.unidadDaoControl import UnidadDaoControl
from models.unidad import Unidad

class UnidadControl:
    def __init__(self):
        self.dao = UnidadDaoControl()

    def create_unidad(self, ID, actividade, tema):
        try:
            unidad = Unidad(ID, actividade, tema)
            self.dao.create(unidad)
        except DuplicateEntryException as e:
            print(e)

    def read_unidad(self, ID):
        try:
            return self.dao.read(ID)
        except NotFoundException as e:
            print(e)

    def update_unidad(self, ID, actividade=None, tema=None):
        try:
            return self.dao.update(ID, actividade=actividade, tema=tema)
        except NotFoundException as e:
            print(e)

    def delete_unidad(self, ID):
        try:
            return self.dao.delete(ID)
        except NotFoundException as e:
            print(e)
