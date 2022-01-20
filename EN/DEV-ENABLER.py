from multiprocessing.connection import wait
import os
username = os.getlogin()
print('DEV-ENABLER: By Robichani6-1 (Transportes Chancleta)')
yes = ["sí", "si", "s", "y", "yes"]
no = ["no", "n"]
response = input("Dou yo want activate camera 0 and console? (Y/N)")

def change_values(file):

    values = {
        'uset g_console "0"': 'uset g_console "1"\n',
        'uset g_developer "0"': 'uset g_developer "1"\n',
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
        print('[+] Camera 0 and the console have been successfully activated.')
         
while True:
  if response.lower() in yes:
    change_values(os.path.join(r"C:\Users\\"+str(username)+"\Documents\Euro Truck Simulator 2\config.cfg"))
    break
    quit()
  elif response.lower() in no:
    print("[+] The program is closing...")
    break
    quit()
  else:
   print("Invalid response, try again")
   response = input("Dou yo want activate camera 0 and console? (Y/N)")


    
