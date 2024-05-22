from controls.exception.duplicateEntryException import DuplicateEntryException
from controls.exception.notFoundException import NotFoundException

class AsignacionDaoControl:
    def __init__(self):
        self.data = []

    def create(self, asignacion):
        if self.read(asignacion.ID) is not None:
            raise DuplicateEntryException(f"Asignacion with ID {asignacion.ID} already exists")
        self.data.append(asignacion)

    def read(self, ID):
        for asignacion in self.data:
            if asignacion.ID == ID:
                return asignacion
        return None

    def update(self, ID, **kwargs):
        asignacion = self.read(ID)
        if asignacion is None:
            raise NotFoundException(f"Asignacion with ID {ID} not found")
        for key, value in kwargs.items():
            if hasattr(asignacion, key):
                setattr(asignacion, key, value)
        return True

    def delete(self, ID):
        asignacion = self.read(ID)
        if asignacion is None:
            raise NotFoundException(f"Asignacion with ID {ID} not found")
        self.data.remove(asignacion)
        return True
