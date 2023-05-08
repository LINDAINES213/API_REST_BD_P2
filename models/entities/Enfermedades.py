class Enfermedades():
    def __init__(self, id, nombre=None, tipo=None, sintomas=None, mortalidad=None, ubicacion_geografica=None) -> None:
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.sintomas = sintomas
        self.mortalidad = mortalidad
        self.ubicacion_geografica = ubicacion_geografica
    
    def to_JSON(self):
        return{
            'id': self.id,
            'nombre': self.nombre, 
            'tipo': self.tipo,
            'sintomas': self.sintomas,
            'mortalidad': self.mortalidad,
            'ubicacion_geografica': self.ubicacion_geografica
        }
