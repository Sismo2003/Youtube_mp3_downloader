from colorama import Fore, Back, Style, init
from pyfiglet import Figlet
import pyfiglet as pf
import time 
from termcolor import colored, cprint
import os
from pytube import YouTube 

# La funcion init es parte de colorama el parametro "autoreset = True" lo utilizamos para que
# Cuando usemos las funciones Fore, Back , Style se resetie y no tengamos que hacerlo manual mente
# Con el comando (funcion).Reset + (Nuevo color) + ("texto") 
init(autoreset=True)





# Funcion " Waiting_time() "la utilizamos para una pantalla de espera
# Con esta funcion hacemos que al momento de pasar de una funcion a otra nos de una mini pantalla
# De espera con el fin de que el programa no vaya tan rapido y se vea las transiciones muy rapidas
# Podemos modificar el tiempo de espera dentro de la iteracion del "For" en la linea del "time.sleep(...)"
# El parametro aqui es un entero que significa segundos de espera en este caso es cada 0.3 segundos cada iteracion
def waiting_time():
    text = colored(Fore.LIGHTMAGENTA_EX + "Cargando", attrs=["bold","blink"])
    print(text, end=" ")
    for i in range(0,10):
        print(". ", end=" ")
        time.sleep(.3)
    return 0


# En esta funcion se utiliza para borrar la terminal dependiendo de que siste operativo utilices
# En mi caso utilizo mac entonces comento la funcion para windows 
# En el caso donde utilices cualquier distribucion de linux basta con dejar la funcion " os.system("clear") " que es igual a la mac
# Si utlizas Windows solo comenta la funcion de mac/linux y descomenta la de windows
def clear():
    os.system("clear") # mac / linux:
    #os.system("cls") # windows



def mp3():
    figura_1 = (pf.figlet_format("ILEGAL"))
    print (colored(Fore.RED + figura_1 , attrs=[ "blink"]))
    time.sleep(.5)
    clear()
    print(Fore.YELLOW+ Back.BLUE + "♬♬♬♬♬♬♬♬  Descarga de archivo MP3      
    ♬♬♬♬♬♬♬♬\n" )
    figura_2 = (pf.figlet_format("               MP3"))#♬♬♬
    print (colored(Fore.BLUE + figura_2 , attrs=[ "blink", "bold"]))
    print(Fore.GREEN  + Style.BRIGHT+ Style.DIM + """
            Ingresa el Link: 
    """)
    try:
        youtube_link = input(YouTube(">>> "))
        client_video = youtube_link.streams.first()
    except:
        print(""""
            Algo salio mal :/""")
        print(""" 
            Quieres devolverte al menu?""")
        print(Fore.WHITE + "1." +Fore.RESET +  Fore.LIGHTMAGENTA_EX + "Si, por fa ")
        print(Fore.WHITE + "2." +Fore.RESET +  Fore.LIGHTMAGENTA_EX + "No, crack")
        client_answer = input(">>> ")
        if(client_answer == 1 ):
            return start();
        else:
            return 0;


    print(f"El Nombre de la cancion es: {client_video.title}")
    print("""
            Es correcto?
        """)
    print(Fore.WHITE + "1." + Fore.RESET + Fore.BLUE + f"Si, el nombre de la cancion es {client_video.title}")
    print(Fore.WHITE + "2." +Fore.RESET + Fore.BLUE + f"No, mala copeaste mucho...")
    client_answer = input(">>> ")
    if(client_answer == 1):
        client_video.download('~/Desktop')
    else:
        return start();
    try:
        link = YouTube(input(">> "))
        root = link.streams.first()
        
        
    except:
        print("LINK no valido")
        waiting_time()
        start()
    print("Descargando")
    

def sos ():
    clear();
    print(Fore.RED + """
        Estas en la funcion de emergencia.
    """)
    print(Fore.LIGHTMAGENTA_EX+ """ 
        Si llegaste aqui es por que algo salio mal.
        Que hiciste? no se. Pero petaste el programa.
    """)
    print(Fore.RED + """ 
        Si PETO.
    """)
    print(Fore.YELLOW + """ 
            Pero no te preocupes para eso existe esta Funcion.
            Te dare la opción de salir del programa.
    """)
    print(Fore.WHITE + "Presiona 1." + Fore.RESET + Fore.BLUE + " Volver al Menu. ")
    print(Fore.WHITE + "Presiona 2." +  Fore.RESET + Fore.BLUE + " Para salir del programa.")
    try:
        client_op = int(input(">> ") )
    except:
        print(pf.figlet_format("TE CALENTASTE"))
        print(Fore.RESET+Fore.RED + "MALA COPEASTE MUY MALLLLLL")
        print("Saldremos del programa...");
        return 0;
    if(client_op == 1):
        waiting_time();
        clear();
        return start();
    else:
        return 0;
    

def start ():
    clear()
    print(pf.figlet_format("            BIENVENIDOS"))

    print(Fore.RED +"""
       :) Estas a punto de descargar la cancion que mas te gusta :)
    """)

    print(Fore.RESET + Fore.LIGHTMAGENTA_EX + """
    ***  Recuerdad que para descagar la cancion de tus gustos debes de 
       Ingresar el Link de la cancion de youtube que deseas descargar...  ***\n
    """)
    
    print(colored (Fore.RESET  + Fore.YELLOW + """
                    ###########  IMPORTANTE ############               """, attrs=[ "blink"]))
     
    print(colored( """ 

        Para Ingresar la opcion deseada solo tecle el numero de la opcion
              en el caso donde desee salirse del programa tecle el numero "9"
    
    """,attrs=[ "blink"]))


    print( Style.BRIGHT +Fore.YELLOW + """
    Ingrese la opcion de descagar del video 
    """)

    print(Fore.WHITE + "1. " + Fore.GREEN + "Descargar solo el MP3"+ Fore.RESET + Fore.LIGHTCYAN_EX + "   COLD COLD COLD\n")
    print(Fore.WHITE + "2. " + Fore.GREEN + "Descargar El video + Audio" + Fore.RESET + Fore.LIGHTCYAN_EX + "   COLD COLD COLD\n")
    print(Fore.WHITE + "3. " + Fore.GREEN + "Configuracion personaliza" +  Fore.RESET + Fore.RED + "   HOT HOT HOT HOT\n")
   
    try:
        client_op = int(input(">> ") )
    except:
        print(pf.figlet_format("TE CALENTASTE"))
        print(Fore.RESET+Fore.RED + "MALA COPEASTE MUY MALLLLLL")



    if(client_op == 1):
        waiting_time()
        clear()
        mp3();
        print("GRACIAS POR ESCOJERNOS.....")
        print("Saliendo del programa")
        for i in range(0,10):
            print(". ", end=" ")
            time.sleep(.3)
        print("\n")
        clear()
         



sos();






