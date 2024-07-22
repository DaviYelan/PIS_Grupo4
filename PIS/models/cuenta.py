from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin #type: ignore

class Cuenta(UserMixin):
    def __init__(self, id, correo, clave, role=None):
        self.id = id
        self.correo = correo
        self.clave = clave
        self.role = role

    @classmethod
    def check_password(cls, hashed_password, clave):
        return check_password_hash(hashed_password, clave)
    
    #print(generate_password_hash("1234"))