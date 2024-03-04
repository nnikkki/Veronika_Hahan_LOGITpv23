from MinuOmaModul1 import *

salasõnad=[]
kasutajanimed=[]
while True:
    print("1-registreerimine\n2-autoriseerimine\n3-nime või parooli muutmine\n4-unustanud üarooli taastamine\n5-lõpetamine")
    vastus=int(input("Sisestage arv "))
    if vastus==1:
        print("registreerimine")
        kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
    elif vastus==2:
        print("autoriseerimine")
        autoriseerimine(kasutajanimed,salasõnad)
    elif vastus==3:
        print("nime või parooli muutmine")
    elif vastus==4:
        print("unustanud üarooli taastamine")
    elif vastus==5:
        print("lõpetamine")
        break
    else:
        print("Tundmatu valik")

