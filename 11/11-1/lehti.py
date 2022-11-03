from julkaisu import Julkaisu
class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        self.toimittaja = toimittaja
        super().__init__(nimi)

    def print_info(self):
        print(f"Julkaisun nimi on {self.nimi} Toimittaja on {self.toimittaja}")