#Kivi-paber-käärid
import random


valikud=["Kivi","Paber","Käärid"]
skoor_bot=0
skoor_kasutaja=0
while True:
    bot=random.choice(valikud)
    kasutaja=input("Valige: Kivi, Paber või Käärid ").capitalize()
    if kasutaja not in valikud:
        print("Vale valik")
        continue
        
    print(f"Teie valik: {kasutaja}")
    print(f"bot valik: {bot}")
    if kasutaja==bot:
       print("Viik")
    elif (kasutaja=="Kivi" and bot=="Käärid") or (kasutaja=="Käärid" and bot=="Paber") or (kasutaja=="Paber" and bot=="Kivi"):
       print("Te võitsite")
       skoor_kasutaja+=1
    else:
       print("bot võitis")
       skoor_bot+=1

    print(f"Teie skoor: {skoor_kasutaja} and bot skoor: {skoor_bot}")
    kordus=input("Kas soovite veel mängida? (jah/ei): ").lower()
    if kordus!="jah":
        break





#6
from random import *
list_=[]
m=randint(1,30)
for i in range(m):
    list_.insert(i,randint(1,87))
print(list_)
max_=max(list_)
print("max:",max_,"Kokku:",m)
a=max_/m
indeks=list_.index(max_)
max_=a
list_[indeks]=a
print(list_)
#6
lst=[]
v=int(input("Kui palju numbreid te nimekirjas soovite?"))
for i in range(v):
    v=int(input("Arv: "))
    lst.append(v)
max_=0
for el in lst:
    if el>suur:
        suur=el
print(f"suur {suur}, indeks on {lst.index(suur) + 1}\n{lst}")
lst[lst.index(suur)]=max_/ len(lst)





#4.2
Indeksid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
while True:
    indeks=input("Sisestage postiindeks: ")
    if len(indeks)==5 and indeks.isdigit():
        break
    else:
        print("Ainult 5 numbriline arv saab kontrollida!")
print(indeks,"kasutatakse",Indeksid[int(indeks[0])-1], "piirkonnas")
if int(indeks[0]) in [1,2,3]:
    pass
else:
    pass
maakond=Indeksid[int(indeks[0])-1]
if maakond==1 or maakond==2 or maakond==3:
     print("Оставайтесь дома!")
else:
     print("Носите маски!")
print()



#4.1
Indeksid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
while True:
    indeks=input("Sisestage postiindeks: ")
    if len(indeks)==5 and indeks.isdigit():
        break
    else:
        print("Ainult 5 numbriline arv saab kontrollida!")
maakond=int(indeks[0])
if maakond==1 or maakond==2 or maakond==3:
     print("Оставайтесь дома!")
else:
     print("Носите маски!")

if   maakond==1:
    print("Tallinn")
elif maakond==2:
    print("Narva, Narva-Jõesuu")
elif maakond==3:
    print("Kohtla-Järve")
elif maakond==4:
    print("Ida-Virumaa, Lääne-Virumaa, Jõgevamaa")
elif maakond==5:
    print("Tartu linn")
elif maakond==6:
    print("Tartumaa, Põlvamaa, Võrumaa, Valgamaa")
elif maakond==7:
    print("Viljandimaa, Järvamaa, Harjumaa, Raplamaa")
elif maakond==8:
    print("Pärnumaa")
elif maakond==9:
    print("Läänemaa, Hiiumaa, Saaremaa")
else:
    print("Tundamatu maakond")

#2.3
from string import *
from random import *

while True:
    sym=input("Mis sümbol kasutame?")
    if sym in punctuation: 
        break
    else:
        print("Saa kasutada ainult:!#$%&'()*+,-./:;<=>?@[\]^_`{|}~.")
while True:
    try:
        N=int(input("Ridade arv:  "))
        break
    except TypeError:
        print("Ainult täisarvud")
for i in range(N):
    print(randint(1,50)*sym)


#2.2.3
vanused=[]
N=int(input("Mitu elemendi?"))
for i in range(N):
    vanus=randint(10,97)
    vanused.append(vanus)
print(vanused)
min_=min(vanused)
max_=max(vanused)
sum_=sum(vanused)
keskmine=sum_/N
print("Minimum:",min_,"Maksimum:",max_,"Summa:",sum_,"Keskmine:",keskmine)



#2.2.2
opilased = ['Juhan', 'Kati', 'Mario', 'Mario', 'Mati', 'Mati']
unikaalsed_opilased = []
for nimi in opilased:
    if nimi not in unikaalsed_opilased:
        unikaalsed_opilased.append(nimi)
print(unikaalsed_opilased)


#2.2.1
nimed=[]
for i in range(5):
    nimi=input(f"Sisestage {i+1}. nimi:")
    nimed.append(nimi)

print("Oli: " , nimed)
nimed.sort()
print("Sortimise pärast: ", nimed)
print("Viimasena oli lisatud: ", nimed)

vananimi=input("Mis nimi on vaja asendada?")
if nimed.count(vananimi)>0:
    uusnimi=input("Mis on uus nimi?")
    i=0
    for nimi in nimed:
        if nimi==vananimi:
           nimed[i]=uusnimi
        i+=1
else:
    print(f"{vananimi} ei ole")
print(nimed)



#1
while True:  
    print("Выберите функцию:")
    print("1. Операции с текстовыми строками")
    print("2. Поиск подстроки в строке")
    print("3. Замена подстроки в строке")
    print("4. Разделение строки")
    print("5. Проверки свойств строки")
    print("6. Объединение строк")
    print("7. Выравнивание строки")
    print("8. Подсчет подстроки в строке")
    print("9. Преобразование регистра строки")
    print("10. Проверка начала и конца строки")
    print("11. Объединение списка строк")
    print("12. Поиск последнего вхождения подстроки")
    print("13. Разбиение строки на три части")
    print("14. Инвертирование регистра строки")
    print("15. Поиск слов с заглавной буквы")
    print("16. Завершить программу")
    valik=input("Введите номер выбранной функции (1-16): ")   # Получаем выбор пользователя  
    if valik=="16":
        print("Программа завершена.")
        break
    elif valik=="1":
        print("\nОперации с текстовыми строками:")  # Операции с текстовыми строками
        print("1. Сцепление строк")
        print("2. Умножение строки на число")
        operatsiooni_valik=input("Выберите операцию (1-2): ")
        if operatsiooni_valik=="1":
            s1=input("Введите первую строку:")    # Сцепление строк
            s2=input("Введите вторую строку:")
            tulemus=s1+s2
            print("Результат сцепления строк:", tulemus)
        elif operatsiooni_valik=="2":    # Умножение строки на число      
            s=input("Введите строку:")
            n=int(input("Введите число:"))
            tulemus=s*n
            print("Результат умножения строки на число:", tulemus)
        else:
            print("Viga")
    elif valik=="2":  # Поиск подстроки в строке
        print("\nПоиск подстроки в строке:")
        s=input("Введите строку:")
        substr=input("Введите подстроку для поиска:")
        indeks=s.find(substr)
        if indeks!=-1:     # Выводит результат поиска, если подстрока найдена
            print(f"Подстрока найдена на позиции {indeks}")
        else:          
            print("Viga")
    elif valik=="3":   # Замена подстроки в строке
        print("\nЗамена подстроки в строке:")
        s=input("Введите строку:")
        vana_alamstring=input("Введите подстроку для замены:")
        uus_alamstring=input("Введите новую подстроку:")
        tulemus=s.replace(vana_alamstring, uus_alamstring)
        print("Результат замены подстроки:", tulemus)
    elif valik=="4":   # Разделение строки
        print("\nРазделение строки:")
        s=input("Введите строку:")
        eraldaja=input("Введите разделитель:")
        osad=s.split(eraldaja)
        print("Результат разделения строки:", osad)
    elif valik=="5":   # Проверки свойств строки
        print("\nПроверки свойств строки:")
        s=input("Введите строку:")
        print("isdigit:", s.isdigit())
        print("isalpha:", s.isalpha())
        print("isalnum:", s.isalnum())
        print("islower:", s.islower())
        print("isupper:", s.isupper())
        print("isspace:", s.isspace())
        print("istitle:", s.istitle())
    elif valik=="6":    # Объединение строк
        print("\nОбъединение строк:")
        eraldaja=input("Введите разделитель:")
        stringid=[]
        n=int(input("Введите количество строк:"))
        for i in range(n):
            stringid.append(input(f"Введите строку {i + 1}:"))
        tulemus=eraldaja.join(stringid)
        print("Результат объединения строк:", tulemus)
    elif valik=="7":     # Выравнивание строки
        print("\nВыравнивание строки:")
        s=input("Введите строку:")
        laius=int(input("Введите ширину выравнивания:"))
        täitechar=input("Введите символ заполнения:")
        print("Результат выравнивания по центру:", s.center(laius, täitechar))
        print("Результат выравнивания влево:", s.ljust(laius, täitechar))
        print("Результат выравнивания вправо:", s.rjust(laius, täitechar))
    elif valik=="8":    # Подсчет подстроки в строке
        print("\nПодсчет подстроки в строке:")
        s=input("Введите строку:")
        alamstring=input("Введите подстроку для подсчета:")
        loend=s.count(substr)
        print("Количество вхождений подстроки:", loend)
    elif valik=="9":      # Преобразование регистра строки
        print("\nПреобразование регистра строки:")
        s=input("Введите строку:")
        print("Результат преобразования к верхнему регистру:", s.upper())
        print("Результат преобразования к нижнему регистру:", s.lower())
    elif valik=="10":    # Проверка начала и конца строки
        print("\nПроверка начала и конца строки:")
        s=input("Введите строку:")
        prefiks=input("Введите префикс:")
        sufiks=input("Введите суффикс:")
        if s.startswith(prefiks):
            print("Строка начинается с префикса")
        else:
            print("Строка не начинается с префикса")
        if s.endswith(sufiks):
            print("Строка заканчивается суффиксом")
        else:
            print("Строка не заканчивается суффиксом")
    elif valik=="11":   # Объединение списка строк
        print("\nОбъединение списка строк:")
        stringid=[]
        n=int(input("Введите количество строк:"))
        for i in range(n):
            stringid.append(input(f"Введите строку {i + 1}:"))
        tulemus=''.join(stringid)
        print("Результат объединения строк из списка:", tulemus)
    elif valik=="12":           # Поиск последнего вхождения подстроки
        print("\nПоиск последнего вхождения подстроки:")
        s=input("Введите строку:")
        alamstring=input("Введите подстроку для поиска:")
        index=s.rfind(substr)
        if index!=-1:
            print(f"Подстрока найдена на позиции {index}")
        else:
            print("Подстрока не найдена")
    elif valik=="13":    # Разбиение строки на три части
        print("\nРазбиение строки на три части:")
        s=input("Введите строку:")
        eraldaja=input("Введите разделитель:")
        osa1, osa2, osa3=s.partition(eraldaja)
        print("Первая часть:", osa1)
        print("Разделитель и вторая часть:", eraldaja, osa2)
        print("Третья часть:", osa3)
    elif valik=="14":     # Инвертирование регистра строки
        print("\nИнвертирование регистра строки:")
        s=input("Введите строку:")
        pööratud=s.swapcase()
        print("Результат инвертирования регистра:", pööratud)
    elif valik=="15":   # Поиск слов с заглавной буквы
        print("\nПоиск слов с заглавной буквы:")
        s=input("Введите строку:")
        suure_algustähega_sõnad=[sõna for sõna in s.split() if sõna.istitle()]
        print("Слова с заглавной буквы:", suure_algustähega_sõnad)
    else:
        print("Viga")
