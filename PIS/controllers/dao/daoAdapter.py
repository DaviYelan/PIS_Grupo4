from typing import List, TypeVar, Generic, Type
from controllers.connecction.connection import Connection

T = TypeVar('T')

class DaoAdapter(Generic[T]):
    atype: Type[T]

    def __init__(self, atype: Type[T], connection: Connection):
        self.atype = atype
        self.connection = connection
        self.table_name = atype.__name__.upper()

    def _list(self):
        query = f"SELECT * FROM {self.table_name}"
        cursor = self.connection.execute(query)
        results = cursor.fetchall()
        print(f"Results: {results}")  
        print(f"Cursor Description: {cursor.description}") 
        objects_list = []
        column_names = [description[0] for description in cursor.description]
        for row in results:
            data_dict = dict(zip(column_names, row))
            print(f"Data Dict: {data_dict}") 
            obj = self.atype.deserializar(data_dict)
            objects_list.append(obj)
        return objects_list

    def _get(self, id):
        query = f"SELECT * FROM {self.table_name} WHERE ID = :id"
        cursor = self.connection.execute(query, {'id': id})
        row = cursor.fetchone()
        if row:
            data_dict = {description[0]: value for description, value in zip(cursor.description, row)}
            return self.atype.deserializar(data_dict)
        return None
    
    def _save(self, data: T):
            columns = data.serializable.keys()
            placeholders = ', '.join([':' + col for col in columns])
            max_id_query = f"SELECT MAX(ID) FROM {self.table_name}"
            cursor = self.connection.execute(max_id_query)
            max_id = cursor.fetchone()[0]
            next_id = (max_id or 0) + 1
            query = f"INSERT INTO {self.table_name} (ID, {', '.join(columns)}) VALUES (:id, {placeholders})"
            params = data.serializable
            params['id'] = next_id
            self.connection.execute(query, params)
            self.connection.connection.commit()

    def _merge(self, data, id):
        columns = data.serializable.keys()
        set_clause = ', '.join([f"{col} = :{col}" for col in columns if col != 'id'])
        query = f"UPDATE {self.table_name} SET {set_clause} WHERE ID = :id"
        params = {**data.serializable, 'id': id}
        print(f"Query: {query}")
        print(f"Params: {params}")
        try:
            self.connection.execute(query, params)
            self.connection.connection.commit()
            print("Update successful")
        except Exception as e:
            print(f"Error al actualizar el registro: {e}")
            self.connection.connection.rollback()



    def _delete(self, id):
        query = f"DELETE FROM {self.table_name} WHERE ID = :id"
        try:
            self.connection.execute(query, {'id': id})
            self.connection.connection.commit()
        except Exception as e:
            print(f"Error al eliminar el registro con ID {id}: {e}")
            self.connection.connection.rollback()
