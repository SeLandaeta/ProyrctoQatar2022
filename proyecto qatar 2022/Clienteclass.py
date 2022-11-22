class cliente:
    def __init__(self,nombre,id,age):
        self.nombre = nombre 
        self.id=id
        self.age = age
    def __repr__(self):
        return(f"Mister/Miss:{self.nombre} \nYour id is: {self.id} \nYour age:{self.age} ")
