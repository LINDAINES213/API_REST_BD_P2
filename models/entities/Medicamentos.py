class Medicamentos():
    def __init__(self, id, nombre=None, cantidad_actual=None, cantidad_necesaria=None, necesita_compra=None, hospital=None) -> None:
        self.id = id
        self.nombre = nombre
        self.cantidad_actual = cantidad_actual
        self.cantidad_necesaria = cantidad_necesaria
        self.necesita_compra = necesita_compra
        self.hospital = hospital
    
    def to_JSON(self):
        return{
            'id': self.id,
            'nombre': self.nombre, 
            'cantidad_actual': self.cantidad_actual,
            'cantidad_necesaria': self.cantidad_necesaria,
            'necesita_compra': self.necesita_compra,
            'hospital': self.hospital
        }
