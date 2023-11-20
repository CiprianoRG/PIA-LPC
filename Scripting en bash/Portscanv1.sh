#!/bin/bash
#Script netdiscover.sh
#16/09/2023 Luis Cipriano Rodriguez Gonzalez
direccion_ip=$1
puertos="20 21 22 23 25 50 51 53 110 119 135 136 137 138 143 161 162 389 443 445 636 1025 1443 3389 5985 5986 8080 10000"
# Verificando que el parámetro ip no venga vacío
if [ $# -eq 0 ]; then
    echo "Modo de uso: $0 <dirección IP>"
    exit 1
fi

# Bucle for para cada puerto en $puertos
for port in $puertos; do
    timeout 1 bash -c "echo > /dev/tcp/$direccion_ip/$port" > /dev/null 2>&1 &&
    echo "$direccion_ip:$port is open" ||
    echo "$direccion_ip:$port is closed"
done
