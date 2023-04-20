from database.db import get_connection
from .entities.Bitacora import Bitacora

class BitacoraModel():

    @classmethod
    def get_bitacora(self):
        try:
            connection=get_connection()
            bitacora=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT fechahora, accion, nombre_tabla FROM bitacora")
                resultset=cursor.fetchall()
                
                for row in resultset:
                    bitacora=Bitacora(row[0], row[1], row[2])
                    bitacora.append(bitacora.to_JSON())

            connection.close()
            return bitacora
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_bitacora(self, nombre_tabla):
        try:
            
            connection=get_connection()
            bitacora=[]

            with connection.cursor() as cursor:
                cursor.execute("""SELECT fechahora, accion, nombre_tabla FROM bitacora
                                WHERE nombre_tabla = %s""", (nombre_tabla,))
                row=cursor.fetchone()
                
                bitacora = None

                if row != None:
                    bitacora=Bitacora(row[0], row[1], row[2])
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
                cursor.execute("""INSERT INTO (fechahora, accion, nombre_tabla)
                                VALUES (%s, %s, %s)""", (bitacora.fechahora, bitacora.accion, bitacora.nombre_tabla))
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
                cursor.execute("""UPDATE bitacora SET fechahora = %s, accion = %s, nombre_tabla = %s
                                """, (bitacora.fechahora, bitacora.accion, bitacora.nombre_tabla))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows             
        except Exception as ex:
            raise Exception(ex)
