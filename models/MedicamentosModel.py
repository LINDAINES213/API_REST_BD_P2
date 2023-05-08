from database.db import get_connection
from .entities.Medicamentos import Medicamentos

class MedicamentosModel():

    @classmethod
    def get_medicamentos(self, connection, mes):
        try:
            connection=get_connection()
            medicamentos=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM medicamentos WHERE fecha_vencimiento LIKE '{}%'".format(mes))
                rows=cursor.fetchone()
                
                if rows != None:
                    usuario = Medicamentos(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6])
                    return usuario
                else:
                    return None
            connection.close()
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_medicamentos(self, id):
        try:
            
            connection=get_connection()
            medicamentos=[]

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id, nombre, cantidad_actual, cantidad_necesaria, necesita_compra, hospital FROM medicamentos
                                WHERE id = %s""", (id,))
                row=cursor.fetchone()
                
                medicamentos = None

                if row != None:
                    medicamentos=Medicamentos(row[0], row[1], row[2], row[3], row[4])
                    medicamentos = medicamentos.to_JSON()

            connection.close()
            return medicamentos
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_medicamentos(self, medicamentos):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO (id, nombre, cantidad_actual, cantidad_necesaria, necesita_compra, hospital)
                                VALUES (%s, %s, %s, %s, %s, %s)""", (medicamentos.id, medicamentos.nombre, medicamentos.cantidad_actual, medicamentos.cantidad_necesaria, medicamentos.necesita_compra, medicamentos.hospital))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows             
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def update_medicamentos(self, medicamentos):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE medicamentos SET id = %s, nombre = %s, cantidad_actual = %s, cantidad_necesaria = %s, necesita_compra = %s, hospital = %s
                                WHERE id = %s""", (medicamentos.id, medicamentos.nombre, medicamentos.cantidad_actual, medicamentos.cantidad_necesaria, medicamentos.necesita_compra, medicamentos.hospital))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows             
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_medicamentos(self, medicamentos):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM medicamentos WHERE id = %s", (medicamentos.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows             
        except Exception as ex:
            raise Exception(ex)