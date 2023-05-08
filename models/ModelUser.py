from .entities.User import User
from database.db import get_connection

class ModelUser():

    @classmethod
    def login(self, connection, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, email, password, tipo, username FROM usuario WHERE email = '{}' AND password = '{}' AND tipo = '{}'".format(usuario.email, usuario.password, usuario.tipo))
                row = cursor.fetchone()

                if row != None:
                    usuario = User(row[0], row[1], row[2], row[3], row[4])
                    return usuario
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def signin(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO usuario (email, password, tipo, username)
                                VALUES (%s, %s, %s, %s)""", (usuario.email, usuario.password, usuario.tipo, usuario.username))
                affected_rows = cursor.rowcount
                connection.commit()

            

            connection.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, connection, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, email, tipo, username FROM usuario WHERE id = '{}'".format(id))
                row = cursor.fetchone()
            
                if row != None:
                    return User(row[0], row[1], row[2], None, row[3])
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)        