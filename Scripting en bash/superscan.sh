#!/bin/bash
#
# Ejemplo de Menu en BASH
#
date
    echo "||"
    echo "||===========================||"
    echo "||   Menu Principal          ||"
    echo "||===========================||"
    echo "||I. NetDiscover"
    echo "||II. Portscanv1"
    echo "||III. Welcome"
    echo "||IV. Exit"
    echo "||"
read -p "Opción  [ 1 - 4 ] " c
case $c in
        1) /home/hmstudent/Desktop/ejercicios/Practica06/netdiscover.sh;;
        2) /home/hmstudent/Desktop/ejercicios/Practica06/Portscanv1.sh;;
        3) /home/hmstudent/Desktop/ejercicios/Practica06/welcome.sh;;
        4) echo "Bye!"; exit 0;;
esac
