#LUIS CIPRIANO RODRIGUEZ GONZALEZ
#1753573
import nmap

#CON EL ARGUMENTO -sU HACEMOS UN ESCANEO UDP, Y DE EL OBTENEMOS INFORMACION COMO LOS PUERTOS ABIERTOS Y EL NOMBRE
def escaneo_udp(host):
    escaner = nmap.PortScanner()
    escaner.scan(host, arguments='-sU')
    print("Resultados del escaneo UDP:")
    for host, resultado in escaner.all_hosts().items():
        print(f"Host: {host}")
        for puerto, info in resultado['udp'].items():
            print(f"Puerto {puerto}: {info['state']} - {info['name']}")

#CON EL ARGUMENTO -p- NOS ASEGURAMOS QUE SE ESCANEAN TODOS LOS PUERTOS, Y CON -sV SE OBTIENE INFORMACION MAS DETALLLADA COMO SUS SERVICIOS Y VERSION
def escaneo_completo(host):
    escaner = nmap.PortScanner()
    escaner.scan(host, arguments='-p- -sV')
    for scanned_host in escaner.all_hosts():
        print(f"Host: {scanned_host}")
        if 'tcp' in escaner[scanned_host]:
            for puerto, info in escaner[scanned_host]['tcp'].items():
                print(f"Puerto {puerto}: {info.get('state', 'Desconocido')} - {info.get('name', 'Desconocido')} - {info.get('product', 'Desconocido')} {info.get('version', 'Desconocido')}")

# -O NOS AYUDA A SACAR EL SISTEMA OPERATIVO DEL OBJETIVO
def deteccion_sistema_operativo(host):
    escaner = nmap.PortScanner()
    escaner.scan(host, arguments='-O')
    print(f"Sistema Operativo de {host}: {escaner[host]['osmatch'][0]['name']}")

# -sn SIRVE PARA HACER UN ESCANEO DE HOSTS PERO SIN HACER UN ESCANEO DE PUERTOS, 
def escaneo_red_con_ping(red):
    escaner = nmap.PortScanner()
    escaner.scan(hosts=red, arguments='-sn')
    for host in escaner.all_hosts():
        print(f"Host: {host} está activo (respondió al ping)")

#FUNCION PARA MOSTRAR EL MENU PRINCIPAL
def menu():
    print("1. Escaneo UDP")
    print("2. Escaneo Completo")
    print("3. Detección de Sistema Operativo")
    print("4. Escaneo de Red con Ping")
    print("0. Salir")

#PROGRAMA PRINCIPAL
if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Selecciona una opción (0-4): ")

        if opcion == "0":
            break
        elif opcion == "1":
            host = input("Ingrese la dirección IP del host: ")
            escaneo_udp(host)
        elif opcion == "2":
            host = input("Ingrese la dirección IP del host: ")
            escaneo_completo(host)
        elif opcion == "3":
            host = input("Ingrese la dirección IP del host: ")
            deteccion_sistema_operativo(host)
        elif opcion == "4":
            red = input("Ingrese la dirección de red (por ejemplo, 192.168.1.0/24): ")
            escaneo_red_con_ping(red)
        else:
            print("Opción no válida. Intente de nuevo.")
