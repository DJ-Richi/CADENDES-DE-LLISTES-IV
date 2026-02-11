# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 30/01/2026
# Versió: 1
#
# Descripció: Crea una instància de Cotxe i crida els dos mètodes.
# Crea una classe Persona amb els atributs nom i edat, i un mètode saludar() que imprimeixi "Hola, sóc {nom}".
# Crea una subclasse Treballador que afegeixi un atribut feina i un mètode mostrar_feina() que imprimeixi "Treballo com a {feina}".
# Especificacions d'Entrada: Crea una instància de Treballador i prova els mètodes.

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def saludar(self):
        print(f"Hola, sóc {nom}")


class Treballador(Persona):
    def __init__(self, feina):
        self.feina = feina

    def mostrar_feina():
        print(f"Treballo com a {feina}")
        