from pickle import FALSE
from string import *
from time import sleep
def registreerimine(kasutajad:list,paroolid:list)->any:
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
                           
                    break
                else:
                   print("Nõrk salasõna!")
                break
        else:
            print("Selline kasutaja on juba olemas!")
    return k, p
def autoriseerimine(kasutajad:list,paroolid:list):
    """Funktsioon kuvad ekraanile "Tere tulemas!" kui kasutaja onolemas nimekirjas
       Nimi on järjendis kasutajad
       Salasõna on paroolide järjendis
       Nimi ja salasõna indeksid on võrdsed
    :param list kasutajad:....
    :param list paroolid:....
    """
    while True:
        nimi=input("Sisesta kasutajanimi: ")
        parool=input("Sisesta salasõna: ")
        p+=1
        if nimi in kasutajad and paroolid:
            if kasutajad.index(nimi)==paroolid.index(parool):
                print(f"Tere tulemast! {nimi}")
                break
            else:
                print("Vale nimi või salasõna")
                if p==5:
                    print("Proovi uuesti 10 sek pärast")
                    for i in range(10):
                        sleep(1)
                        print(f"On jäänud {10-i} sek")
        else:
            print("Kasutajat pole")