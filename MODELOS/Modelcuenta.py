from .entities.cuenta import Cuenta

class ModelCuenta:
    
    @classmethod
    def login(self, db, cuenta):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, correo, clave FROM cuenta WHERE correo = '{}'""".format(cuenta.correo)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                cuenta = Cuenta(row[0], row[1], Cuenta.check_password(row[2], cuenta.clave))
                return cuenta  
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, correo FROM cuenta WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
               return Cuenta(row[0], row[1], None)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        