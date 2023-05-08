from utils.DateFormats import DateFormat


class Traslados():

    def __init__(self, id_traslados, id_medico=None, hospital_anterior=None, hospital_nuevo=None, fecha_traslado=None) -> None:
        self.id_traslados = id_traslados
        self.id_medico = id_medico
        self.hospital_anterior = hospital_anterior
        self.hospital_nuevo = hospital_nuevo
        self.fecha_traslado = fecha_traslado

    def to_JSON(self):
        return{
            'id_traslados': self.id_traslados,
            'id_medico': self.id_medico,
            'hospital_anterior': self.hospital_anterior,
            'hospital_nuevo': self.hospital_nuevo,
            'fecha_traslado': self.fecha_traslado
        }   
