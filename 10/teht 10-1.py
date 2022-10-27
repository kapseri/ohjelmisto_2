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

        #hissi.kerros = hissi.kerros + x
        #if hissi.kerros > hissi.ylin:
        #    hissi.kerros = hissi.ylin
        #    return hissi.kerros
        #else:
        #    return hissi.kerros


    def kerros_alas(self,x,hissi):
        while True:
            hissi.kerros -=1
            if hissi.kerros < hissi.alin:
                hissi.kerros = hissi.alin
                return hissi.alin
            if hissi.kerros == x:
                return hissi.kerros

       # hissi.kerros = hissi.kerros + x
       # if hissi.kerros < hissi.alin:
       #     hissi.kerros = hissi.alin
       #     return hissi.kerros
       # else:
       #     return hissi.kerros
    
    def siirry_kerrokseen(self,hissi,x):
        x = int(x)
        if x > hissi.kerros:
            self.kerros_ylös(x,hissi)
        else:
            self.kerros_alas(x,hissi)
        

h = Hissi(10,0)
h.siirry_kerrokseen(h,8)
print (h.kerros)
h.siirry_kerrokseen(h,5)
print (h.kerros)
h.siirry_kerrokseen(h,8)
print (h.kerros)
h.siirry_kerrokseen(h,0)
print (h.kerros)