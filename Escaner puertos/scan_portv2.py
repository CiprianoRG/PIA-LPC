#LUIS CIPRIANO RODRIGUEZ GONZALEZ
#1753573
#Parte 1
import socket
#Parte 2
def scan(addr,port):
    #creando un objeto socket
    socket_obj=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #Estableciendo el timeout para el objeto
    socket.setdefaulttimeout(1)
    #conexion exitosa devuelve 0, de lo contrario devuelve error
    result =socket_obj.connect_ex((addr,port))
    socket_obj.close()
    return result
#parte 3
ports=[21,22,25,80]

#Parte 4
for i in range(11,15):
    addr="192.168.0.{}".format(i)
    for port in ports:
        result=scan(addr,port)
        if result==0:
            print(addr,port,'OK')
        else:
            print(addr,port,'Failed')