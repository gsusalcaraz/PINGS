import os
import platform
import subprocess
import time
from datetime import datetime

def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ['ping', param, '1', host]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) == 0

def clear_console():
    os.system("cls" if platform.system().lower() == "windows" else "clear")

def save_to_log(message):
    with open("ping_log.txt", "a") as file:
        file.write(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - {message}\n")

def main():
    server = ""
    google = "8.8.8.8"
    clear_console()
    print("REALIZANDO PING A LA DNS DE GOOGLE + SERVER")
    print("Inicio del script: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    while True:
        if not ping(server):
            current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            message = f"No hay conexión con {server} - {current_time}"
            print(message)
            save_to_log(message)
        if not ping(google):
            current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            message = f"No hay conexión de INTERNET {google} - {current_time}"
            print(message)
            save_to_log(message)        
        else:
           print(".", end="", flush=True)  # Muestra un punto por cada ping exitoso
        time.sleep(1)

if __name__ == '__main__':
    main()
