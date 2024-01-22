from datetime import *
from random import*
#2
 summa=0
 for i in range(10):
     arv=float(input("Sisesta arv: "))
     summa+=arv
 print(summa)

#1
nimi=input("Mis on sinu nimi?").capitalize()
mitu=int(input("Mitu korda tervitada?"))
for i in range(1,mitu+1):
    print("Ole tervitatud, "+nimi+", "+str(i)+". korda. ")


#Komm
print("1. variandt -while True-")
while True:
    v=input("Tahan komme!").lower()
    if v=="komm": break

print("2. variandt -while tingimusega-")
v=""
while v!="komm":
    v=input("Tahan komme!").lower()



#Nädala päevad
paevad=["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev","Reede","Laupäev","Pühapäev"]
tunnid=["8 tundi","9 tundi","5 tundi","8 tundi","6 tundi","tunde pole","tunde pole"]
for i in range(7):
    print(paevad[i]+"  "+tunnid[i])


#8
arve_nr=datetime.now()
print(arve_nr)
tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0
tooded=["Piim","Leib","Saia"]   
for i in range(3):
    toode=tooded[i]
    hind=randint(50,150)/100
    v=input("Toode:"+toode+"Hind"+str(hind)+"\nKas tahad osta?").lower()
    if v=="jah":
        mitu=int(input("Mitu"))
        tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
        summa+=mitu*hind    
        
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)




