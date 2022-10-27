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

#Pääohjelma
auto1 = Auto("ABC-123","142 km/h")
auto1.Kiihdytä(30)
auto1.Kiihdytä(70)
auto1.Kiihdytä(50)
print(auto1.nopeus,"km/h")
auto1.Kiihdytä(-200)
print(auto1.nopeus,"km/h")