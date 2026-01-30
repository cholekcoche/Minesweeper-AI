import math, random



class Configuracion:
    #Esto es una configuración default
    NumeroCasillas = 100
    NumeroBombas = 15
    CaracterCasillasVacias = "."
    

    def obtener_lado(self):
        return int(math.sqrt(self.NumeroCasillas))

    def get_NumeroBombas(self):
        return self.NumeroBombas
    
    def get_NumeroCasillas(self):
        return self.NumeroCasillas
    
    def get_CaracterCasillasVacias(self):
        return self.CaracterCasillasVacias

    def set_NumeroBombas(self, NumeroBombas):
        if NumeroBombas % 1 != 0:
            print("No se admiten numeros decimales")
            return

        elif NumeroBombas < 0:
            print("Error, no se puede estableces un numero menor a 0 bombas")

        elif NumeroBombas > self.NumeroCasillas:
            print("No se pueden estableces más bombas que casillas")
            
        

        else:
            self.NumeroBombas = NumeroBombas
            

    def set_NumeroCasillas(self, NumeroCasillas):

        if NumeroCasillas % 1 != 0:
            print("Lo siento, pero solo se aceptan numeros enteros")
            return
        
        raiz = math.sqrt(NumeroCasillas)

        if not raiz.is_integer():
            print("Lo siento, pero el tablero solamente puede ser cuadrado")

        elif NumeroCasillas < 9:
            print("No se admiten tableros menores a 3x3")

        elif NumeroCasillas > 3600:
            print("La consola muestra el tablero con errores cuando la cifra de casillas supera 3600")
            print("¿Estas seguro que quieres más de 3600 casillas?")
            print("S//N")
            respuesta = input(">> ")
            if respuesta.title() == "S" or respuesta.title() == "Y":
                print("Actualizado")
                self.NumeroCasillas = NumeroCasillas

            else:
                print("El numero actual de casillas es:")
                print(self.NumeroCasillas)
                


        
        else:
            if self.NumeroBombas >= NumeroCasillas:
                self.set_NumeroBombas(NumeroCasillas//2)
            self.NumeroCasillas = NumeroCasillas

    def set_CaracterCasillasVacias(self, CaracterCasillasVacias):
        self.CaracterCasillasVacias = CaracterCasillasVacias





class Casilla:

    Caracter_bomba = "♠"
    Caracter_bandera = "‼"

    

    def __init__(self, Fila, Columna, Bomba, Caracter, Valor):
        self.Fila = Fila
        self.Columna = Columna
        self.Bomba = Bomba
        self.Caracter = Caracter
        self.Valor = Valor #Esto es para el bot
        

    def set_Bomba(self, Bomba):
        self.Bomba = Bomba

    


    def Comprobar_bomba(self):
        return self.Bomba

                            



     

        




class Partida:

    Tablero = []

    def Bombas_proximas(self, Casilla):
        Bombas_cerca = 0
        Fila = Casilla.Fila
        Columna = Casilla.Columna

        
        for i in range(Fila-1, Fila+2):
            for j in range(Columna-1, Columna+2):
                if i < 0 or i == Mapa.obtener_lado():#########Esto es lo más importante para no meter muchos if
                    continue

                if j < 0 or j == Mapa.obtener_lado():
                    continue

                elif i == Fila and j == Columna:
                    continue
                else:
                    Bombas_cerca = Bombas_cerca+Juego.Tablero[i][j].Comprobar_bomba()

        return Bombas_cerca
    
    def Cambiar_valor(self, Fila, Columna):
        Revisar = []
        Revisar.append(self.Tablero[Fila][Columna])
        Vistas = []

        while Revisar != []:

            Revisar[0].Caracter = str(self.Bombas_proximas(Revisar[0]))
        
       
            if Revisar[0].Caracter != "0":
                Vistas.append(Revisar[0])
                Revisar.pop(0)
            else:
                for i in range(Revisar[0].Fila-1, Revisar[0].Fila+2):
                    for j in range(Revisar[0].Columna-1, Revisar[0].Columna+2):

                        if i < 0 or i == Mapa.obtener_lado():
                            continue
                        elif j < 0 or j == Mapa.obtener_lado():
                            continue

                        else:
                            if self.Tablero[i][j].Caracter == Casilla.Caracter_bandera:
                                continue


                            elif self.Tablero[i][j] in Revisar or self.Tablero[i][j] in Vistas:
                                continue
                            else:
                                Revisar.append(self.Tablero[i][j])

                Vistas.append(Revisar[0])
                Revisar.pop(0)

    def Comprobar_victoria(self):
        CasillasSinNumero = 0
        Numeros = ["0","1","2","3","4","5","6","7","8","9"]

        for fila in self.Tablero:
            for casilla in fila:
                if casilla.Caracter not in Numeros:
                    CasillasSinNumero = CasillasSinNumero+1
                else:
                    continue

        if CasillasSinNumero == Mapa.NumeroBombas:
        
            return 1
        
        else:
            return 0
        
        
    def set_bandera(self):
        Eleccion = 1
        while Eleccion == 1:

            print("""
Puedes:
1. Poner
2. Quitar
3. Volver""")
        
            Quitar = input(">> ")
        
            if Quitar == "1":
                Juego.Vista_tablero(0)
                Datos = self.selec_casilla()
                Fila = Datos[0]
                Columna = Datos[1]
                if self.Tablero[Fila][Columna].Caracter == Mapa.CaracterCasillasVacias:
                    self.Tablero[Fila][Columna].Caracter = Casilla.Caracter_bandera
                    Juego.Vista_tablero(0)

                else:
                    print("Lo siento, no es posible poner banderas en casillas con contenido. Solo se permite en casillas 'vacias'")
            
            elif Quitar == "2":
                Juego.Vista_tablero(0)
                Datos = self.selec_casilla()
                Fila = Datos[0]
                Columna = Datos[1]
                if self.Tablero[Fila][Columna].Caracter == Casilla.Caracter_bandera:
                    self.Tablero[Fila][Columna].Caracter = Mapa.CaracterCasillasVacias
                    Juego.Vista_tablero(0)
                else:
                    print("No se ha encontrado la bandera")

            else:
                Eleccion = 0

    def set_bandera_bot(self, casilla):
        self.Tablero[casilla.Fila][casilla.Columna].Caracter = Casilla.Caracter_bandera
        return






            
    
    



    def Vista_tablero(self, All):
        print("\n")
        Ejex = True
        Espacios = len(str(Mapa.obtener_lado()))
        Resultado = ""
        Numero_fila = 1
        Numero_casilla = 1
        Corrector = 1

        if All == 1: #Una vez has perdido mostrara el mapa con tus casillas y las bombas
            if Ejex == True:
                for z in range(0, Mapa.obtener_lado()+1):
                    if z == 0:
                            Resultado = " "

                

                    else:
                        if z == 1:
                            Resultado = Resultado+" "*len(str(Mapa.obtener_lado()))+str(z)


                        elif len(str(Mapa.obtener_lado())) > len(str(z)):  
                            Resultado = Resultado+" "*2+str(z)

                        elif len(str(Mapa.obtener_lado())) == 1:
                            Resultado = Resultado+" "*2+str(z)

                    
                        else:
                            Resultado = Resultado+" "+str(z)

                Ejex = False
                print(Resultado)
                Resultado = ""
            



            for fila in self.Tablero:
                Primer_recorrido = 1
                Resultado = str(Numero_fila)
                Numero_casilla = 1
            
            
                
            
                for casilla in fila:
                        
                    if Primer_recorrido == 1:
                        Primer_recorrido = 0

                        if casilla.Bomba == 1:
                            Resultado = Resultado+" "*Espacios+casilla.Caracter_bomba
                            Numero_casilla = Numero_casilla+1

                        else:
                            Resultado = Resultado+" "*Espacios+casilla.Caracter
                            Numero_casilla = Numero_casilla+1
                    

                

                    else:

                        if casilla.Bomba == 1:

                            Resultado = Resultado+"  "*Corrector+casilla.Caracter_bomba
                            Numero_casilla = Numero_casilla+1

                        else:
                            Resultado = Resultado+"  "*Corrector+casilla.Caracter
                            Numero_casilla = Numero_casilla+1
                    
                
                print(Resultado)


                Numero_fila = Numero_fila+1
                if len(str(Numero_fila)) > len(str(Numero_fila-1)):
                    Espacios = Espacios-1



        else:#El mapa de forma normal para jugar
        
            if Ejex == True:
                for z in range(0, Mapa.obtener_lado()+1):
                    if z == 0:
                            Resultado = " "

                

                    else:
                        if z == 1:
                            Resultado = Resultado+" "*len(str(Mapa.obtener_lado()))+str(z)


                        elif len(str(Mapa.obtener_lado())) > len(str(z)):  
                            Resultado = Resultado+" "*2+str(z)

                        elif len(str(Mapa.obtener_lado())) == 1:
                            Resultado = Resultado+" "*2+str(z)

                    
                        else:
                            Resultado = Resultado+" "+str(z)

                Ejex = False
                print(Resultado)
                Resultado = ""
            



            for fila in self.Tablero:
                Primer_recorrido = 1
                Resultado = str(Numero_fila)
                Numero_casilla = 1
            
            
                
            
                for casilla in fila:
                        
                    if Primer_recorrido == 1:
                        Primer_recorrido = 0

                        Resultado = Resultado+" "*Espacios+casilla.Caracter
                        Numero_casilla = Numero_casilla+1
                    

                

                    else:

                        Resultado = Resultado+"  "*Corrector+casilla.Caracter
                        Numero_casilla = Numero_casilla+1
                    
                
                print(Resultado)


                Numero_fila = Numero_fila+1
                if len(str(Numero_fila)) > len(str(Numero_fila-1)):
                    Espacios = Espacios-1




    

                        
                        





    def creacion_tablero(self):

        for i in range(0, Mapa.obtener_lado()):
            fila = []

            for j in range(0, Mapa.obtener_lado()):

                fila.append(Casilla(i, j, 0, Mapa.get_CaracterCasillasVacias(), 0))

            self.Tablero.append(fila)

    def selec_casilla(self):
        while True:
            print("\n Dime la fila")
            Fila = input(">> ")
            print("Dime la columna")
            Columna = input(">> ")

            try:
                Fila = int(Fila)
                Columna = int(Columna)
                Fila = Fila-1
                Columna = Columna-1
                break

            except:
                continue
            

        Datos = []
        Datos.append(Fila)
        Datos.append(Columna)
        return Datos
    
    def Que_quieres_hacer(self):

        while True:
            print("¿Que quieres hacer?")
            print("""
1. Poner/Quitar una bandera
2. Seleccionar casilla
3. Que juegue el bot
""")
            Info = input(">> ")
            if Info.title() == "Poner una bandera" or Info == "1":
                return 0
            
            elif Info.title() == "Seleccionar casilla" or Info == "2":
                return 1
            
            elif Info.title() == "Que juegue el bot" or Info == "3":
                return 2
            else:
                print("No te he entendido, dimelo otra vez")
            



    

    def set_bombas(self, i, j):
        Numero_bombas_puestas = 0

        Ayuda_fila = [i, i+1, i-1]
        Ayuda_Columna = [j, j+1, j-1]

        while Numero_bombas_puestas < Mapa.get_NumeroBombas():

                for fila in self.Tablero:
                    for casilla in fila:

                        Bomba = random.randint(1,50)

                        if Numero_bombas_puestas == Mapa.get_NumeroBombas():
                            continue

                        elif casilla.Fila == i and casilla.Columna == j:
                            continue

                        elif casilla.Fila in Ayuda_fila and casilla.Columna != j and casilla.Bomba == 0:
                            Bomba = random.randint(1,150)
                            if Bomba == 1:
                                casilla.Bomba = Bomba
                                Numero_bombas_puestas = Numero_bombas_puestas+1

                            else:
                                continue


                        elif casilla.Columna in Ayuda_Columna and casilla.Fila != i and casilla.Bomba == 0:
                            Bomba = random.randint(1,150)
                            if Bomba == 1:
                                casilla.Bomba = Bomba
                                Numero_bombas_puestas = Numero_bombas_puestas+1

                            else:
                                continue
                        

                        
                        elif Bomba == 1 and casilla.Bomba == 0:
                            casilla.Bomba = 1
                            Numero_bombas_puestas = Numero_bombas_puestas+1

    def Partida_empezada(self):
        Sesion = 1
        Primera_casilla = 1
        Respuesta = None
        self.Tablero = []
        Juego.creacion_tablero()
        Robot = None
        

        while Sesion == 1:
            
            self.Vista_tablero(0)
            
            if Primera_casilla == 1:

                
                
                Respuesta = self.selec_casilla()
                self.set_bombas(Respuesta[0], Respuesta[1])
                self.Cambiar_valor(Respuesta[0], Respuesta[1])
                Primera_casilla = 0

            else:

                if self.Comprobar_victoria() == 1:
                    Sesion = 0
                    print("Has ganado!!!")
                    Juego.Vista_tablero(0)
                    continue

                else:


                    Respuesta = Juego.Que_quieres_hacer()
                    if Respuesta == 0:
                        self.set_bandera()

                    elif Respuesta == 1:

                        Respuesta = self.selec_casilla()

                        if Juego.Tablero[Respuesta[0]][Respuesta[1]].Comprobar_bomba() == 1:
                            print("Lo siento, había una bomba")
                            Juego.Vista_tablero(0)
                            self.Vista_tablero(1)
                            Sesion = 0
                        


                        else:

                            self.Cambiar_valor(Respuesta[0], Respuesta[1])

                    elif Respuesta == 2:
                        Robot = Bot()
                        Robot.obtener_mapa(self.Tablero)
                        Robot.obtener_configuracion(Mapa)
                        Respuesta = Robot.Pasos()############################33
                        if Respuesta == 2:
                            print("El bot lo logro")
                            Juego.Vista_tablero(0)
                            break

                        else:
                            break


                    else:#Evitar fallo
                        continue

        

class Bot:

    Mapa_bot = []
    Settings = None
    Evitar = []

    def obtener_mapa(self, Tablero):
        self.Mapa_bot = Tablero


    def obtener_configuracion(self, config):
        self.Settings = config

        


    def Pasos(self):
        Bordes = []
        Resuelto = 0
        
        while Resuelto == 0:
            self.obtener_mapa(Juego.Tablero)
            Juego.Vista_tablero(0)
            Bordes = self.Guardar_bordes()
            Resuelto = self.Resolver(Bordes)
            if Resuelto == 1:
                print("Lo siento, el bot ha fallado.")
                return 1
            Resuelto = Juego.Comprobar_victoria()
            if Resuelto == 1:
                print("Has ganado")
                return 2




    def Guardar_bordes(self):
        Bordes = []
        Numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        for fila in self.Mapa_bot:
            for casilla in fila:
                if casilla.Caracter in Numeros:
                    for i in range(-1,2):
                        for j in range(-1,2):
                            if casilla.Fila+i < 0:
                                continue

                            elif casilla.Fila+i > len(fila)-1:

                                continue

                            elif casilla.Columna+j < 0:
                                continue
                                
                            elif casilla.Columna+j > len(fila)-1:
                                continue

                            elif self.Mapa_bot[casilla.Fila+i][casilla.Columna+j].Caracter == self.Settings.CaracterCasillasVacias:
                                if casilla not in Bordes:
                                    Bordes.append(casilla)
                                    continue

                            else:
                                continue

                else:
                    continue

        return Bordes
    
    def Resolver(self, Bordes):
        Cambio = 0 #Monitorea si ha habido algun cambio
        Casillas_vacias = []
        for fila in self.Mapa_bot:
            for casilla in fila:
                
                Banderas = []
                Casillas_vacias = []
                if casilla in Bordes:
                    for i in range(-1,2):
                        for j in range(-1,2):
                            if casilla.Fila+i < 0 or casilla.Fila+i > len(fila)-1:
                                continue
                            elif casilla.Columna+j < 0 or casilla.Columna+j > len(fila)-1:
                                continue
                            elif self.Mapa_bot[casilla.Fila+i][casilla.Columna+j].Caracter == self.Settings.CaracterCasillasVacias:
                                if self.Mapa_bot[casilla.Fila+i][casilla.Columna+j] not in Casillas_vacias:
                                    Casillas_vacias.append(self.Mapa_bot[casilla.Fila+i][casilla.Columna+j])
                                    

                            elif self.Mapa_bot[casilla.Fila+i][casilla.Columna+j].Caracter == Casilla.Caracter_bandera:
                                if self.Mapa_bot[casilla.Fila+i][casilla.Columna+j] not in Banderas:

                                    Banderas.append(self.Mapa_bot[casilla.Fila+i][casilla.Columna+j])
                                    
                    if casilla.Caracter == len(Banderas):
                        for i in range(len(Casillas_vacias)):


                            Juego.Cambiar_valor(Casillas_vacias[i].Fila, Casillas_vacias[i].Columna)
                        Cambio = 1


                    elif len(Casillas_vacias) == int(casilla.Caracter)-len(Banderas):
                        

                        
                        
                        
                        for i in range(len(Casillas_vacias)):
                            Juego.set_bandera_bot(Casillas_vacias[i])
                            
                        Cambio = 1

                    elif int(casilla.Caracter)-len(Banderas) == 0:
                        for i in range(len(Casillas_vacias)):
                            Juego.Cambiar_valor(Casillas_vacias[i].Fila, Casillas_vacias[i].Columna)

                        Cambio = 1

                    
                    

            if Cambio == 1:
                return 0
        if Cambio == 0:
            Resultado = self.Metodo2(Bordes)
            return Resultado
            

    def Metodo2(self, Bordes):
        
        Casillas_vacias=[]
        Casillas_vistas = []
        Banderas = []
        Valor = 10 #Pongo 10 como valor base ya que no puede ser en el juego
        Elegido = []
            
        for fila in self.Mapa_bot:
            for casilla in fila:
                Banderas = []
                if casilla in Bordes:
                    for i in range(-1,2):
                        for j in range(-1,2):
                            if casilla.Fila+i < 0 or casilla.Fila+i > len(fila)-1:
                                continue
                            elif casilla.Columna+j < 0 or casilla.Columna+j > len(fila)-1:
                                continue
                            elif self.Mapa_bot[casilla.Fila+i][casilla.Columna+j].Caracter == self.Settings.CaracterCasillasVacias:
                                
                                Casillas_vacias.append(self.Mapa_bot[casilla.Fila+i][casilla.Columna+j])

                            elif self.Mapa_bot[casilla.Fila+i][casilla.Columna+j].Caracter == Casilla.Caracter_bandera:
                                Banderas.append(self.Mapa_bot[casilla.Fila+i][casilla.Columna+j])
        
                while len(Casillas_vacias) != 0:
                    Casillas_vacias[0].Valor = Casillas_vacias[0].Valor+int(casilla.Caracter)-len(Banderas)
                    if Casillas_vacias[0] in Casillas_vistas:
                        Casillas_vacias.pop(0)

                    else:
                        Casillas_vistas.append(Casillas_vacias[0])
                        Casillas_vacias.pop(0)

        for i in range(len(Casillas_vistas)):
            
            if Casillas_vistas[i].Valor < Valor:
                Valor = Casillas_vistas[i].Valor
                Elegido = [Casillas_vistas[i]]
            else:
                continue
        


        for i in range(len(Casillas_vistas)):
            Casillas_vistas[i].Valor = 0

        if Elegido[0].Bomba == 1:
            Juego.Vista_tablero(1)
            return(1)

        else:
            Juego.Cambiar_valor(Elegido[0].Fila, Elegido[0].Columna)
            return(0)
    
            

                        



                        
                        






        

Mapa = Configuracion()




while True:
    #Menú principal
    print("""\n 
    Escribe alguna de estas respuestas:
        1. Consultas
        2. Configuración
        3. Comenzar juego
        4. Salir
     \n""")
    respuesta = input(">> ")

    #Consultas
    if respuesta == "1" or respuesta.title() == "Consultas":

        print("""\n 
        Escribe alguna de estas respuestas:
              1. Consultar numero de bombas
              2. Consultar numero de casillas
              3. Consultar Caracter para casillas vacias
         \n""")
        
        respuesta = input(">> ")


        if respuesta.title() == "Consultar numero maximo de bombas" or respuesta == "1":
            print(Mapa.get_NumeroBombas())

        elif respuesta.title() == "Consultar numero de casillas" or respuesta == "2":
            print(Mapa.NumeroCasillas)

        elif respuesta.title() == "Consultar caracter para casillas vacias" or respuesta == "3":
            print(Mapa.get_CaracterCasillasVacias())

        
    
    #Configuración
    elif respuesta == "2" or respuesta.title() == "Configuración":

        print("""\n 
            Escribe alguna de estas respuestas:
                1. Configurar numero de bombas
                2. Configurar numero de casillas
                3. Configurar caracter (skin) de las casillas vacias
        \n""")
        
        respuesta = input(">> ")
    
        if respuesta.title() == "Configurar numero maximo de bombas" or respuesta == "1":
            print("¿Cuantas bombas quieres en el tablero?")
            respuesta = input(">>")
            try:
                respuesta =int(respuesta)
                Mapa.set_NumeroBombas(respuesta)

            except:
                print("El programa no puede leer lo otorgado")

        elif respuesta.title() == "Configurar numero de casillas"  or respuesta == "2":
            print("¿De cuantas casillas quieres el tablero?")
            respuesta = input(">> ")
            try:
                respuesta = int(respuesta)
                Mapa.set_NumeroCasillas(respuesta)

            except:
                print("El programa no puede leer lo otorgado")
                
                

        elif respuesta.title() == "Configurar caracter (skin) de las casillas vacias" or respuesta == "3":
            print("Dime por que caracter quieres sustituir el caracter actual de las casillas vacias")
            respuesta = input(">> ")
            Mapa.set_CaracterCasillasVacias(respuesta)
    

    #Partida

    elif respuesta.title() == "Comezar Juego" or respuesta == "3":
        Juego = Partida()
        Juego.Partida_empezada()


    #Salir
    elif respuesta.title() == "Salir" or respuesta == "4":
        print("Cerrando juego...")
        break


    elif respuesta == "r":
        pass
