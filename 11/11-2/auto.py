class Auto:

        
    def __init__(self,rekisteritunnus,huippunopeus,nopeus=0,matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka
    def Kiihdytä(self,numero):
        self.nopeus += numero
        #huippu = self.huippunopeus.split(" ")
        #huippu = huippu[0]
        huippu = self.huippunopeus
        int(self.nopeus)
        if self.nopeus >= 0 and self.nopeus < huippu:
            return(self.nopeus)
        if self.nopeus > huippu:
            self.nopeus = huippu
            return(self.nopeus)
        else:
            self.nopeus = 0
            return(self.nopeus)
    

    def kulje(self, tunti):
        int(tunti)
        self.matka += self.nopeus * tunti
        self.matka=int(self.matka)
        return(self.matka)
    
class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akku, nopeus=0, matka=0):
        self.akku = akku
        self.nopeus = nopeus
        self.matka = matka
        super().__init__(rekisteritunnus,huippunopeus)
    

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankki, nopeus=0,matka=0):
        self.akku = tankki
        super().__init__(rekisteritunnus,huippunopeus,nopeus,matka)