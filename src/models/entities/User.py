from flask_login import UserMixin
from werkzeug.security import check_password_hash

class User():

    def __init__(self, email, nombre=None, apellido=None, contrasena=None) -> None:
        self.email = email
        self.nombre = nombre
        self.apellido = apellido
        self.contrasena = contrasena

    def is_authenticated(self):
        return True

    def check_password(self, contrasena):
        return check_password_hash(self.contrasena, contrasena)
    
    def to_JSON(self):
        return{
            'email': self.email,
            'nombre': self.nombre, 
            'apellido': self.apellido,
            'contrasena': self.contrasena
        }


