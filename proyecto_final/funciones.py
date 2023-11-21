import datetime
import colorama
from colorama import Fore
colorama.init(autoreset=True)

lista_de_tiempos=[]#se guardan los tiempos
lista_de_registros=[] #se guardan las matrices de los juegos
lista_jugadores=[] #se guardan los jugadores
lista_ganadores=[]
diccionario_jugadores={}
diccionario_njuegos={}
#numero_juegos=0
juegos_realizados=0 #indica el numero de juegos realizados

def ver_numero(a=str): # Se crea una verificación para que las entradas sean números
    n=["1","2","3","4","5","6","7"]
    c=0
    for x in n:
        if a==x: #A representa la entrada en texto y x es un numero de la lista
            c+=1
    if c!=0:
        return int(a)
    else:        
        while c==0:
            a=input(Fore.RED+"Ingrese un número válido"+Fore.WHITE+": ")
            for x in n:
                if a==x:
                    c+=1
        return int(a)            
             
# Se define una función para mostrar la matriz
def print_matrix(l=list):
    for x in l:
        for y in x:
            print(y,end=" ")
        print()
    if len(l)!=1: # para evitar errores en la salida de juegos realizados
        print("1 2 3 4 5 6 7")
    return " "

# Se define una funcion para verificar las casillas
def verificar_mov(listita=list):
    ver=0 ## Variable de verificacion
    for x in listita: # Itera en fila
        for y in x: # Itera en columna
            if y!="_": # cuenta espacios no vacíos
                ver+=1
    a=42-ver
    return a

# Se define una verificacion en diagonal 1 para la funcion
def ver_d1(l=list): # Se agrega la lista a verificar como parametro
    a=0 # Indice importante para la validacion de la verificacion
    for y in range(4):
        for x in range(3):
            a1=l[x][y]
            a2=l[x+1][y+1]
            a3=l[x+2][y+2]
            a4=l[x+3][y+3]
            #print(f"Iteracion {y+1}: ",end="")
            #print(f"{a1},{a2},{a3},{a4}")
            if a1==a2==a3==a4 and a1!="_":
                #print("Se ha encontrado un ganador")
                a+=1
                break
        if a==1:
            break
    return a

# Se define una verificacion en diagonal 2 para la funcion
def ver_d2(l=list): # Se agrega la lista a verificar como parametro
    a=0 # Indice importante para la validacion de la verificacion
    for y in range(4):
        #print(y)
        for x in range(3):
            a1=l[x][3+y]
            a2=l[x+1][3+y-1]
            a3=l[x+2][3+y-2]
            a4=l[x+3][3+y-3]
            #print(f"Iteracion {y+1}: ",end="")
            #print(f"{a1},{a2},{a3},{a4}")
            if a1==a2==a3==a4 and a1!="_":
                #print("Se ha encontrado un ganador")
                a+=1
                break
        if a==1:
            break
    return a

# Se define una función para modificar la matriz
def insert_matrix(r=int,c=int,l=list,n=int): # r=fila c=columna l=lista n=contador para cada jugador
    if n%2!=0: #n es un indicador para poder escoger "O" o "X" dependiendo del jugador
        l[r][c-1] =Fore.RED+"X" #En este caso se usa "c-1" para que la entrada directa pueda ser el número indicado
        return l #En este caso l es la matriz donde se guardan los cambios
    else:
        l[r][c-1] =Fore.BLUE+"O"
        return l #En este caso l es la matriz

# Definimos una función para la verificación de columnas
def ver_colv(l=list): # Se agrega la lista a verificar como parametro
    a=0
    for x in range(7):
        for y in range(3):
            a1=l[y][x]
            a2=l[y+1][x]
            a3=l[y+2][x]
            a4=l[y+3][x]
            if a1==a2==a3==a4 and a1!="_":
                #print("Se ha encontrado a un ganador") #ganador v
                a+=1
                break
        if a==1:
            break
    return a

# Definimos una función para la verificación de fila
def ver_colh(l=list): # Se agrega la lista a verificar como parametro
    a=0
    for x in range(6):
        ##print(x)
        for y in range(4):
            a1=l[x][y]
            a2=l[x][y+1]
            a3=l[x][y+2]
            a4=l[x][y+3]
            if a1==a2==a3==a4 and a1!="_":
                #print("Se ha encontrado a un ganador") #ganador h
                a+=1
                break
        if a==1:
            break
    return a

# Se define una funcion para la continuidad del juego:
def juego(j1 = str, j2 = str):
    l= [["_","_","_","_","_","_","_",],
        ["_","_","_","_","_","_","_",],
        ["_","_","_","_","_","_","_",],
        ["_","_","_","_","_","_","_",],
        ["_","_","_","_","_","_","_",],
        ["_","_","_","_","_","_","_",]]
    tiempo=datetime.datetime.now().time() # nos da la hora actual
    cadena_tiempo=str(tiempo) # convertimos a string para poder eliminar los decimales
    tiempo_formateado=cadena_tiempo.split(".")[0]
    fecha=datetime.date.today() # nos da la fecha actual
    print("Juego "+Fore.RED+f"{j1}"+Fore.WHITE+" vs "+Fore.BLUE+f"{j2}"+Fore.WHITE + f" {tiempo_formateado}"+Fore.WHITE+f" {fecha}")
    cancelar=input("-1: Para cancelar ") #cancelar el juego
    if cancelar== "-1":
        mensaje= "-"
        print()
        diccionario_njuegos[j1]+=1
        diccionario_njuegos[j2]+=1
        lista_ganadores.append("Cancelado")
        return mensaje
    else:
        print(print_matrix(l))
        turno = 1 # Indica el turno de cada jugador (1 por defecto)
        row_def = 5 # Indica la fila por defecto (5)
        a=0
        b=0
        c=1
        v1=0
        v2=0
        col_jugador=input(f"{j1} ? ") # Fila del jugador
        col_jugador=ver_numero(col_jugador) # Se verifica la entrada
        while col_jugador<1 or 7<col_jugador:
            col_jugador=int(input(f"{j1} ? "))
        resultado=insert_matrix(row_def,col_jugador,l,turno)
        print_matrix(resultado)
        turno+=1
        while a==0 and b==0 and v1==0 and v2==0 and c!=0:
            row_def=5
            if turno%2!=0: # Si el turno es impar j1
                col_jugador=input(f"{j1} ? ") # col del jugador 
                col_jugador=ver_numero(col_jugador) #se verifica la entrada
                while col_jugador<1 or 7<col_jugador:
                    col_jugador=input(f"{j1} ? ")
                    col_jugador=ver_numero(col_jugador)
                #Al parecer se puede cambiar todo esto por un while
                if resultado[row_def][col_jugador-1]== "_":
                    row_def=5     
                else:
                    while resultado[row_def][col_jugador-1]!= "_": # Importante hubo un error al usar la funcion insert, problemas de indices
                        row_def-=1
                        if row_def<0: ### Verificación vertical
                            col_jugador=int(input(f"{j1} ? "))
                            row_def=5
                resultado=insert_matrix(row_def,col_jugador,resultado,turno)
            else: # Si el turno es par j2
                col_jugador=input(f"{j2} ? ") # col del jugador
                col_jugador=ver_numero(col_jugador)
                while col_jugador<1 or 7<col_jugador:
                    col_jugador=input(f"{j2} ? ")
                    col_jugador=ver_numero(col_jugador) 
                #Al parecer se puede cambiar todo esto por un while
                if resultado[row_def][col_jugador-1]== "_":
                    row_def=5
                else:
                    while resultado[row_def][col_jugador-1]!= "_": #Importante para que no haya error con indice 0
                        row_def-=1
                        if row_def<0: ### Verificación vertical
                            col_jugador=int(input(f"{j2} ? "))
                            row_def=5 #Para que reinicie el contador
                resultado=insert_matrix(row_def,col_jugador,resultado,turno)
            print_matrix(resultado)
            print()
            a=ver_colv(resultado)
            b=ver_colh(resultado)
            v1=ver_d1(resultado)
            v2=ver_d2(resultado)
            c=verificar_mov(resultado)
            turno+=1  ####suma cada iteracion
        if c==0:
            print("Empate!")
            lista_ganadores.append("Empate")
        elif turno%2!=0: 
            print("El jugador " + Fore.BLUE+j2 + Fore.WHITE+ " ha ganado") #se invierte porque el turno suma
            diccionario_jugadores[j2]+=1 #Agregado final diccionario
            lista_ganadores.append(j2)
        else:
            print("El jugador " + Fore.RED+j1 + Fore.WHITE+ " ha ganado")
            diccionario_jugadores[j1]+=1 #Agregado final diccionario
            lista_ganadores.append(j1)
        diccionario_njuegos[j1]+=1
        diccionario_njuegos[j2]+=1
        print()
        return resultado




