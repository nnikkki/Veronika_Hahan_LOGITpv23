from ast import Try
from random import *
from math import *
from re import A

#10
try:
    P=int(input("Sõbrade kogus: "))
except :
    print("Kogus on täisarv")
Pitsa_hind = 12.90
Pitsa_hind*=Pitsa_hind*1.1
print("Igaüks maksab", Pitsa_hind/P)




#9
try:
    a=float(input("введите сторону А "))
except :
    print("On vaja täisvarv kasutada!")
try:
    b=float(input("введите сторону B "))
except :
    print("Viga muutujaga!")
try:
    c=float(input("введите сторону C "))
except :
    print("Viga c muutujaga!")

P= a + b + c
print(f"периметр треугольника: {P} ")

#8
print("  @..@")        #либо через center
print(" (----)")
print("( \__/ )")
print("^^ \"\" ^^  ")

#7
try:
     min_=int(input("Min:  "))
except :
    print("On vaja täisarv kasutuda!") 
try:
    max_=int(input("Max:  "))
except :
    print("Viga max_ muutujaga!")


a1=randint(min_,max_)
a2=randint(min_,max_)
a3=randint(min_,max_)
a4=randint(min_,max_)
a5=randint(min_,max_)
keskmine=(a1+a2+a3+a4+a5)/5
print("Arvud: {0},{1},{2},{3},{4}. Arvitmetiline keskmine on  {5}".format(a1,a2,a3,a4,a5,keskmine))  




#6
try:
    aeg = float(input("Mitu tundi kulus sõiduks? "))
    try:
        teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
        kiirus = teepikkus/aeg
        print("Sinu kiirus oli " + str(kiirus) + "km/h")
    except :
     print("Viga andmetaga! ") 
except :
    print("On vaja ainult numbrid sisestada!")





#5
N=float(input("pikkus: "))
M=float(input("laius: "))
d=sqrt(M**2+N**2)
print("Diagonaal=",d,"m")


#4
u=float(input("Ümbermõõt: "))  #L=pi*r=pi*d
d=round(u/pi,2)
print("läbimõõt =",d)


#3
kokku=randint(1,100)
print("Laual peal on",kokku,"kommid.Mitu tahad süüa?")
kommid=int(input())
kokku-=kommid
print("Nüüd kokku on",kokku)


vanus=18
eesnimi="Jaak"
pikkus=16.5
kas_käib_koolis=True

print("Muutuja vanus",vanus,"on",type(vanus))
print("Muutuja eesnimi",eesnimi,"on",type(eesnimi))
print("Muutuja pikkus",pikkus,"on",type(pikkus))
print("Muutuja kas_käib_koolis",kas_käib_koolis,"on",type(kas_käib_koolis))

arv1=float(input("Arv1: "))
t=input("Tehe: ")
arv2=float(input("Arv2: "))
vastus=eval(str(arv1)+t+str(arv2))
print(str(arv1)+t+str(arv2)+"="+str(vastus))
print(arv1,t,arv2,"=",vastus,sep="")
print("{0}{1}{2}={3}".format(arv1,t,arv2,vastus))


print("Tere maailm!".center(75,"-"))
nimi=input("Mis on sinu nimi? ").capitalize()   #nika->Nika
print("Tere "+nimi+"!")
print("Tere",nimi+"!")
print("Tere {0}!".format(nimi))
vanus=int(input("Kui vana sa oled? "))  #"21"!=21
print("Tere {0}!Sa oled {1} aastat vana".format(nimi,vanus))
print("Muutuja nimi=",nimi,type(nimi))
print("Muutuja vanus=",vanus,type(vanus))