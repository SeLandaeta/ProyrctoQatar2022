class estadios: 
    def __init__(self,id,name,capacity,location):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.location  = location 
    def __repr__(self):
        return(f"""
        STADIUM ID:{self.id}
        STADIUM NAME:{self.name} 
        STADIUM CAPACITY:{self.capacity}K
        LOCATION:{self.location}
        """)