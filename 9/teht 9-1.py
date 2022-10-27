class Auto:
    def __init__(self,rekisteritunnus,huippunopeus,nopeusnyt=0,matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeusnyt = nopeusnyt
        self.matka = matka

#Pääohjelma

auto1 = Auto("ABC-123","142 km/h")
print ("Rek tunnus:",auto1.rekisteritunnus,"\nHuippunopeus:", auto1.huippunopeus, "\nTämänhetkinen nopeus:",auto1.nopeusnyt, "\nKuljettu matka:",auto1.matka)