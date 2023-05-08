from database.db import get_connection
from .entities.Traslados import Traslados

class TrasladosModel():

    @classmethod
    def get_traslados(self):
        try:
            connection=get_connection()
            traslados=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_traslados, id_medico, hospital_anterior, hospital_nuevo, fecha_traslado FROM bitacora ORDER BY id_traslados")
                resultset=cursor.fetchall()
                
                for row in resultset:
                    traslados=Traslados(row[0], row[1], row[2], row[3], row[4])
                    traslados.append(traslados.to_JSON())

            connection.close()
            return traslados
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_traslados(self, id_traslados):
        try:
            
            connection=get_connection()
            traslados=[]

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_traslados, id_medico, hospital_anterior, hospital_nuevo, fecha_traslado FROM bitacora
                                WHERE id_traslados = %s""", (id_traslados,))
                row=cursor.fetchone()
                
                traslados = None

                if row != None:
                    traslados = Traslados(row[0], row[1], row[2], row[3], row[4])
                    traslados = traslados.to_JSON()

            connection.close()
            return traslados
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_traslados(self, traslados):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO (id_traslados, id_medico, hospital_anterior, hospital_nuevo, fecha_traslado)
                                VALUES (%s, %s, %s, %s, %s)""", (traslados.id_traslados, traslados.id_medico, traslados.hospital_anterior, traslados.hospital_nuevo, traslados.fecha_traslado))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows             
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def update_traslados(self, traslados):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE traslados SET id_traslados = %s, id_medico = %s, hospital_anterior = %s, hospital_nuevo = %s, fecha_traslado = %s,
                                """, (traslados.id_traslados, traslados.id_medico, traslados.hospital_anterior, traslados.hospital_nuevo, traslados.fecha_traslado))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows             
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_traslados(self, traslados):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM traslados WHERE id_traslados = %s", (traslados.id_traslados,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows             
        except Exception as ex:
            raise Exception(ex)