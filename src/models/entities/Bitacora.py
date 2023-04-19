from utils.DateFormats import DateFormat

class Bitacora():
    def __init__(self, fechahora=None, accion=None, nombre_tabla=None) -> None:
        self.fechahora = fechahora
        self.accion = accion
        self.nombre_tabla = nombre_tabla
    
    def to_JSON(self):
        return{
            'fechahora': self.fechahora,
            'accion': self.accion,
            'nombre_tabla': self.nombre_tabla
        }
