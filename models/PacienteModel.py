from database.db import get_connection
from .entities.Paciente import Paciente

class PacienteModel():

    @classmethod
    def get_pacientes(self):
        try:
            connection=get_connection()
            pacientes=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_paciente, dpi, nombre, telefono, direccion, imc, altura, peso, adiccion, enfermedades_hereditarias, tratamientos, medico_asignado, hospital_asignado, enfermedades, evolucion_enfermedad, fecha_ingreso, fecha_salida, correo, contrasena FROM pacientes ORDER BY id_paciente DESC")
                resultset=cursor.fetchall()
                
                for row in resultset:
                    paciente=Paciente(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18])
                    pacientes.append(paciente.to_JSON())

            connection.close()
            return pacientes
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_paciente(self, id_paciente):
        try:
            
            connection=get_connection()
            pacientes=[]

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_paciente, dpi, nombre, telefono, direccion, imc, altura, peso, adiccion, enfermedades_hereditarias, tratamientos, medico_asignado, hospital_asignado, enfermedades, evolucion_enfermedad, fecha_ingreso, fecha_salida, correo, contrasena FROM pacientes
                                WHERE id_paciente = %s""", (id_paciente,))
                row=cursor.fetchone()
                
                paciente = None

                if row != None:
                    paciente=Paciente(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18])
                    paciente = paciente.to_JSON()

            connection.close()
            return paciente
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_paciente(self, pacientes):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO pacientes (id_paciente, dpi, nombre, telefono, direccion, imc, altura, peso, adiccion, enfermedades_hereditarias, tratamientos, medico_asignado, hospital_asignado, enfermedades, evolucion_enfermedad, fecha_ingreso, fecha_salida, correo, contrasena)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (pacientes.id_paciente, pacientes.dpi, pacientes.nombre, pacientes.telefono, pacientes.direccion, pacientes.imc, pacientes.altura, pacientes.peso, pacientes.adiccion, pacientes.enfermedades_hereditarias, pacientes.tratamientos, pacientes.medico_asignado, pacientes.hospital_asignado, pacientes.enfermedades, pacientes.evolucion_enfermedad, pacientes.fecha_ingreso, pacientes.fecha_salida, pacientes.correo, pacientes.contrasena))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows             
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def update_paciente(self, pacientes):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE pacientes SET id_paciente = %s, dpi = %s, nombre = %s, telefono = %s, direccion = %s, imc = %s, altura = %s, peso = %s, adiccion = %s, enfermedades_hereditarias = %s, tratamientos = %s, medico_asignado = %s, hospital_asignado = %s, enfermedades = %s, evolucion_enfermedad = %s, fecha_ingreso = %s, fecha_salida = %s, correo = %s, contrasena = %s
                                WHERE id_paciente = %s""", (pacientes.id_paciente, pacientes.dpi, pacientes.nombre, pacientes.telefono, pacientes.direccion, pacientes.imc, pacientes.altura, pacientes.peso, pacientes.adiccion, pacientes.enfermedades_hereditarias, pacientes.tratamientos, pacientes.medico_asignado, pacientes.hospital_asignado, pacientes.enfermedades, pacientes.evolucion_enfermedad, pacientes.fecha_ingreso, pacientes.fecha_salida, pacientes.correo, pacientes.contrasena))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows             
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_paciente(self, pacientes):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM pacientes WHERE id_paciente = %s", (pacientes.id_paciente,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows             
        except Exception as ex:
            raise Exception(ex)