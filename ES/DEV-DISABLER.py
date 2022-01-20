from multiprocessing.connection import wait
import os
username = os.getlogin()
print('DEV-DISABLER: Creado por Robichani6-1 (Transportes Chancleta)')
yes = ["sí", "si", "s", "y", "yes"]
no = ["no", "n"]
response = input("¿Quieres desactivar la cámara 0 y la consola? (S/N)")

def change_values(file):

    values = {
        'uset g_console "1"': 'uset g_console "0"\n',
        'uset g_developer "1"': 'uset g_developer "0"\n',
    }
    with open(file, 'r+') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            for key in values:
                if key in line:
                    lines[i] = values[key]
                    break
    with open(file, 'w') as f:
        f.writelines(lines)
        print('[+] La cámara 0 y la consola se han deshabilitado con éxito.')
         
while True:
  if response.lower() in yes:
    change_values(os.path.join(r"C:\Users\\"+str(username)+"\Documents\Euro Truck Simulator 2\config.cfg"))
    break
    quit()
  elif response.lower() in no:
    print("[+] El programa se está cerrando ...")
    break
    quit()
  else:
   print("Respuesta inválida, inténtalo de nuevo.")
   response = input("¿Quieres desactivar la cámara 0 y la consola? (S/N)")


    
