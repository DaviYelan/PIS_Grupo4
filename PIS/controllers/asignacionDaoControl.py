from controllers.dao.daoAdapter import DaoAdapter
from models.asignacion import Asignacion

class AsignacionDaoControl(DaoAdapter):
    def __init__(self, connection):
        super().__init__(Asignacion, connection)
        self.__asignacion = None

    @property
    def _asignacion(self):
        if self.__asignacion is None:
            self.__asignacion = Asignacion()
        return self.__asignacion

    @_asignacion.setter
    def _asignacion(self, value):
        self.__asignacion = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._save(self._asignacion)
    
    def merge(self, pos):
        self._merge(self._asignacion, pos)
    
    def delete(self, pos):
        self._delete(self._asignacion, pos)

    def save_asignacion(self, docente_id, materia_id):
        # Verificar que los IDs no sean nulos o vacíos
        if not docente_id or not materia_id:
            raise ValueError("Docente ID y Materia ID son necesarios.")
        
        query = """
            INSERT INTO ASIGNACION (DOCENTE_ID, MATERIA_ID)
            VALUES (:docente_id, :materia_id)
        """
        params = {'docente_id': docente_id, 'materia_id': materia_id}
        
        try:
            self.connection.execute(query, params)
            self.connection.connection.commit()  # Confirmar la transacción
            print("Asignación guardada exitosamente.")
        except Exception as e:
            print(f"Error al guardar asignación: {e}")
            self.connection.connection.rollback()
