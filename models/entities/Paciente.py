from utils.DateFormats import DateFormat


class Paciente():

    def __init__(self, id_paciente, dpi=None, nombre=None, telefono=None, direccion=None, imc=None, altura=None, peso=None, adiccion=None, enfermedades_hereditarias=None, tratamientos=None, medico_asignado=None, hospital_asignado=None, enfermedades=None, evolucion_enfermedad=None, fecha_ingreso=None, fecha_salida=None, correo=None, contrasena=None) -> None:
        self.id_paciente = id_paciente
        self.dpi = dpi
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.imc = imc
        self.altura = altura
        self.peso = peso
        self.adiccion = adiccion 
        self.enfermedades_hereditarias = enfermedades_hereditarias
        self.tratamientos = tratamientos
        self.medico_asignado = medico_asignado
        self.hospital_asignado = hospital_asignado
        self.enfermedades = enfermedades
        self.evolucion_enfermedad = evolucion_enfermedad
        self.fecha_ingreso = fecha_ingreso
        self.fecha_salida = fecha_salida
        self.correo = correo
        self.contrasena = contrasena

    def to_JSON(self):
        return{
            'id_paciente': self.id_paciente,
            'dpi': self.dpi,
            'nombre': self.nombre, 
            'telefono': self.telefono,
            'direccion': self.direccion,
            'imc': self.imc,
            'altura': self.altura,
            'peso': self.peso,
            'adiccion': self.adiccion,
            'enfermedades_hereditarias': self.enfermedades_hereditarias,
            'tratamientos': self.tratamientos,
            'medico_asignado': self.medico_asignado,
            'hospital_asignado': self.hospital_asignado,
            'enfermedades': self.enfermedades,
            'evolucion_enfermedad': self.evolucion_enfermedad,
            'fecha_ingreso': self.fecha_ingreso,
            'fecha_salida': self.fecha_salida,
            'correo': self.correo,
            'contrasena': self.contrasena
        }       