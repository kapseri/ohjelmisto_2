from ast import While
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

num = 1
auto=[]
for x in range(10):
    rek = (f"ABC-{num}")
    nopeus = random.randrange(100,200)
    nopeus = str(nopeus)
    autox = Auto(rek,nopeus)
    num += 1
    auto.append(autox)

u=0
y = 0
numb = 1
#Kisa
while True:
    kiihy = random.randrange(-10,15)
    if u == 10:
        u = 0
    if auto[u].matka < 10000:
        auto[u].Kiihdytä(kiihy)
        auto[u].kulje(1)
    elif auto[u].matka >= 10000:
        break
    u +=1
    

#After kisa print
for x in range(11):
    print ("\nAuto",numb,"\nRekkari:", auto[y].rekisteritunnus , "\nHuippunopeus:" , auto[y].huippunopeus ,"km/h", "\nNopeus nyt:", auto[y].nopeus ,"km/h", "\nMatka kuljettu:" , auto[y].matka,"km")
    y +=1
    numb +=1
    if numb == 11:
        break