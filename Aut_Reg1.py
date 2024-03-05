from MinuOmaModul1 import *
koodi_sõna=["koodi.1"]
salasõnad=["Parool.1"]
kasutajanimed=["Kasutajanimed.1"]
while True:
    print(kasutajanimed)
    print(salasõnad)
    print(koodi_sõna)
    print("1-registreerimine\n2-autoriseerimine\n3-nime või parooli muutmine\n4-unustanud üarooli taastamine\n5-lõpetamine")
    vastus=int(input("Sisestage arv "))
    if vastus==1:
        print("registreerimine")
        kasutajanimed,salasõnad,koodi_sõna=registreerimine(kasutajanimed,salasõnad,koodi_sõna)
    elif vastus==2:
        print("autoriseerimine")
        autoriseerimine(kasutajanimed,salasõnad)
    elif vastus==3:
        print("nime või parooli muutmine")
        vastus=input("Kas muudame nime või parooli ")
        if vastus=="nime":
            kasutajanimed=nime_või_parooli_muutmine(kasutajanimed)
        elif vastus=="parool":
            salasõnad==nime_või_parooli_muutmine(salasõnad)
        elif vastus=="mõlemad":
            print("Nimi muutmine: ")
            kasutajanimed=nime_või_parooli_muutmine(kasutajanimed)
            print("Parooöi muutmine")
            salasõnad==nime_või_parooli_muutmine(salasõnad)
    elif vastus==4:
        print("unustanud üarooli taastamine")
        print("Unustanud üarooli taastamine")
        kasutajanimed,salasõnad,koodi_sõna = unustanud_üarooli_taastamine(kasutajanimed,salasõnad,koodi_sõna)
    elif vastus==5:
        print("lõpetamine")
        break
    else:
        print("Tundmatu valik")  

