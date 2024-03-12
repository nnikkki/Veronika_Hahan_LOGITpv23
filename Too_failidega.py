from MinuOmaModul1 import *
from random import *
kasutajanimed=[]
salasõnad=[]
while True:
    print("1-Administraatori registreerimine\n2-Kasutaja\n3-Andiminstarot")
    vastus=int(input("Sisestage arv"))
    if vastus==1:
       print("Administraatori registreerimine")
       kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
    elif vastus==2:
       print("Kasutaja")
       print("Tere tulemast viktoriinile!")
       nimi=input("Mis on sinu nimi? ")
       print("Tere", nimi)
    elif vastus==3:
       autoriseerimine(kasutajanimed,salasõnad)
       küsimused=loe_ankeet("Ankeet.txt")
       for i in range(len(küsimused)):
             print(f"{i+1}. Küsimus on: "+küsimused[i])


    
failide_kustutamine()

ümber_kirjuta_fail(input("Faili nimi: "))

kirjuta_failisse("Päevad1.txt")

päevad=loe_failist("Päevad1.txt")
print(päevad)
for päev in päevad:
    print(päev)
