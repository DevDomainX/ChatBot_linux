#!/usr/bin/env python3
import os as x
import sys
from colorama import init, Fore, Style, Back
init()


title = Fore.LIGHTCYAN_EX+Style.BRIGHT+'''\nChatBot: \n
Created by: Hans Saldias

by: 1LugarParaProgramar

Date: 06 octubre 2023


Script: ChatBot Comandos linux

Help use: -h

More 40 command linux

\n\n'''
print(title)
print("\nChatBot: Hola soy tu asistente virtual para ingresar visite 1LugarParaProgramar o insert password\n\n")
pwd = input("\nChatBot insert passwords: ")
if pwd == "1LugarParaProgramar":
    pass
else:
    print("visite 1LugraParaProgramar y pida la contrasena en los comentarios\ncreated by: Hans Saldias")
    sys.exit()


cont = 0
pre = int(input("\nChatBot cuantas preguntas va a realizar: "))    
while cont < pre:
    cont += 1
    print("\n\nChat Bot Linux Commnd\ncomandos vacicos\nCreated by: Hans saldias\n\n")
    text = input("\nChatBot (-h): ").lower()

    try:

        if 'ls' in text:
            x.system("clear")
            print("\nChatBot: {} este comando es para listar los archivos de un directorio actual o donde estamos (ponerlos en lista)".format(text))
        if 'mv' in text:
            x.system("clear")
            print("\nChatBot: {} Este comando es para mover un archivo o carpeta de un lugar a otro eje: (mv carpeta1 $Home) esto moveria la carpeta1 a el Home".format(text))
        if "rm" in text:
            x.system("clear")
            print("\nChatBot: {} este comando es para eliminar una archivo o imagen lo que sea para eliminar un directorio se nesesita otro comando porque es un directorio (rm archivo.txt)".format(text))
        if "rm -r" in text:
            x.system("clear")
            print("\nChatBot: {} este comando sirve para eliminar directorios ya que pide permiso generalmente de superusuario".format(text))
        if "cat" in text:
            x.system("clear")
            print("\nChatBot: {} este comando permite ver el contenido de un echivo sin poder editar solo mirarlo (cat archivo.txt)".format(text))
        if 'play' in text:
            x.system("clear")
            print("\nChatBot: {} este archivo permite reproducir sonidos o musica (play sound.mp3)".format(text))
        if "cd" in text:
            x.system("clear")
            print("\nChatBot: {} este comando permite entrar a la carpeta que pongamos despues del comando (cd $home) entra ala carpeta Home".format(text))
        if "mkdir" in text:
            x.system("clear")
            print("\nChatBot: {} este comando es para crear carpetas (mkdir Script) crea la carpeta llamada script\n Si son con dos palabras separadas (mkdir 'script carpeta') se crea script carpeta".format(text))
        if 'exit' in text:
            x.system("clear")
            print("\nChatBot: {} este comando es para salir de la cmd los cual se repite 2 veces para salir de todo".format(text))
        if 'apt update' in text:
            x.system("clear")
            print("\nChatBot: {} este comando es para (ACTUALIZAR) los repositorios que ya estan intalados".format(text))
        if 'apt upgrade' in text:
            x.system("clear")
            print("\nChatBot: {} este comando es para descargar todas las actualizaciones de los paquetes de cambios que se han hecho".format(text))
        if 'pkg install' in text:
            x.system("clear")
            print("\nChatBot: {} este comando es para instalar paquetes (pkg install python3)".format(text))
        if 'git' in text:
            x.system("clear")
            print("\nChatBot: {} este paquete se esesita para poder clonar repositorios de github (pkg install git)".format(text))
        if 'uname' in text:
            x.system("clear")
            print("\nChatBot: {} este comando muestra la informacion del sistema operativo".format(text))
        if 'ifconfig' in text:
            x.system("clear")
            print("te comando muestra la ip de pc y la red de enmascaramiento de esta")
        if 'neofetch' in text:
            x.system("clear")
            print("\nChatBot: {} este comando muestra la informacion sobre el sistema operativo y el hardware ".format(text))
        if 'find' in text:
            x.system("clear")
            print("\nChatBot: {} este comando busca archivos que siguen un patron".format(text))
        if 'alias' in text:
            x.system("clear")
            print("\nChatBot: {} este comando sirve para darle un alias temporal a una serie de comandos".format(text))
        if 'unalias' in text:
            x.system("clear")
            print("\nChatBot: {} este comando permite eliminar una alias de una serie de comandos".format(text))
        if 'pwd' in text:
            x.system("clear")
            print("\nChatBot: {} este comando permite ver la ruta desde donde estamos".format(text))
        if "cd .." in text:
            x.system("clear")
            print("\nChatBot: {} este comando permite volver atras una carpeta desde donde estamos".format(text))
        if 'cp' in text:
            x.system("clear")
            print("\nChatBot: {} este comando permite copiar el archivo que le damos asta otro directorio o ruta ".format(text))
        if 'man' in text:
            x.system("clear")
            print("\nChatBot: {} este comando permite mostrar el manual del comando despues de man eje:(man mkdir)".format(text))
        if 'chmod' in text:
            x.system("clear")
            print("\nChatBot: {} este comando es para  dar o quitar permisos de lectura (r) escritura (w) ejecucion (x)".format(text))
        if './' in text:
            x.system("clear")
            print("\nChatBot: {} este comando permite ejecutar archivos eje: ./script.py".format(text))
        if 'sudo su' in text:
            x.system("clear")
            print("\nChatBot: {} este comando sirve para poner el modo super usuario o root".format(text))
        if 'shutdown' in text:
            x.system("clear")
            print("\nChatBot: {} este comando es para apagar la maquina virtual que estamos usando igual que para reiniciarla".format(text))
        if "unzip" in text:
            x.system("clear")
            print("\nChatBot: {} este comando permite extraer los archivos de un archivo (unzip archivo.zip)".format(text))
        if 'echo' in text:
            x.system("clear")
            print("\nChatBot: {} este comando permite imprimir texto en pantalla de la cmd donde estamos".format(text))
        if 'help' in text:
            x.system("clear")
            print("\nChatBot: {} este comando es para ver o pedir ayuda de los comandos que no conocemos".format(text))
        if 'ping' in  text:
            x.system("clear")
            print("\nChatBot: {} este comando es para poder ver la conectividad en ese momento o aser un ping en una ip si le das una".format(text))
        if 'nano' in text:
            x.system("clear")
            print("\nChatBot: {} este comando es para abrir el editor de codigo nano eje: nano script.py".format(text))
        if 'vim' in text:
            x.system("clear")
            print("\nChatBot: {} este comando es para abrir el editor de codigo vim similar a nano".format(text))
        if 'history' in text:
            x.system("clear")
            print("\nChatBot: {} este comando es para ver el historial de los comandos usados en la cmd".format(text))
        if 'passwd' in text:
            x.system("clear")
            print("\nChatBot: {} este comando permite cambiar las contrasena de las cuentas de usuarios".format(text))
        if 'creditos' in text:
            x.system("clear")
            print("\nChatBot: gracias a 1LugarParaProgramar")
        if 'creador' in text:
            x.system("clear")
            print("\nChatBot: Created by: Hans Saldias")
        if "-h" in text:
            x.system("clear")
            print("\nChatBot: ls, mv, cd, chmod, git, etc\n ;)")

            

    except ValueError:
        print("comando no comprendido, intente nuevamente")

