from MinuOmaModul1 import *

salasõnad=loe_failist("Salasõnad_faillist.txt")
kasutajanimed=loe_failist("Kasutajad.txt")
while True:
    print(kasutajanimed)
    print(salasõnad)
    print("1-registreerimine\n2-autoriseerimine\n3-nime või parooli muutmine\n4-unustanud parooli taastamine\n5-lõpetamine\n")
    vastus=int(input("Sisestage arv"))
    if vastus==1:
        print("Registreerimine")
        kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
        print(salasõnad)
        print(kasutajanimed)
    elif vastus==2:
        print("Autoriseerimine")
        print(salasõnad)
        print(kasutajanimed)
        autoriseerimine(kasutajanimed,salasõnad)
    elif vastus==3:
        print("Nime või parooli muutmine")
        vastus=input("Kas muudame nime, parooli või mõlemad")
        if vastus=="nimi":
            kasutajanimed=nimi_või_parooli_muutmine(kasutajanimed)
        elif vastus=="parool":
            salasõnad=nimi_või_parooli_muutmine(salasõnad)
        elif vastus=="mõlemad":
            print("Nimi muutmine: ")
            kasutajanimed=nimi_või_parooli_muutmine(kasutajanimed)
            print("Parooli muutmine: ")
            salasõnad=nimi_või_parooli_muutmine(salasõnad)
    elif vastus==4:
        print("Unustanud parooli taastamine")

    elif vastus==5:
        print("Lõpetamine")
        break
    else:
        print("Tundmatu valik")
