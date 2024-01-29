print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Mis on sinu nimi? ").capitalize() 
print(nimi, "oi, kui ilus nimi!")
vastus=input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
try:
   if vastus=="1":
       pikkus=int(input(" pikkus: " ))
       mass=float(input("mass:  "))
       indeks=mass/(0.01*pikkus)**2
       print(nimi, "! Sinu keha indeks on {round, 1}".format(indeks))
       if indeks<16:
            print("Tervisele ohtlik alakaal")
       elif 16<indeks<19:
            print("Alakaal")
       elif 19<indeks<25:
            print("Normaalkaal")
       elif 25<indeks<30:
            print("Ülekaal")
       elif 30<indeks<35:
            print("Rasvumine")
       elif 35<indeks<40:
            print("Tugev rasvumine")
       elif indeks>40:
            print("Tervisele ohtlik rasvumine ")
       else : 
           print("Viga")
   else :
       print("Kahju! See on väga kasulik info!")
       print("\n")  
except:
   print("Viga")



from random import *
from datetime import *
a=10                   #int
b=2.3                  #float
c="programma"          #str
d="1.1"                #str
print(b.is_integer())  #Fals
print(c.isalpha())     #True
print(d.isalpha())     #Fals
print(d.isnumeric())   #Fals
print(d.isdigit())
print(d.isdecimal())


#13.1
try:
   gender=input("Sugu: ")
   if gender.isalpha() and (gender.lower()=="naine" or gender.lower()=="mees"):
       if gender.lower()=="naine":
           print("Ei soobi")
       else:
           try:
               age=int(input("Vanus: "))
               if 16<age<=18:
                   print("Oled meeskonnas!")
               else:
                   print("Vanus ei soobi!")
           except :
               print("Vale vanus! Viga andmetüübiga!")
   else: 
       print("Sisesta õige tekst!")
except :
   print("Viga andmetüübiga!")

#13
try:
    gender=input("Kas sa oled mees või naine?")
    if  gender.lower()=="naine":
        print("Kahjuks, otsime ainult mehi")
    elif gender.lower()=="mees":
        try:
           age=int(input("palun märkige oma vanus"))
           if  age>=16 and age<18:
               print("Sa sobid meie meeskonda!")
           else:
            print("Kahjuks sa ei sobi meie meeskonda.")
        except :
             print("Viga")
    else:
         print("Viga")
        
except :
  print("Viga")



#12
try:
#    hind = float(input("Sisesta toote hind:"))
   if    hind<=10:
         soodustus = hind * 0.1
   elif  hind>=10:
         soodustus = hind * 0.2
   else:
         print("Viga")
   okonnelik_hind = hind - soodustus
except :
   print("Viga")




11
#10
#from math import *
#try:
#    n1=float(input("ввеите первое число "))
#    n1=float(input("ввеите второе число 
#    o=input(+ - * /")
#except :
#    pass


9
a=float(input("введите сторону a "))
b=float(input("введите сторону b "))
if a==b:
   print("это квадрат")
else:
   print("viga")



#8
from random import *
from datetime import *

arve_nr=datetime.now()
print(arve_nr)

tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0

toode="Piim"
hind=randint(50,150)/100
v=input("Toode:"+toode+"Hind"+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu"))
    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
    summa+=mitu*hind
toode="Saia"
hind=randint(50,150)/100
v=input("Toode:"+toode+"Hind"+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu"))
    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
    summa+=mitu*hind
toode="Leiba"
hind=randint(50,150)/100
v=input("Toode:"+toode+"Hind"+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu"))
    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
    summa+=mitu*hind
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)



#7
sugu=input("Kas sa oled mees või naine?").lower
if sugu=="naine" or sugu=="n":
   l1=155
   l2=170
   l3=255
elif sugu=="mees" or sugu=="m":
   l1=160
   l2=180
   l3=255
else:
   l1=0
   print("Viga")
if l1!=0:
 try:
       Inimese_kasv=float(input("Kui pikk sa oled?"))
       if Inimese_kasv<=l1:
          print("lühike")
       elif l1<Inimese_kasv<=l2:
          print("keskmine ")
       elif l2<Inimese_kasv<=l3:
          print("pikk")
       else:
          print("Viga")
 except:
        print("Viga")



#6
try:
   Inimese_kasv=float(input("Kui pikk sa oled?"))
   if Inimese_kasv<=150:
       print("lühike")
   elif 150<Inimese_kasv<=180:
       print("keskmine ")
   elif 180<Inimese_kasv<=210:
       print("pikk")
   else:
       print("Viga")
except :
   print("Viga")



#5
try:
   t=float(input("Mis on ruumi temperatuur?"))
   if t>18:
       print(str(t))
   else:
       print("See on külm")
except :
   print("Viga")



#4
try:
   hind=float(input("Hind: "))
   if hind>=700:
       hind*=0.7
       print(hind)
except :
   print("Viga")




#3
try:
   a=float(input("a: "))
   try:
       b=float(input("b: "))
       S=a*b
       print("Pindala võrdub", S)
       soov=input("Kas tahad remondi teha?").lower()
       if soov=="jah" or soov=="да":
           try:
               hind=float(input("Ruutmeetri hind: "))
               summa=hind*S
               print("Remondi summa on", summa)
           except :
               print("Viga")
       else:
           print("Head aega!")
   except :
       print("Viga")
except :
   print("Viga")



#2
eesnimi1=input("Mis on sinu nimi?").capitalize()
eesnimi2=input("Mis on sinu nimi?").capitalize()
if (eesnimi1=="Julia" and eesnimi2=="Karina") or (eesnimi1=="Karina" and eesnimi2=="Julia"):
   print("Te olete täna oma pinginaabrid")
else:
   print("Rühmakaaslased")

if (eesnimi1!=eesnimi2) and eesnimi1 and eesnimi2 in ["Julia", "Karina"]:
   print("Te olete täna oma pinginaabrid")
else:
   print("Rühmakaaslased")



#1
eesnimi=input("Mis on sinu nimi?").capitalize()
if eesnimi=="Juku":
   try:
       vanus=int(input("Kui vana sa oled? ")) 
       print("Jukule ostame ", end="")
       if 0<vanus<=6:
           print("tasuta pilet")
       elif 6<vanus<14:
           print("lastepilet")
       elif 14<vanus<=65:
           print("täispilet")
       elif 65<vanus<=100:
           print("sooduspilet")
       else:
           print("mitte midagi. Viga andmetega!")
   except :
       print("Int formaaton on vaja kasutada") 

else:
   print("Mine ise kinno!")
