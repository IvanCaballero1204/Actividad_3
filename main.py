#!/usr/bin/env python3
from math import pi

def triangulo():
    base = int(input("Ingresa base del triangulo: "))
    altura = int(input("Ingresa altura del triangulo: "))
    return base * altura / 2

def circulo():
    radio = int(input("Ingresa radio del circulo: "))
    return pi * radio**2

def main():
    print("Hola mundo")
    nombre = input("¿Cual es tu nombre? ")
    print("Hola {}".format(nombre))
    edad = int(input("¿Cuántos años tienes? "))
    print("{} tienes {} años y en un año tendrás {} años".format(nombre, edad, edad + 1))
    area_triangulo = triangulo()
    print("El area de tu triangulo es igual a: {}".format(area_triangulo))
    area_circulo = circulo()
    print("El area de tu circulo es igual a: {}".format(area_circulo))

main()
