class producto:
    def __init__(self,nombre,precio,restaurante):
        self.nombre = nombre 
        self.precio = precio
        self.restaurante = restaurante 
        #self.tipo = tipo
    def __repr__(self):
        return(f"PRODUCT:{self.nombre}\nPRICE{self.precio}")