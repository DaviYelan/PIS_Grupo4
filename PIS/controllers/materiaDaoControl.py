from controllers.dao.daoAdapter import DaoAdapter
from models.materia import Materia

class MateriaDaoControl(DaoAdapter):
    def __init__(self, connection):
        super().__init__(Materia, connection)
        self.__materia = None

    @property
    def _materia(self):
        if self.__materia is None:
            self.__materia = Materia()
        return self.__materia

    @_materia.setter
    def _materia(self, value):
        self.__materia = value

    @property
    def _lista(self):
        return self._list()

    @property
    def save(self):
        self._save(self._materia)

    def merge(self, pos):
        self._merge(self._materia, pos)

    def delete(self, pos):
        self._delete(self._materia, pos)

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, nombre FROM materia")
        result = cursor.fetchall()
        cursor.close()
        return [{'id': row[0], 'nombre': row[1]} for row in result]