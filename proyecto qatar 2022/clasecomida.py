from claseproducto import producto


class comida(producto):
    def __init__(self,nombre,precio,restaurante,type,preparation):
        producto.__init__(self,nombre,precio,restaurante)
        self.type = type
        self.preparation = preparation
        if self.nombre == "Fish and Chips":
            self.preparation = "Packeged"
        else:
             self.preparation = "Prepared"
    
    
    def __repr__(self):
        return(f"**{self.restaurante}** \nPRODUCT:{self.nombre}\nPRICE:{self.precio}$\nTYPE:{self.type} \nPREPARATION:{self.preparation}")
    


        
