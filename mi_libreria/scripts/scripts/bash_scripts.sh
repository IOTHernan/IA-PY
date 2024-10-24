#!/bin/bash

# bash_scripts.sh

function script1 {
    echo "Este es el Script 1"
}

function script2 {
    echo "Este es el Script 2"
}

function script3 {
    echo "Este es el Script 3"
}

case "$1" in
    "script1") script1 ;;
    "script2") script2 ;;
    "script3") script3 ;;
    *) echo "Script no encontrado" ;;
esac
