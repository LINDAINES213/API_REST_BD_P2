from database.db import get_connection
from .entities.Medicos import Medicos

class MedicosModel():

    @classmethod
    def get_medicos(self):
        try:
            connection=get_connection()
            medicos=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_medico, dpi, nombre, telefono, direccion, num_colegiado, especialidades, hospital, fecha_contratacion, correo, contrasena FROM medicos ORDER BY id_medico DESC")
                resultset=cursor.fetchall()
                
                for row in resultset:
                    medicos=Medicos(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    medicos.append(medicos.to_JSON())

            connection.close()
            return medicos
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_medicos(self, id_medico):
        try:
            
            connection=get_connection()
            medicos=[]

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_medico, dpi, nombre, telefono, direccion, num_colegiado, especialidades, hospital, fecha_contratacion, correo, contrasena FROM medicos
                                WHERE id_medico = %s""", (id_medico,))
                row=cursor.fetchone()
                
                medicos = None

                if row != None:
                    medicos=Medicos(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    medicos = medicos.to_JSON()

            connection.close()
            return medicos
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_medicos(self, medicos):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO medicos (id_medico, dpi, nombre, telefono, direccion, num_colegiado, especialidades, hospital, fecha_contratacion, correo, contrasena)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (medicos.id_medico, medicos.dpi, medicos.nombre, medicos.telefono, medicos.direccion, medicos.num_colegiado, medicos.especialidades, medicos.hospital, medicos.fecha_contratacion, medicos.correo, medicos.contrasena))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows             
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def update_medicos(self, medicos):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE medicos SET id_medico = %s, dpi = %s, nombre = %s, telefono = %s, direccion = %s, num_colegiado = %s, especialidades = %s, hospital = %s, fecha_contratacion = %s, correo = %s, contrasena = %s
                                WHERE id_medico = %s""", (medicos.id_medico, medicos.dpi, medicos.nombre, medicos.telefono, medicos.direccion, medicos.num_colegiado, medicos.especialidades, medicos.hospital, medicos.fecha_contratacion, medicos.correo, medicos.contrasena))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows             
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_medicos(self, medicos):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM medicos WHERE id_medico = %s", (medicos.id_medico,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows             
        except Exception as ex:
            raise Exception(ex)