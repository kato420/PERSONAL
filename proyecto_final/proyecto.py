import datetime
from funciones import ver_numero,print_matrix,juego,lista_de_tiempos,lista_de_registros,lista_jugadores,lista_ganadores,diccionario_jugadores,diccionario_njuegos,juegos_realizados
import colorama
from colorama import Fore
colorama.init(autoreset=True)

while True:
    #Para que se actualice el valor de la lista
    print(Fore.YELLOW+"Juego 4 en linea")
    print(Fore.RED+"1 "+Fore.WHITE+"Comenzar Juego")
    print(Fore.BLUE+"2 "+Fore.WHITE+"Jugar vs computadora")
    print(Fore.GREEN+"3 "+Fore.WHITE+"Juegos realizados")
    print(Fore.YELLOW+"4 "+Fore.WHITE+"Salir")
    opcion=input(Fore.MAGENTA+"Opcion: ")
    while opcion!="1" and opcion!="2" and opcion!="3" and opcion!="4":
        print(Fore.GREEN+"INGRESE UN NÚMERO VÁLIDO"+Fore.WHITE+" :" ,end="")
        opcion=input("")
    #####INICIO DEL JUEGO
    if opcion=="1":
        print()
        print(Fore.RED+"COMENZAR JUEGO"+Fore.WHITE+":")
        print("Nombre jugador"+Fore.RED+" 1: ",end="")
        j1=input("")
        if j1 not in diccionario_jugadores:
            diccionario_jugadores[j1]=0
            diccionario_njuegos[j1]=0 #para contar los numeros de veces que ha jugado
        lista_jugadores.append(j1)
        print("Nombre jugador"+Fore.BLUE+" 2: ",end="")
        j2=input("")
        if j2 not in diccionario_jugadores:
            diccionario_jugadores[j2]=0
            diccionario_njuegos[j2]=0 #para contar los numeros de veces que ha jugado
        lista_jugadores.append(j2)
        matriz_guardada=juego(j1,j2)
        #region tiempo
        tiempo_1=datetime.datetime.now().time() # nos da la hora actual
        cadena_tiempo_1=str(tiempo_1) # convertimos a string par
        tiempo_formateado_1=cadena_tiempo_1.split(".")[0]
        fecha_1=datetime.date.today() # nos da la fecha actual
        f_t=f"{tiempo_formateado_1} {fecha_1}"
        lista_de_tiempos.append(f_t)
        #endregion
        juegos_realizados+=1 #nos ayuda para verificar la opción 2
        #print(matriz_guardada)
        lista_de_registros.append(matriz_guardada)
    #####VERIFICACION DE JUEGOS
    elif opcion=="3":
        print()
        if len(lista_de_registros)==0:
            print(Fore.GREEN+"No se registran juegos")
            print()
        else:
            print(Fore.GREEN+"Se mostrarán los registros: ")
            print()
            l_titutlo=[" Jugadores"," FechaHora"," Ganador"]
            print(f"{l_titutlo[0].ljust(21)}\t{l_titutlo[1].ljust(21)}\t{l_titutlo[2]}")
            mini_c=0 #se usa el minicontador para indicar los jugadores
            lista_vacia=" "
            for x in range(juegos_realizados):
                print(Fore.YELLOW+str(x+1)+". " + Fore.RED + str(lista_jugadores[x+mini_c]) + Fore.WHITE+" vs " + Fore.BLUE + str(lista_jugadores[x+mini_c+1])+f"\t{lista_vacia.ljust(1)}"+ Fore.WHITE + f" {lista_de_tiempos[x]}" +f"\t{lista_vacia.ljust(1)}" + f" {lista_ganadores[x]}")
                mini_c+=1
            #Nueva implementación - Parte 2 proyecto
            print()
            print("Jugador\t Cant. Juegos\tGanadas") #Importante para el orden
            for x in diccionario_jugadores:
                print(f"{x.ljust(10)}\t{diccionario_njuegos[x]}\t{diccionario_jugadores[x]}") #Importante para el orden
            a=input("Qué juego desea verificar? ")
            a=ver_numero(a)
            while len(lista_de_registros)<a and a!=0: #mientras que esté fuera del rango
                a=input("Qué juego quiere verificar?")
                a=ver_numero(a)
            print_matrix(lista_de_registros[a-1])
            print()
    
    elif opcion=="2":
        print("Inicia el juego con la computadora")
        print() 
    elif opcion=="4":
        break
    else:
        print("Opción no válida. Elige una opción válida")
print(Fore.GREEN+"Gracias por jugar")
