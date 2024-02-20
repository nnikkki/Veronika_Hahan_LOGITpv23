
##1
#while True:
#   try:
#       mitu=int(input("Mitu tk:  "))
#       if 1<mitu<10:
#           break
#   except ValueError:
#       print("Vale tüüp")    
#for i in range(mitu):
#   print(' Ä '.center(10, ' ' ), end="")
#print()
#for i in range(mitu):
#   print(' / \ '.center(10, ' ' ), end="")
#print()
#for i in range(mitu):
#   print(' | |  '.center(10, ' ' ), end="")
#print()
#for i in range(mitu):
#   print('__'.center(10, ' ' ), end="")
#print()

#1
while True:
   try:
       mitu=int(input("Mitu tk:  "))
       if 1<mitu<10:
           break
   except ValueError:
       print("Vale tüüp")    
for i in range(mitu):
   print(' Ä '.center(10, ' ' ), end="")
print()
for i in range(mitu):
   print(' / \ '.center(10, ' ' ), end="")
print()
for i in range(mitu):
   print(' | |  '.center(10, ' ' ), end="")
print()
for i in range(mitu):
   print('__'.center(10, ' ' ), end="")
print()

#2
from random import *

for i in range(5):
  try:
      N=int(input("Kulutused:  "))
  except ValueError:
     print("Vale tüüp")  
aasta_kulud=0
arv_kulutamine=0
for i in range(12):
   for i in range(5):
       kulutamine=randint(100,1000)
       aasta_kulud+=kulutamine
       arv_kulutamine+=1
keskmine_summa=aasta_kulud/arv_kulutamine
print("Keskmine kulutatud summa aastas: "+str(keskmine_summa))

#3
from random import *
try:
   M=float(input("Kangatüki pikkus meetrites: "))
   while M>0:
       pikkus=randint(0,int(M))
       M -=pikkus
       print("Ülejäänud kangast: "+str(M))
   print("Kangas sai otsa")
except ValueError:
   print("Viga!")

#4
from random import *
L=int(input("Sisestage maatriksi laius: "))
H=int(input("Sisestage maatriksi pikkus: "))
for i in range(L):
   for i in range(H):
       arv=randint(0,100)
       print(arv, end=" ")
   print()

#5
from random import *
A=float(input("Kogu palk: "))
tõõtajad=int(input("Tõõtajate arv: "))
arvutama=0
for i in range(tõõtajad):
    palk=randint(600,2000)
    pensionär=randint(0,5)
    if palk>A and pensionär==1:
        arvutama+=1
if arvutama>0:
    print("Suurema palgaga töötajad: "+ str(A), "eurot ja on pensionäridele: "+str(arvutama))
else:
    print("Kõigeima palgaga töötajaid pole!")


##2
#from random import *


#for i in range(5):
#  try:
#      N=int(input("Kulutused:  "))
#  except ValueError:
#     print("Vale tüüp")  
#aasta_kulud=0
#arv_kulutamine=0
#for i in range(12):
#   for i in range(5):
#       kulutamine=randint(100,1000)
#       aasta_kulud+=kulutamine
#       arv_kulutamine+=1
#keskmine_summa=aasta_kulud/arv_kulutamine
#print("Keskmine kulutatud summa aastas: "+str(keskmine_summa))

##3
#from random import *
#try:
#   M=float(input("Kangatüki pikkus meetrites: "))
#   while M>0:
#       pikkus=randint(0,int(M))
#       M -=pikkus
#       print("Ülejäänud kangast: "+str(M))
#   print("Kangas sai otsa")
#except ValueError:
#   print("Viga!")

##4
#from random import *
#try:   
#   L=int(input("Sisestage maatriksi laius: "))
#   H=int(input("Sisestage maatriksi pikkus: "))
#except:
#    print("Viga")
#for i in range(L):
#   for i in range(H):
#       arv=randint(0,100)
#       print(arv, end=" ")
#   print()

#5
from random import *
while True:
    try:      
         A=float(input("Kogu palk: "))   
         if 600<A<2000:
             break
    except:
     print("Viga")
try: 
    tõõtajad=int(input("Tõõtajate arv: "))
except:
    print("Viga")
arvutama=0
for i in range(tõõtajad):
    palk=randint(600,2000)
    pensionär=randint(0,5)
    if palk>A and pensionär==1:
        arvutama+=1
if arvutama>0:
    print("Suurema palgaga töötajad: "+ str(A), "eurot ja on pensionäridele: "+str(arvutama))
else:
    print("Kõigeima palgaga töötajaid pole!")

