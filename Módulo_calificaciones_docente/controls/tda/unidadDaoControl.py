from controls.exception.duplicateEntryException import DuplicateEntryException
from controls.exception.notFoundException import NotFoundException

class UnidadDaoControl:
    def __init__(self):
        self.data = []

    def create(self, unidad):
        if self.read(unidad.ID) is not None:
            raise DuplicateEntryException(f"Unidad with ID {unidad.ID} already exists")
        self.data.append(unidad)

    def read(self, ID):
        for unidad in self.data:
            if unidad.ID == ID:
                return unidad
        return None

    def update(self, ID, **kwargs):
        unidad = self.read(ID)
        if unidad is None:
            raise NotFoundException(f"Unidad with ID {ID} not found")
        for key, value in kwargs.items():
            if hasattr(unidad, key):
                setattr(unidad, key, value)
        return True

    def delete(self, ID):
        unidad = self.read(ID)
        if unidad is None:
            raise NotFoundException(f"Unidad with ID {ID} not found")
        self.data.remove(unidad)
        return True
