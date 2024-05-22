from controls.exception.duplicateEntryException import DuplicateEntryException
from controls.exception.notFoundException import NotFoundException
from controls.tda.rubricaDaoControl import RubricaDaoControl
from models.rubrica import Rubrica

class RubricaControl:
    def __init__(self):
        self.dao = RubricaDaoControl()

    def create_rubrica(self, ID, componente, instrumentoEvaluacion, ponderacion):
        try:
            rubrica = Rubrica(ID, componente, instrumentoEvaluacion, ponderacion)
            self.dao.create(rubrica)
        except DuplicateEntryException as e:
            print(e)

    def read_rubrica(self, ID):
        try:
            return self.dao.read(ID)
        except NotFoundException as e:
            print(e)

    def update_rubrica(self, ID, componente=None, instrumentoEvaluacion=None, ponderacion=None):
        try:
            return self.dao.update(ID, componente=componente, instrumentoEvaluacion=instrumentoEvaluacion, ponderacion=ponderacion)
        except NotFoundException as e:
            print(e)

    def delete_rubrica(self, ID):
        try:
            return self.dao.delete(ID)
        except NotFoundException as e:
            print(e)