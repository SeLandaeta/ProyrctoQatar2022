class partidos:
    def __init__(self,homeTeam,awayTeam,date,stadiumid,id):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.date = date
        self.stadiumid = stadiumid
        self.id = id
    def __repr__(self):
        return(f"""
        HOME TEAM :{self.homeTeam}
        AWAY TEAM:{self.awayTeam} 
        DATE:{self.date}
        STADIUM:{self.stadiumid}
        MATCH ID:{self.id}
        """)
    
           
                