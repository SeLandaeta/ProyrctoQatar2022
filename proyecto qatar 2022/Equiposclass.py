class equipos:
    def __init__ (self,name,flag,fifacode,fifagroup,id):
        self.name = name
        self.flag = flag
        self.fifacode = fifacode
        self.fifagroup = fifagroup
        self.id = id
    def __repr__(self):
            return (f"""
            TEAM NAME:{self.name}
            TEAM FLAG:{self.flag} 
            TEAM FIFA CODE:{self.fifacode}
            WORLD CUP GROUP:{self.fifagroup}
            TEAM ID:{self.id} 
            """)
