from database.db import get_connection
from .entities.User import User

class UserModel():
        
    @classmethod
    def add_user(self, usuario):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO usuario (email, nombre, apellido, contrasena)
                                VALUES (%s, %s, %s, %s)""", (usuario.email, usuario.nombre, usuario.apellido, usuario.contrasena))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows             
        except Exception as ex:
            raise Exception(ex)