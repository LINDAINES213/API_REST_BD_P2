from utils.DateFormats import DateFormat


class Medicos():

    def __init__(self, id_medico, dpi=None, nombre=None, telefono=None, direccion=None, num_colegiado=None, especialidades=None, hospital=None, fecha_contratacion=None, correo=None, contrasena=None) -> None:
        self.id_medico = id_medico
        self.dpi = dpi
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.num_colegiado = num_colegiado
        self.especialidades = especialidades
        self.hospital = hospital
        self.fecha_contratacion = fecha_contratacion
        self.correo = correo
        self.contrasena = contrasena

    def to_JSON(self):
        return{
            'id_medico': self.id_medico,
            'dpi': self.dpi,
            'nombre': self.nombre, 
            'telefono': self.telefono,
            'direccion': self.direccion,
            'num_colegiado': self.num_colegiado,
            'especialidades': self.especialidades,
            'hospital': self.hospital,
            'fecha_contratacion': self.fecha_contratacion,
            'correo': self.correo,
            'contrasena': self.contrasena
        }
