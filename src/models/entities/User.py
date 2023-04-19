from flask_login import UserMixin



class User(UserMixin):

    def __init__(self, id, email, password, tipo, username="") -> None:
        self.id = id
        self.email = email
        self.password = password
        self.tipo = tipo
        self.username = username

