#!/usr/bin/env python3
from math import pi

def triangulo():
    base = int(input("Ingrese base del triangulo: "))
    altura = int(input("Ingrese altura del triangulo: "))
    return base * altura /2

def circulo():
    radio = int(input("Ingrese radio del circulo: "))
    return pi * radio**2

def dona():
    radio_externo = int(input("Ingrese radio externo: "))
    radio_interno = int(input("Ingrese radio interno: "))
    return circulo(radio_externo) - circulo(radio_interno)
