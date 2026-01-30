# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 30/01/2026
# Versió: 1
#
# Descripció: Crea una classe Vehicle amb un atribut marca i un mètode arrencar().
# Especificacions d'Entrada: Crea una subclasse Cotxe que afegeixi un mètode tocar_claxon() que imprimeixi "Pip pip!". Crea una instància de Cotxe i crida els dos mètodes.

class Vehicle:
    def __init__(self, marca):
        self.marca = marca
    
    def arrancar(self):
        print(f"{self.marca}esta arrancant...")

class Cotxe(Vehicle):
    def tocar_claxon(self):
        print("Pip pip!")