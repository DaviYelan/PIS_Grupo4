from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class Cuenta(UserMixin):
    def __init__(self, id, correo, clave) -> None:
        self.id = id
        self.correo = correo
        self.clave = clave

    @classmethod
    def check_password(self, hashed_password, clave):
        return check_password_hash(hashed_password, clave)

    #print(generate_password_hash("grupocuatro"))
    #print(generate_password_hash("lore"))
    print(generate_password_hash("456"))