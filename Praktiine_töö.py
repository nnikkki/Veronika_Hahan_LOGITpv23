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


try:
    t=float(input("Mis on ruumi temperatuur?"))
    if t>18:
        print(str(t))
    else:
        print("See on külm")
except :
    print("Viga")


try:
    hind=float(input("Hind: "))
    if hind>=700:
        hind*=0.7
        print(hind)
except :
    print("Viga")

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
