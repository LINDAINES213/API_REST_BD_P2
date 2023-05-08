class Hospitales():
    def __init__(self, codigo, nombre=None, tipo=None, ubicacion=None) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.ubicacion = ubicacion

    def to_JSON(self):
        return{
            'codigo': self.codigo,
            'nombre': self.nombre, 
            'tipo': self.tipo,
            'ubicacion': self.ubicacion
        }
