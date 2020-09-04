from netmiko import ConnectHandler
from equipos import *
from paramiko.ssh_exception import SSHException

pregunta = input("ingrese show command para analizar en la red: ")

try:
    Device1 = ConnectHandler(**Equipo1)
    output = Device1.send_command(pregunta)
    print("========================================================")
    print("Results from command output to host: ",Equipo1["host"])
    print(output)
    print("========================================================")
    print()
except Exception as ex:
    print(ex,Equipo1["host"])
    print("========================================================")


try: 
    Device2 = ConnectHandler(**Equipo2)
    output2 = Device2.send_command(pregunta)
    print("========================================================")
    print("Results from command output to host: ",Equipo2["host"])
    print(output2)
    print("========================================================")
except Exception:
    print('SSH is not enabled for this device.',Equipo2["host"])
    print("========================================================")
    print()

    
try:    
    Device3 = ConnectHandler(**Equipo3)
    output3 = Device3.send_command(pregunta)
    print("========================================================")
    print("Results from command output to host: ",Equipo3["host"])
    print(output3)
    print("========================================================")
    print()
except Exception:
    print('SSH is not enabled for this device.',Equipo3["host"])
    print("========================================================")
    print()


try:    
    Device4 = ConnectHandler(**Equipo4)
    output4 = Device4.send_command(pregunta)
    print("========================================================")
    print("Results from command output to host: ",Equipo4["host"])
    print(output4)
    print("========================================================")
    print()
except Exception:
    print('SSH is not enabled for this device.',Equipo4["host"])
    print("========================================================")
    print()

try:    
    Device5 = ConnectHandler(**Equipo5)
    output5 = Device5.send_command(pregunta)
    print("========================================================")
    print("Results from command output to host: ",Equipo5["host"])
    print(output5)
    print("========================================================")
    print()
except Exception:
    print('SSH is not enabled for this device.',Equipo5["host"])
    print("========================================================")
    print()
