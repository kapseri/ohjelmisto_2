import random
class Auto:

        
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
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


    def __str__(self):
        return "\nRekkari: " + self.rekisteritunnus + "\nNopeus: " + self.huippunopeus


class Kilpailu:
    def __init__(self,nimi,pituus,automaara):
        self.nimi = nimi
        self.pituus = pituus
        self.automaara = automaara
        self.autot = []
        num = 1
        for x in range(automaara+1):
            rek = (f"ABC-{num}")
            nopeus = random.randrange(100,200)
            nopeus = str(nopeus)
            autox = Auto(rek,nopeus)
            num += 1
            self.autot.append(autox)
    def tunti_kuluu(self,x):
        u=0
        for x in range (len(self.autot)):
            kiihy = random.randrange(-10,15)
            if u == 10:
                u = 0
            self.autot[u].Kiihdytä(kiihy)
            self.autot[u].kulje(x)
            u +=1
    def tulosta_tilanne(self):
        y = 0
        numb = 1
        for x in range(len(self.autot)):

            print("\nAuto",numb," ┃ Rekkari:", self.autot[y].rekisteritunnus , " ┃ Huippunopeus:" , self.autot[y].huippunopeus ,"km/h", " ┃ Nopeus nyt:", self.autot[y].nopeus ,"km/h", " ┃ Matka kuljettu:" , self.autot[y].matka,"km")
            y +=1
            numb +=1
            if numb == len(self.autot):
                break
    def kilpailu_ohi(self):
        u = 0
        for x in range(len(self.autot)):
            if self.autot[u].matka >= self.pituus:
                return True
            u +=1




##Pääohjelma
kisa = Kilpailu("kisa",8000,10)
while True:
    kisa.tunti_kuluu(10)
    kisa.tulosta_tilanne()
    if kisa.kilpailu_ohi()==True:
        break
kisa.tulosta_tilanne()