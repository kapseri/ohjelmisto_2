class Hissi:
    def __init__(self, ylin, alin, kerros = 0):
        self.kerros = kerros
        self.ylin = ylin
        self.alin = alin
    
    def kerros_ylös(self,x,hissi):
        while True:
            hissi.kerros +=1
            if hissi.kerros > hissi.ylin:
                hissi.kerros = hissi.ylin
                return hissi.ylin
            if hissi.kerros == x:
                return hissi.kerros


    def kerros_alas(self,x,hissi):
        while True:
            hissi.kerros -=1
            if hissi.kerros < hissi.alin:
                hissi.kerros = hissi.alin
                return hissi.alin
            if hissi.kerros == x:
                return hissi.kerros
    
    def siirry_kerrokseen(self,hissi,x):
        x = int(x)
        if x > hissi.kerros:
            self.kerros_ylös(x,hissi)
        else:
            self.kerros_alas(x,hissi)

class Talo:
    def __init__(self, ylin, alin, numero,maara=0):
        self.numero = numero
        self.ylin = ylin
        self.alin = alin
        self.hissit = []
        for x in range(self.numero):
            ylin = self.ylin
            alin = self.alin
            hissi = Hissi(ylin,alin)
            self.hissit.append(Hissi(ylin,alin))
    siirry = Hissi.siirry_kerrokseen
    def aja_hissiä(self,numero,kerros):
        hissi = self.hissit[numero -1]
        use = hissi.siirry_kerrokseen(hissi,kerros)
        print("Hissi numero",numero, "nyt kerroksessa", hissi.kerros)
        return use
    def palohälytys(self):
        maara = len(self.hissit)
        num = 0
        numero = num + 1
        for x in range(maara):
            hissi = self.hissit[num]
            use = hissi.siirry_kerrokseen(hissi,self.alin)
            print("Hissi numero",numero, "nyt kerroksessa", hissi.kerros)
            num +=1
            numero +=1
        return use


# Pääohjelma

koti = Talo(10,0,3)

koti.aja_hissiä(2,2)

koti.aja_hissiä(3,3)

koti.palohälytys()