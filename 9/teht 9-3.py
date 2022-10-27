class Auto:

        
    def __init__(self,rekisteritunnus,huippunopeus,nopeus=0,matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka
    def Kiihdytä(self,numero):
        self.nopeus += numero
        huippu = self.huippunopeus.split(" ")
        huippu = huippu[0]
        huippu = int(huippu)
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

#Pääohjelma
auto1 = Auto("ABC-123","142 km/h")
auto1.Kiihdytä(20)
auto1.kulje(100)
auto1.Kiihdytä(40)
auto1.kulje(1.5)
print(f"Auto1: {auto1.rekisteritunnus}\nvauhti: {auto1.nopeus}km/h\nmatka: {auto1.matka}km")