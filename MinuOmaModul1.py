from math import radians
from pickle import FALSE
from string import *
from time import sleep
from os import path, remove
def registreerimine(kasutajad:list,paroolid:list,koodi:list)->any:
    """Funktsioon tagastab kasutajad ja paroolid
    :param list kasutajad: kasutajad nimed list
    :param list paroolid: paroolide nimed list
    :trype: lisy,list


    """
    while True:
        nimi=input("Mis on sinu kasutajanimed? ")
        if nimi not in kasutajad:
            while True:
                parool=input("Mis on sinu salasõnad? ")
                flag_p=False 
                flag_l=False
                flag_u=False
                flag_d=False
                if len(parool)>=8:                  
                    parool_list=list(parool)
                    for p in parool_list:
                        if p in punctuation:
                               flag_p=True
                        elif p in ascii_lowercase:
                              flag_l=True
                        elif p in ascii_uppercase:
                              flag_u=True
                        elif p in digits:
                              flag_d=True
                    if flag_p and flag_u and flag_l and flag_d:
                          kasutajad.append(nimi)
                          paroolid.append(parool)
                          koodi_sõna=input("Mis on sinu koodi sõnad? ")
                          koodi.append(koodi_sõna)
                    break
                else:
                   print("Nõrk salasõna!")
            break
        else:
            print("Selline kasutaja on juba olemas!")
    return kasutajad, paroolid, koodi_sõna
def autoriseerimine(kasutajad:list,paroolid:list):
    """Funktsioon kuvad ekraanile "Tere tulemas!" kui kasutaja onolemas nimekirjas
       Nimi on järjendis kasutajad
       Salasõna on paroolide järjendis
       Nimi ja salasõna indeksid on võrdsed
    :param list kasutajad:....
    :param list paroolid:....
    """
    p=0
    while True:
        nimi=input("Sisesta kasutajanimi: ")
        if nimi in kasutajad:
            while True:
                parool=input("Sisesta salasõna: ")
                p+=1
                try:
                    if kasutajad.index(nimi)==paroolid.index(parool):
                        print(f"Tere tulemast! {nimi}")
                        break
                except: 
                    print("Vale nimi või salasõna")
                    if p==5:
                        print("Proovi uuesti 10 sek pärast")
                        for i in range(10):
                            sleep(1)
                            print(f"On jäänud {10-i} sek")
                        break
            break
        else:
             print("Kasutajat pole")
 

def nime_või_parooli_muutmine(list_:list):
    """Funktsioon võimaldab kasutajal muuta oma kasutajanime või parooli.
    
    
    
    """
    muutuja=input("Vana nimi või parool: ")
    if muutuja in list_:
        indeks=list_.index(muutuja)
        muutuja=input("Uus nimi või parool: ")
        list_[indeks]=muutuja
    return list_

def unustanud_üarooli_taastamine(kasutajad:list,paroolid:list,koodi:list):
    """Funktsioon aitab kasutajal unustatud parooli taastada.
    
    """
    nimi=input("Sisesta kasutajanimi, mille parooli soovid taastada: ")
    if nimi in kasutajad:
        indeks=kasutajad.index(nimi)
        vastus=input(f"Kas soovid taastada parooli kasutajale '{nimi}'? (jah/ei): ")
        if vastus.lower()=="jah":
            koodi_sõna=input("Mis on koodi sõna? ")
            if koodi_sõna==koodi[indeks]:
                uus_parool=input("Sisesta uus parool: ")
                paroolid[indeks]=uus_parool
                print("Parool on edukalt taastatud!")
            else:
                print("Viga")
        else:
            print("Parooli taastamine tühistatud.")
    else:
        print("Sellise kasutajanimega kasutajat ei leitud.")
def loe_failist(fail:str)->list:
    """Funktsioon loeb tekst *.txt failist
    """
 
    f=open(fail,"r",encoding="utf-8")
    järjend=[]
    for rida in f:
         järjend.append(rida.strip())
    f.close()
    return järjend 
def kirjuta_failisse(fail:str,järjend=[]):
    """Salvestame tekst failisse
    """
    n=int(input("Mitu: "))
    for i in range(n):
        järjend.append(input(f"{i+1}. sõna: "))
    f=open(fail,"a",encoding="utf-8")
    for element in järjend:
        f.write(element+"\n")
    f.close()
def ümber_kirjuta_fail(fail:str):
    """
    """
    f=open(fail,"w")
    text=input("Sisesta tekst:")
    f.write(text+"\n")
    f.close()
def failide_kustamine():
    """
    """
    failinimi=input("Mis fail tahad eemaldada? ")
    if path.isfile(failinimi):
        remove(failinimi)
        print(f"Fail {failinimi} oli kustutatud")
    else:
        print(f"Fail {failinimi} puudubh")