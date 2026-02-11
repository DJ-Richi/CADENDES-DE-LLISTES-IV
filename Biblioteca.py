# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 11/02/2026
# Versió: 1
#
# Descripció: Crea una classe Llibre amb atributs titol i autor, i un mètode mostrar_info().
# Crea dues subclasses:
# LlibrePaper amb atribut n_pàgines
# LlibreDigital amb atribut format (PDF, ePub...)
# Especificacions d'Entrada: LlibrePaper amb atribut n_pàgines LlibreDigital amb atribut format (PDF, ePub...)

class Llibre:
    def __init__(self, titol, autor):
        self.titol = titol
        self.autor = autor

    def mostrar_info(self):
        print("Àrea no definida")

class LlibrePaper(Llibre):
    def __init__(self, titol, autor, numero_pagines):
        super().__init__(titol, autor)
        self.numero_pagines = numero_pagines

    def mostrar_info(self):
        print(f"Llibre en paper: '{self.titol}' de {self.autor}, {self.numero_pagines} pàgines.")

class LlibrePaper(Llibre):
    def __init__(self, titol, autor, numero_pagines):
        super().__init__(titol, autor)
        self.numero_pagines = numero_pagines

    def mostrar_info(self):
        print(f"Llibre en paper: '{self.titol}' de {self.autor}, {self.numero_pagines} pàgines.")