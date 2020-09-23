#!/usr/bin/env python3

def main():
    print("Hola mundo")
    nombre = input("¿Cual es tu nombre? ")
    print("Hola {}".format(nombre))
    edad = int(input("¿Cuántos años tienes? "))
    print("{} tienes {} años y en un año tendrás {} años".format(nombre, edad, edad + 1))

main()
