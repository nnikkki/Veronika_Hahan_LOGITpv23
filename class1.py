from datetime import *
from random import*
from tkinter.tix import InputOnly
#16
number=randint(1,100)
katsed=3
while katsed>0:
    külaline=int(input("угадай число от 1 до 100:"))
    if külaline==number:
        print("вы угадали")
        break
    else:
        katsed-=1
        print(f"у вас осталось {katsed} попыток")
        if katsed==0:
            print(f"извините вы использовали все попытки, загаданное число было{number}")
            veelkord=input("хотите ли угадать?: ").lower()
            if veelkord.lower()=="ei":
                break
            else:
                katsed=3
         

#15
katsed=0
while True:
    vastus=input("Osta elevant ära! Kirjuta elevant")
    katsed+=1

    if vastus.loweer()==:
        print(f"Õige! Ostsid elevanti ära {katsed} katsega.")
        break
    else:
        print("Vale vastus. Proovi uuesti.")


#9
Korrutamine=[5]
arv=["1","2","3","4","5","6","7","8","9","10"]
for i in range(10):
    tulemus=int(arv[i])*5
    print(f"{arv[i]}*5={tulemus}")


#9.1
korrutamine=5
for i in range(1,11):
    tulemus=(i)*5
    print(f"{i}*5={tulemus}")

#8
paaris=0
paaritu=0
for i in range(1, 101):
    if i%2==0:
        print(f"{i}-paaris")
        paaris+=1
    else:
        print(f"{i}-paaritu")
        paaritu+=1

print(f"Paarisarvude arv: {paaris}")
print(f"Paaritute arvude arv: {paaritu}")

#7
for i in range(5):
    number=randint(0,9)
    print(number,end="")
print()


#4
for i in range(1,11):
    for j in range(1,11):
        print(i*j)
    print()

#3
k=0
while True:
    k+=1
    num1=randint(1, 50)
    num2=randint(1, 50)
    p=0
    v=0
    while p!=5:
        p+=1
        v=int(input("Millega võrdub {0}+{1}".format(num1,num2)))
        if v==num1+num2:
            print("Tubli")
            break
        else:
            print("Mõtle veel!")
    print("{0}+{1}={2}".format(num1,num2,num1+num2))


    if k==5: break






#2
summa=0
for i in range(10):
     arv=float(input("Sisesta arv: "))
     summa+=arv
print(summa)


summa=0
i=0
while True:
    i+=1
    arv=float(input("Sisesta arv: "))
    summa+=arv
    if i==10: break
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




