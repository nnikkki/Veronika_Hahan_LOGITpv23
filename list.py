nimed=["Mati","Kati"]
while True:
    valik=input("Andmete lisamine-add \nAndmete nätamine-show\nAndmete kustutamine-del\nJärjendi pööramine-rev\nAndmete kustutamine-clear\nAndmete sortimine-sort\n")
    if valik=="add":
        valik=input("Kas lisame mitu inimest(mitu) või positsioonile(pos)\n").lower()
        if valik=="mitu":
            while True:
                try:
                    mitu=int(input("Mitu inimest lisame?"))
                    if mitu>0:
                       break
                    else:   
                        print("On vaja arv suurem kui 0")
                except:
                    print("Viga")
            for i in range(mitu):
                nimi=input("Sisesta nimi: ").capitalize()
                nimed.append(nimi)
        elif valik=="pos":
            while True:
                try:
                    indeks=int(input("Kuhu lisamine?"))
                    if indeks>0 and indeks<len(nimed):
                       break
                    else:
                        print("On vaja arv suurem kui 0")
                except:
                    print("Viga")           
            nimi=input("Mis nimi: ")
            nimed.insert(indeks-1,nimi)    
        else:
            print("Vale valik! Kirjuta (mitu) või (pos) ")
    elif valik=="del":
        while True:
            try:
                valik=input("Kas kustutame nimi(nimi või indeksi järgi lind)").lower()
                if valik=="nimi":
                    nimi=input("Mis nimi on vaja kustutada? ").capitalize()
                    kogus=nimed.count(nimi)
                    if kogus>0:
                        for i in range(kogus):
                            nimed.remove(nimi)
                    else:
                        print(f"Nimi {nimi} ei ole nimekirjas")
                elif valik=="indeksi":
                    indeks=int(input("Mis in järjekordne number? "))
                    nimed.pop(indeks-1) 
                else:
                    print("Vale valik! Kirjuta (nimi) või (indeksi)")
            except:
                print("Viga") 
    elif valik=="show":
        print(nimed)
    elif valik=="rev":
        print(nimed.reverse())
    elif valik=="sort":
        print(nimed.sort())
    elif valik=="clear":
        print(nimed.clear())
    elif valik=="ots":
        ind=-1
        nimi=input("Mis nimi otsime? ")
        if nimed.count(nimi)>0:
            for nim in nimed:
                ind=nimed.index(nimi,ind+1)
                print(f"{nimi} on indeksiga {ind}")
        else:
            print(f"{nimi} on indeksiga {ind+1}")
    