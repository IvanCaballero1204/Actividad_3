#!/usr/bin/env python3
from math import pi
import areas

def main():
    print("Hola mundo")
    nombre = input("¿Cual es tu nombre? ")
    print("Hola {}".format(nombre))
    edad = int(input("¿Cuántos años tienes? "))
    print("{} tienes {} años y en un año tendrás {} años".format(nombre, edad, edad + 1))
    area_triangulo = areas.triangulo()
    print("El area de tu triangulo es igual a: {}".format(area_triangulo))
    area_circulo = areas.circulo()
    print("El area de tu circulo es igual a: {}".format(area_circulo))
    area_dona = areas.dona()
    print("El area de tu dona es igual a: {}".format(area_dona))

print("Bienvenido a main")
main()
