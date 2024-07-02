from models.cuenta import Cuenta
    
class ModelCuenta:
    @classmethod
    def login(cls, db, cuenta):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, correo, clave, role FROM cuenta WHERE correo = '{}'".format(cuenta.correo)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row:
                is_valid_password = Cuenta.check_password(row[2], cuenta.clave)
                if is_valid_password:
                    return Cuenta(row[0], row[1], is_valid_password, row[3])
                else:
                    return None
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(cls, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, correo, role FROM cuenta WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row:
                return Cuenta(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
