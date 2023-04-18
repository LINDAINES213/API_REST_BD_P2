from .entities.User import User
from database.db import get_connection

class ModelUser():

    @classmethod
    def login(self, connection, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, email, password, username FROM usuario WHERE email = '{}' AND password = '{}'".format(usuario.email, usuario.password))
                row = cursor.fetchone()

                if row != None:
                    usuario = User(row[0], row[1], row[2], row[3])
                    return usuario
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_by_id(self, connection, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, email, username FROM usuario WHERE id = '{}'".format(id))
                row = cursor.fetchone()
            
                if row != None:
                    return User(row[0], row[1], None, row[2])
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)        