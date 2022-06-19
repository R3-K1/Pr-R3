import os
import time

print("""
██████╗░██████╗░░░░░░░██████╗░██████╗░
██╔══██╗██╔══██╗░░░░░░██╔══██╗╚════██╗
██████╔╝██████╔╝█████╗██████╔╝░█████╔╝
██╔═══╝░██╔══██╗╚════╝██╔══██╗░╚═══██╗
██║░░░░░██║░░██║░░░░░░██║░░██║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░░░░░░╚═╝░░╚═╝╚═════╝░""")

time.sleep(2)

print("Hello and welcome to my proyect, lets see what you can do:")

respuesta = input("Select your language: ")

if respuesta == "Español":
    print("Bienvenido, a continuación veras las posibles opciones...")
    time.sleep(2)
    modo = input("1) Wifi-Crack-Win10 by R3 (Beta, probablemente no funcione) \n2) Wifi-Crack \n")
if modo == "1":
    os.system('netsh wlan show profiles')
    wifi = input("Introduce el nombre del Wi-fi: ")
    os.system('netsh wlan show profile ' + wifi +' key=clear')
if modo == "2":
    os.system('git clone https://github.com/davidbombal/red-python-scripts.git')
    print("Acabo de instalarte varias herramientas de gran utilidad, suerte. ")
    time.sleep(2)