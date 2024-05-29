from typing import Type
from controller.dao.daoAdapter import DaoAdapter
from models.periodoAcademico import PeriodoAcademico

class PeriodoAcademicoDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(PeriodoAcademico)
        self.__periodoAcademico = None
    

    @property
    def _periodoAcademico(self):
        if self.__periodoAcademico is None:
            self.__periodoAcademico = PeriodoAcademico()
        return self.__periodoAcademico

    @_periodoAcademico.setter
    def _periodoAcademico(self, value):
        self.__periodoAcademico = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._periodoAcademico._id = self._lista._lenght + 1
        self._save(self._periodoAcademico)
    
    def merge(self, pos):
        self._merge(self._periodoAcademico, pos)
    
    def delete(self, pos):
        self._delete(self._periodoAcademico, pos)