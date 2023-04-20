from database.db import get_connection
from .entities.Bitacora import Bitacora

class BitacoraModel():

    @classmethod
    def get_bitacora(self):
        try:
            connection=get_connection()
            bitacora=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, fechahora, accion, nombre_tabla FROM bitacora")
                resultset=cursor.fetchall()
                
                for row in resultset:
                    bitacora=Bitacora(row[0], row[1], row[2], row[3])
                    bitacora.append(bitacora.to_JSON())

            connection.close()
            return bitacora
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_bitacora(self, id):
        try:
            
            connection=get_connection()
            bitacora=[]

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id, fechahora, accion, nombre_tabla FROM bitacora
                                WHERE id = %s""", (id,))
                row=cursor.fetchone()
                
                bitacora = None

                if row != None:
                    bitacora=Bitacora(row[0], row[1], row[2], row[3])
                    bitacora = bitacora.to_JSON()

            connection.close()
            return bitacora
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_bitacora(self, bitacora):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO (id, fechahora, accion, nombre_tabla)
                                VALUES (%s, %s, %s, %s)""", (bitacora.id, bitacora.fechahora, bitacora.accion, bitacora.nombre_tabla))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows             
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def update_bitacora(self, bitacora):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE bitacora SET id = %s, fechahora = %s, accion = %s, nombre_tabla = %s
                                """, (bitacora.id, bitacora.fechahora, bitacora.accion, bitacora.nombre_tabla))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows             
        except Exception as ex:
            raise Exception(ex)
