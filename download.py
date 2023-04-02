from colorama import Fore, Back, Style, init
from pyfiglet import Figlet
import pyfiglet as pf
import time 
from termcolor import colored, cprint
import os
import pytube 

init(autoreset=True)

 

def clear():
    #mac:
    #os.system("clear")
    os.system("cls")

def mp3():
    figura_1 = (pf.figlet_format("ILEGAL"))
    print (colored(Fore.RED + figura_1 , attrs=[ "blink"]))
    time.sleep(.5)
    clear()
    print(Fore.YELLOW + "♬♬♬♬♬♬♬♬  Descarga de archivo MP3   ♬♬♬♬♬♬♬♬\n" )
    figura_2 = (pf.figlet_format("               MP3"))#♬♬♬
    print (colored(Fore.BLUE + figura_2 , attrs=[ "blink", "bold"]))
    
    print(Fore.GREEN  + Style.BRIGHT+ Style.DIM + """
            Ingresa el Link: 
    """)
    link = input(">> ")

    yt = pytube.YouTube(link)
  
    print(f"Descargando {yt.title}")
   # yt.streams.get_audio_only().download()
    
    return 0;




def start ():
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
        time.sleep(2)
        clear()
        mp3();
    elif(client_op == 2):
        time.sleep(2)
        clear()
        return avi();
    elif(client_op == 3):
        time.sleep(2)
        clear()
        return custom();
    elif(client_op == 4):
        print("GRACIAS POR ESCOJERNOS.....")
        return 0; 


def custom():
    for i in range(0,100):
        print(Fore.RED + "TE CALENTASTE\n")

def avi():
    for i in range(0,10):
        print("calmala\n")
    print("calmalaaaaaaaaaaa")

start()






