# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 30/01/2026
# Versió: 1
#
# Descripció: Crea una classe Figura amb un mètode area() que només imprimeixi "Àrea no definida".
# Crea dues subclasses:
# Quadrat amb atribut costat i mètode area() que calculi l'àrea.
# Cercle amb atribut radi i mètode area() que calculi l’àrea (usa math.pi).
# Especificacions d'Entrada: Crea una instància de Treballador i prova els mètodes.

import math

class Figura:
    def area(self):
        print("Area no definida")

class Quadrat(Figura):
    def __init__(self, costat):
        self.costat = costat

    def area(self):
        resultat = self.costat * self.costat
        print(f"L'àrea del quadrat és {resultat}")

class Cercle(Figura):
    def __init__(self, radi):
        self.radi = radi

    def area(self):
        resultat = math.pi * (self.radi ** 2)
        print(f"L'àrea del cercle és {resultat}")
