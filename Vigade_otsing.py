from math import *   #изменила последовательность

print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => ")) #скобки ";добавить float
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)
di=a*sqrt(2)                               #убрать math 
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud")        
b=float(input("Sisesta ristküliku 1. külje pikkus => "))     #добавить float
c=float(input("Sisesta ristküliku 2. külje pikkus => "))     #добавить float
S=b*c
print("Ristküliku pindala", S)                #скобки "
P=2*(b+c)
print("Ristküliku ümbermõõt", P)
di=sqrt(b**2+c**2)                            #убрать math,**
print("Ristküliku diagonaal", round(di))    
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => "))        #добавить float
d=2*r
print("Ringi läbimõõt",d)                    #добавить запятую перед d
S=pi*r**2
print("Ringi pindala", round(S))
C=2*pi*r            #убрать()
print("Ringjoone pikkus", round(C))          
