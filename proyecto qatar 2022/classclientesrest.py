from Clienteclass import cliente 

class clienterest(cliente):
    def __init__(self,nombre,id,age,product):
        cliente.__init__(self,nombre,id,age)
        self.product = product

    def __repr__(self):
        return(f"Mister/Miss:{self.nombre} \nYour id is: {self.id} \nYour age:{self.age} \nProduct:{self.product} ")

