from claseproducto import producto


class bebida(producto):
    def __init__(self,nombre,precio,restaurante,type):
        producto.__init__(self,nombre,precio,restaurante)
        self.type = type
        if self.nombre =="Beer":
            self.type = "Alcohol"
        else:
            self.type = "Non-Alcohol"
    
    
    def __repr__(self):
        return(f"**{self.restaurante}**  \nPRODUCT:{self.nombre}\nPRICE:{self.precio}$\nTYPE:{self.type}")


