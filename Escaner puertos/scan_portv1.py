#LUIS CIPRIANO RODRIGUEZ GONZALEZ
#1753573
#Parte 1
import sys
from socket import *
#Parte 2
#Primer argumento se guarda en host
host=sys.argv[1]
#Segundo argumento se guarda en portstrs
portstrs=sys.argv[2].split('-')

#Parte 3
start_port= int(portstrs[0])
end_port=int(portstrs[1])

#Parte 4
#de host se procesa la funcion gethostbyname para obtener la direccion ip
#se crea una lista para guardar los puertos abiertos
target_ip = gethostbyname(host)
opened_ports=[]

#Parte 5
#se crea un for para probar con sockets los puertos abiertos en el rango dado
for port in range(start_port,end_port):
    sock= socket(AF_INET,SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        opened_ports.append(port)

#Parte 6
print("Opened Ports:")
for i in opened_ports:
    print(i)