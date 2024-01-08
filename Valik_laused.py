from random import *
vanus=randint(15,65)
print(vanus)
if vanus>=18:
    print("Täiskasvatud inimene. Vanemad ei saa kontrollida tulemusi")
else:
    print("Vanemad kontrollida lapsi")


a=randint(-1000,1000)
print(a)
if a%3==0:
    print("{0} jägatakse kolmega".format)
else:
    print("Ei saa jagada kolmega")
hinne=input("Mis hinne sa täna sai?")




if hinne==int("5") or hinne=="A":
    print("Super!")
elif hinne==int("4"):
    print("Hea hinne!")
elif hinne==int("3"):
    print("Rahuldav!")
elif hinne==int("2") or hinne==int("1") or hinne=="MA":
    print("Halb!")
elif hinne=="X":
    print("On vaja töö soritada!!")
else:
    print("Ma ei tea, mis hinne see on!")




arv=int(input("Sisesta arv: "))
if arv==13:
    arv=77
print(arv)

if arv>0:
    print("Positiivne arv")
elif arv<0:
    print("Negatiivne arv")
else:
    print("0")