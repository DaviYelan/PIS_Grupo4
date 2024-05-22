from controls.exception.duplicateEntryException import DuplicateEntryException
from controls.exception.notFoundException import NotFoundException
from controls.tda.asignacionDaoControl import AsignacionDaoControl
from models.asignacion import Asignacion

class AsignacionControl:
    def __init__(self):
        self.dao = AsignacionDaoControl()

    def create_asignacion(self, ID, IdMateria, IdDocente):
        try:
            asignacion = Asignacion(ID, IdMateria, IdDocente)
            self.dao.create(asignacion)
        except DuplicateEntryException as e:
            print(e)

    def read_asignacion(self, ID):
        try:
            return self.dao.read(ID)
        except NotFoundException as e:
            print(e)

    def update_asignacion(self, ID, IdMateria=None, IdDocente=None):
        try:
            return self.dao.update(ID, IdMateria=IdMateria, IdDocente=IdDocente)
        except NotFoundException as e:
            print(e)

    def delete_asignacion(self, ID):
        try:
            return self.dao.delete(ID)
        except NotFoundException as e:
            print(e)