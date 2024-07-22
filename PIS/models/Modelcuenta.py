from werkzeug.security import check_password_hash
from flask_login import UserMixin #type: ignore
import cx_Oracle #type: ignore

class Cuenta(UserMixin):
    def __init__(self, id, correo, clave, rol=None):
        self.id = id
        self.correo = correo
        self.clave = clave
        self.rol = rol

    @classmethod
    def check_password(cls, hashed_password, clave):
        return check_password_hash(hashed_password, clave)

class ModelCuenta:
    @classmethod
    def login(cls, db, cuenta):
        try:
            cursor = db.cursor()
            sql = "SELECT IDCUENTA, CORREO, CLAVE, ROL FROM cuenta WHERE CORREO = :correo"
            cursor.execute(sql, correo=cuenta.correo)
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
            cursor = db.cursor()
            sql = "SELECT IDCUENTA, CORREO, ROL FROM cuenta WHERE IDCUENTA = :id"
            cursor.execute(sql, id=id)
            row = cursor.fetchone()
            if row:
                return Cuenta(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

