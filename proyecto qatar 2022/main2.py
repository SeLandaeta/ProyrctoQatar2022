import requests
import json 
from Equiposclass import equipos
from Partidos_class import partidos
from Estadioclass import estadios
from Clienteclass import cliente
import random 
from ticketclass import ticket
from clientespartidos import clientepartido
from clasecomida import comida
from bebidasclass import bebida


def buscarporprecio(rango1,rango2,stadiums):
    for stadium in stadiums:
                for restaurantes in stadium["restaurants"]:
                    for data in restaurantes["products"]:
                        if rango1 < (data["price"]+data["price"]*0.16) and (data["price"]+data["price"]*0.16)<rango2:
                                print(f"******",restaurantes["name"],"*****")
                                print("====================================")
                                print(f"PRODUCT:",data["name"])
                                print(f"PRICE:",(data["price"]+data["price"]*0.16),"$")
                                print(f"TYPE:",data["type"])
                                print("====================================")

def crearobjetosmenu(stadiums,listabebidas,listacomidas):
    for stadium in stadiums:
                for restaurantes in stadium["restaurants"]:
                    rest = restaurantes["name"]
                    for data in restaurantes["products"]:
                        if data["type"] == "beverages":
                            
                            
                            
                            new_bebida=bebida(data["name"],data["price"]+(data["price"]*0.16),rest,None)
                            listabebidas.append(new_bebida)
    

                        elif data["type"]=="food":
                            new_comida=comida(data["name"],data["price"]+(data["price"]*0.16),restaurantes["name"],data["type"],None)
                            listacomidas.append(new_comida)

def getrestaurante(stadiums,restabuscar):
     print("==================================")
     print("*********RESTAURANT MENU**********")
     print("==================================")

     for stadium in stadiums:
                for restaurantes in stadium["restaurants"]:
                    restmayus = restaurantes["name"].upper()
                    for data in restaurantes["products"]:
                            if restabuscar == restmayus:
                                print("______________________")
                                print(f"PRODUCT:",data["name"])
                                print(f"PRICE:",data["price"])
                                print(f"TYPE:",data["type"])

def buscarprodpornombre(stadiums,prodabuscar):
    for stadium in stadiums:
                for restaurantes in stadium["restaurants"]:
                    for data in restaurantes["products"]:
                        datamayus = data["name"].upper()
                        if prodabuscar == datamayus:
                                print(f"******",restaurantes["name"],"*****")
                                print("====================================")
                                print(f"PRODUCT:",data["name"])
                                print(f"PRICE:",(data["price"]+data["price"]*0.16),"$")
                                print(f"TYPE:",data["type"])
                                print("====================================")

def buscarportipo(lista):
    for data in lista:
        print ("****",data["name"],"****")
        for info in data["products"]:
            print("=======================")
            print(f"PRODUCT:",info["name"])
            print(f"PRICE:",info["price"]+(info["price"]*0.16))
            print(f"TYPE:",info["type"])
        
def get_estadio(lista2,lista,numero):
    for partidos in lista:
        for stadiums in lista2:
         if (partidos["stadium_id"]== numero):
            if (partidos["stadium_id"]==stadiums["id"]):
                return stadiums["name"]
            
def welcome():
    print("* WELCOME TO QATAR WORLD CUP OFFICIAL SITE * ")

def buscarpp(lista,country,lista2):
    for partidos in lista:
            home = partidos["home_team"].upper()
            if (home == country):
                print("_________________________________")
                print("HOME TEAM: ",partidos["home_team"])
                print("AWAY TEAM: ",partidos["away_team"])
                print("DATE: ",partidos["date"])
                print("STADIUM:",get_estadio(lista2,lista,partidos["stadium_id"]))
                print("_________________________________")
                
                
            away = partidos["away_team"].upper()
            if (away== country):
                print("_________________________________")
                print("HOME TEAM: ",partidos["home_team"])
                print("AWAY TEAM: ",partidos["away_team"])
                print("DATE: ",partidos["date"])
                print("STADIUM:",get_estadio(lista2,lista,partidos["stadium_id"]))
                print("_________________________________")           
           
def buscarporestadio(lista,estadioid,lista2):

    for partidos in lista:
            estadios = partidos["stadium_id"]
            if (estadios== estadioid):
                print("_________________________________")
                print("HOME TEAM: ",partidos["home_team"])
                print("AWAY TEAM: ",partidos["away_team"])
                print("DATE: ",partidos["date"])
                print("STADIUM:",get_estadio(lista2,lista,partidos["stadium_id"]))
                print("_________________________________")

def buscarporfecha(lista,fecha,lista2):
    for partidos in lista:
            newdate = partidos["date"].split(" ")

            if (newdate[0]==fecha):
                print("_________________________________")
                print("HOME TEAM: ",partidos["home_team"])
                print("AWAY TEAM: ",partidos["away_team"])
                print("DATE: ",partidos["date"])
                print("STADIUM:",get_estadio(lista2,lista,partidos["stadium_id"]))
                print("_________________________________")

def crearobid(lista,id,lista2):
      for partido in lista:
            estadiopart = get_estadio(lista2,lista,partido["stadium_id"])
           
            
            if (partido["id"] == id):
                new_partido_factura = partidos(partido["home_team"],partido["away_team"],partido["date"],estadiopart,partido["id"]) 
                return new_partido_factura

def generar_ticket (totalticket,idtickets,listatickets,matchid,tickets,aux,idt):
    while aux < totalticket:
                        aux += 1
                        numrandom = random.randint(1,10000)
                        idt.append(numrandom)
                        idtickets.append(numrandom)
                        newticket = ticket(numrandom,matchid,tickets)
                        listatickets.append(newticket)

def main():
    #____________________________________________________________________________
    #Aqui accedo a la API y la convierto en json para poder manejar la informacion
    #____________________________________________________________________________
    url3 = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json"
    r2 = requests.get(url3)
    stadiums=r2.json()
    listastadiums = []


    url1 = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json"
    r1 = requests.get(url1)
    matches  = r1.json()
    listapartidos = []

    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json"
    r = requests.get(url)
    teams = r.json()
    listateams = []
    nombreequipos = []
    idestadios = []
    fechas=[]
    
    
    #_____________________________________________________________________________________
    #Aqui tomo la informacion desde mi api y la convierto en objetos
    #_____________________________________________________________________________________
    
    for team in teams: 
        new_team = equipos(team["name"],team["flag"],team["fifa_code"],team["group"],team["id"])
        listateams.append(new_team)
        ide = int( team["id"])
        nombreequipos.append(team["name"].upper())
    

    
        
   


    for match in matches:
        for stadium in stadiums:
            matchnew = match["date"].split(" ")
            fechas.append(matchnew[0])
            
            
            estadiopart = get_estadio(stadiums,matches,match["stadium_id"])
        partidonuevo = partidos(match["home_team"],match["away_team"],matchnew,estadiopart,match["id"])
        listapartidos.append(partidonuevo)

    

    for stadium in stadiums:
        estadionuevo = estadios(stadium["id"],stadium["name"],stadium["capacity"],stadium["location"])
        listastadiums.append(estadionuevo)
        idestadios.append(stadium["id"])


    

    #==================================================
    #Aqui guardo datos para poder manejarlos a mi antojo
    #==================================================
    totalticketsnormal = 0
    totalticketsvip = 0
    pricevip =0
    pricenormal =0
    price_neto  = 0
    price_neto += (pricevip + pricenormal)
    decuento = 0
    pricedescuento  = price_neto-decuento
    partidosporfactura = []
    listaclientes = []
    idtickets = []
    idtvip = []
    idtreg = []
    listatickets=[]
    cedulavip = []
    listarestaurantes = []
    listacomidas = []
    listabebidas = []
    listaalcoholes = []
    listanoalcoholes =[]
    listapacaged = []
    listaprepared = []
    prodname = []
    clientesrestaurantes = []
    idclientesrestaurante = []



    while True:

        welcome()

        #Modulo principal

        opcion = input("Please select a module: \n1-MATCHES AND STADIUMS MANAGEMENT \n2-BUY TICKETS FOR A MATCH \n3-CHECK MATCH ATTENDENCE \n4-SHOW RESTAURANTS AND BUY FOOD\n---->")
        if opcion == "1":
           while True:


                #=======================================================================
                #Entramos al modulo de el manejo de la data de las api y la busqueda por informacion especifica
                #=======================================================================

                opcion2 = input("Please select and option: \n1-SHOW ALL MATCHES \n2-SHOW ALL TEAMS \n3-SHOW ALL STADIUMS \n4-BROWSE \n5-EXIT \n----->")
                if opcion2 == "1":
                    for partido in listapartidos: 
                        print (partido)

                elif opcion2 == "2":
                    for equipo in listateams:
                        print (equipo)

                elif opcion2 == "3":
                    for estadio in listastadiums:
                        print(estadio)

                elif opcion2 == "4":
                    while True:
                        browoption = input("PLEASE SELECT A BROWSING OPTION: \n1-SEARCH YOUR FAVOURITE TEAM MATCHES \n2-SHOW MATCHES PLAYED IN ONE STADIUM \n3-SHOW MATCHES PLAYED IN A SPECIFIC DATE \n4-GO BACK \n-----> ")
                        
                        if browoption == "1":
                            country = input("PLEASE ENTER YOUR FAVOURITE TEAM NAME:\n-----> ").upper()
                            if buscarpp(matches,country,stadiums):
                                buscarpp(matches,country,stadiums)
                            if country not in nombreequipos:
                                print("_________________________________________________")
                                print("JAJA YOUR TEAM IS NOT IN THE WORLD CUP, BE BETTER")
                                rint("_________________________________________________")

                            
                        


                        elif browoption =="2":
                            stadiumid = int(input("PLEASE ENTER THE STADIUM ID:\n------> "))
                            if buscarporestadio(matches,stadiumid,stadiums):
                                buscarporestadio(matches,stadiumid,stadiums)
                            if stadiumid not in idestadios:
                                print("___________________________________________")
                                print("ERROR 404 NOT FOUNDED IN THE WORLD CUP DATA")
                                print("___________________________________________")
                            
                            
                        
                        elif browoption == "3":
                            date = input("PLEASE ENTER A DATE TO BROWSE(dd/m/yyyy): \n------>")
                            if buscarporfecha(matches,date,stadiums):
                                buscarporfecha(matches,date,stadiums)
                            if date not in fechas:
                                print("___________________________")
                                print("WE COULD NOT FIND YOUR DATE")
                                print("___________________________")

                        
                        elif browoption == "4":
                            break


                elif opcion2 == "5":
                    break
                elif opcion2 is int:
                    print ("Please enter a number not a letter") 
                else:
                    print("_____________________________")
                    print("Please chose a correct option")
                    print("_____________________________")
            
            
        elif opcion == "2":
            while True:
                for partido in listapartidos: 
                        print (partido) 
                print("$$$$$ LETS BUY $$$$$")
                name = input("PLEASE ENTER YOUR NAME: \n---->")
                idpersona = input("PLEASE ENTER YOUR ID: \n---->")
                age = input("PLEASE ENTER YOUR AGE: \n----->")
                matchid = input("PLEASE ENTER ID OF THE MATCH YOU WANT TO BUY TICKETS FOR: \n----->")
                if matchid not in idestadios:
                    print("ERROR 404 NOT FOUNDED")
                print("====================")
                print("*******PRICES*******")
                print("REGULAR TICKET: 50$")
                print("VIP TICKET: 120$")
                print("====================")
                tickets = input("PLEASE SELECT A TICKET [(V) VIP OR (R) REGULAR]:\n------>").upper()
                personanew = clientepartido(name,idpersona,age,tickets,matchid)
                listaclientes.append(personanew)
                aux = 0
                

                
                if tickets == "R":

                    totalticketsnormalr =int( input("PLEASE ENTER THE NUMBER OF TICKETS:\n-----> "))
                    totalticketsnormal += int(totalticketsnormalr)
                    pvp2 = 50
                    precionor = totalticketsnormal*pvp2
                   
                    pricenormal += precionor
                    
                    generar_ticket(totalticketsnormal,idtickets,listatickets,matchid,tickets,aux,idtreg)
                    
                

                elif tickets == "V":
                    totalticketsvipr = int ( input("PLEASE ENTER THE NUMBER OF TICKETS:\n-----> "))
                    totalticketsvip += int(totalticketsvipr)
                    pvp = 120
                    preciovip = totalticketsvip*pvp
                    pricevip += preciovip
                    generar_ticket(totalticketsvip,idtickets,listatickets,matchid,tickets,aux,idtvip)
                    cedulavip.append(idpersona)


                
                opcionticket = input("DO YOU WANT TO BUY MORE TICKETS? [Y(YES)/N(NO)] \n---->").capitalize()
                if opcionticket == "Y":
                    continue
                elif opcionticket =="N":
                    break
            print("$$$$$$$$$$$$$$ RECEIPT $$$$$$$$$$$$$$$$")
            print ("YOUR TOTAL VIP TICKESTS IS:",totalticketsvip)
            print("YOUR PRICE FOR THE VIP TICKETS IS:",pricevip)
            print("YOUR TOTAL REGULAR TICKETS IS:", totalticketsnormal)
            print("YOUR PRICE FOR THE REGULAR TICKETS IS:",pricenormal)
            print("$$$$$$$$$$$$$$ RECEIPT $$$$$$$$$$$$$$$$")
          
           
            for indvtickets in listatickets:
                print("________________________")
                print(indvtickets)
                print("________________________")
            
            
            partidosporfactura.append(crearobid(matches,matchid,stadiums))
            
        elif opcion == "3":

            #==========================================================================
            #ACA ENTRO EN LA VALIDACION DE TICKETS, REVISANDO LA LISTA DE LOS ID DE LOS TICKETS QUE GURDE ANTES 
            #=========================================================================

            ticket_a_revisar = int(input("PLEASE ENTER THE TICKET ID TO CHECK IT:"))

            if ticket_a_revisar not in idtickets:
                print("")
                print("========================")
                print("YOUR TICKET IS NOT VALID")
                print("========================")
                print("")
            elif ticket_a_revisar in idtickets:
                print("")
                print("===============================")
                print("YOUR TICKET HAVE BEEN VALIDATED")
                print('WELCOME TO THE QATAR 2022 WC')
                print("===============================")
                print("")


            ... 
        
        elif opcion =="4":
            #=================================================================
            #RECORRO EL JSON CREADO A PARTIR DE LA API PARA PODER ACCEDER A LOS RESTAURANTES
            #=================================================================
            crearobjetosmenu(stadiums,listabebidas,listacomidas)
            for stadium in stadiums:
                for restaurantes in stadium["restaurants"]:
                    restmayus = restaurantes["name"].upper()
                    listarestaurantes.append(restmayus)
                    for data in restaurantes["products"]:
                        dataupper = data["name"].upper()
                        prodname.append(dataupper)
                        if data["name"] == "Beer":
                            listaalcoholes.append(restaurantes)
                        elif data["name"] == "Pepsi" or data["name"] == "Water":
                            listanoalcoholes.append(restaurantes)
                        elif data["name"]=="Hamburger":
                            listaprepared.append(restaurantes)
                        elif data["name"]=="Fish and Chips":
                            listapacaged.append(restaurantes)
            #==========================================================================
            # Aqui imprimo todas las bebidas para que el cliente pueda ver las opciones 
            #==========================================================================
            print("")
            print("======== BEVERAGES ========")
            print("")
            for bebidas in listabebidas:
                print("================")
                print (bebidas)
                print("================")
            print("")
            print("======== FOOD ========")
            print("")
            for comidas in listacomidas:
                print("================")
                print(comidas)
                print("================")
            
            pedircedula = input("PLEASE ENTER YOUR ID: \n")
            if pedircedula not in cedulavip:
                print("==============================")
                print("YOU DONT HAVE THE A VIP TICKET")
                print("==============================")
            elif pedircedula in cedulavip:
                opcioncompraobusqueda = input("PLEASE ENTER AN OPTION: \n1-BUY FOOD \n2-SEARCH FOOD \n")
                if opcioncompraobusqueda == "2":
                    opcionbusquedarest = input("PLEASE ENTER THE WAY YOU WANT TO SEARCH IN THE MENUS:\n1-PER RESTAURANT NAME \n2-PER ITEM NAME \n3-PER ITEM TYPE \n4-PER ITEM PRICE \n")
                    if opcionbusquedarest == "1":
                        restauranteapedir = input("PLEASE ENTER THE NAME OF RESTAURANT YOU WANT TO BUY FROM: ").upper()
                        if restauranteapedir not in listarestaurantes:
                            print("==================================")
                            print("YOUR RESTAURANT IS NOT IN OUR LIST")
                            print("==================================")
                        elif restauranteapedir in listarestaurantes:
                            getrestaurante(stadiums,restauranteapedir)
                            
                        elif restauranteapedir is int:
                            print("ERROR 404 NOT FOUNDED")
                    elif opcionbusquedarest == "2":
                        prod = input("PLEASE ENTER THE PRODUCT YOU WANT TO LOOK FOR: ").upper()
                        while prod not in prodname:
                            prod = input("PLEASE WRITE A CORRECT OPTION \n")
                            
                        buscarprodpornombre(stadiums,prod)
                    elif opcionbusquedarest == "3":
                        opciontipos = input("PLEASE ENTER THE TYPE YOU ARE LOOKING FOR: \n1-NON-ALCOHOLIC DRINKS \n2-ALCOHOLIC DRINKS \n3-PREPARED FOOD \n4-PACKEGED FOOD \n")
                        if opciontipos =="1":
                            buscarportipo(listanoalcoholes)
                        elif opciontipos =="2":
                            buscarportipo(listaalcoholes)
                        elif opciontipos == "3":
                            buscarportipo(listaprepared)
                        elif opciontipos == "4":
                            buscarportipo(listapacaged)
                        else:
                            print("ERROR 404 NOT FOUNDED ")
                    elif opcionbusquedarest == "4":
                        range1 = int(input("PLEASE THE SMALLES PRICE: \n"))
                        range2 = int(input("PLEASE ENTER THE HIGHEST VALUE: \n"))
                        buscarporprecio(range1,range2,stadiums)
                    

                elif opcioncompraobusqueda == "1":
                    nombrecliente = input("PLEASE ENTER YOUR NAME: \n")
                    pedircedula = input("PLEASE ENTER YOUR ID: \n")
                    if pedircedula not in cedulavip:
                        print("==============================")
                        print("YOU DONT HAVE THE A VIP TICKET")
                        print("==============================")
                    idclientesrestaurante.append(pedircedula)
                    edadcliente = (input("PLEASE ENTER YOUR AGE: \n"))
                    if edadcliente.isnumeric():
                        edadcliente = int(edadcliente)
                    else:
                        print("=====================")
                        print ("SOMETHING WENT WRONG")
                        print("=====================")
                    productocliente = input("PLEASE ENTER THE NAME OF THE PRODUCT YOU WANT TO BUY: \n").upper()
                    if edadcliente < 18:
                        if productocliente == "BEER":
                            print("YOU ARE TOO YOUNG TO BUY THIS PRODUCT")
                    else:
                        print("beso negro")
                    

                    



                    

        elif opcion == "5":
            ...
        
        elif opcion == "6":
            ...
        
        elif opcion == "7":
            break 

        else:
            print("_____________________________")
            print("Please chose a correct option")
            print("_____________________________")


main()
