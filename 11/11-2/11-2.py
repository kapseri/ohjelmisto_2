from auto import *


sähkö = Sähköauto("ABC-15", 180, 52.5)
bensa = Polttomoottoriauto("ACD-123", 165, 32.3)
testi = Auto("ABC-123",165)

print (sähkö.rekisteritunnus)
print (bensa.huippunopeus)

bensa.Kiihdytä(100)
bensa.kulje(3)
sähkö.Kiihdytä(20)
sähkö.kulje(3)
print(f"Auto {sähkö.rekisteritunnus} ajoi {sähkö.matka}km")
print(f"Auto {bensa.rekisteritunnus} ajoi {bensa.matka}km")