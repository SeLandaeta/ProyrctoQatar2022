class ticket:
    def __init__(self,numero,idpartido,tipo):
        self.numero = numero
        self.idpartido = idpartido
        self.tipo = tipo

    def __repr__(self):
        return(f"TICKET NUMBER:{self.numero} \nMATCH ID:{self.idpartido} \nTICKET TYPE:{self.tipo}")