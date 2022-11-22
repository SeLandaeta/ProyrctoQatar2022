from Clienteclass import cliente

class clientepartido(cliente):
    def __init__(self,nombre,id,age,ticket,idmatch):
        cliente.__init__(self,nombre,id,age)
        self.ticket = ticket
        self.idmatch =idmatch
    def __repr__(self):
        return(f"Mister/Miss:{self.nombre} \nYour id is: {self.id} \nYour age:{self.age} \nYour tickets are:{self.ticket} for the match number {self.idmatch}")
