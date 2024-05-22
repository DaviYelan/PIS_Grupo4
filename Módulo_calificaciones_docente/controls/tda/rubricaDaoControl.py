from controls.exception.duplicateEntryException import DuplicateEntryException
from controls.exception.notFoundException import NotFoundException

class RubricaDaoControl:
    def __init__(self):
        self.data = []

    def create(self, rubrica):
        if self.read(rubrica.ID) is not None:
            raise DuplicateEntryException(f"Rubrica with ID {rubrica.ID} already exists")
        self.data.append(rubrica)

    def read(self, ID):
        for rubrica in self.data:
            if rubrica.ID == ID:
                return rubrica
        return None

    def update(self, ID, **kwargs):
        rubrica = self.read(ID)
        if rubrica is None:
            raise NotFoundException(f"Rubrica with ID {ID} not found")
        for key, value in kwargs.items():
            if hasattr(rubrica, key):
                setattr(rubrica, key, value)
        return True

    def delete(self, ID):
        rubrica = self.read(ID)
        if rubrica is None:
            raise NotFoundException(f"Rubrica with ID {ID} not found")
        self.data.remove(rubrica)
        return True