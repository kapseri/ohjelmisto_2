from julkaisu import Julkaisu 

class Kirja(Julkaisu):
    def __init__(self, nimi, sivut, kirjailija):
        self.sivut = sivut
        self.kirjailija = kirjailija
        super().__init__(nimi)

    def print_info(self):
        print(f"Julkaisun nimi on {self.nimi} Sivumäärä on {self.sivut} ja kirjailija on {self.kirjailija}")