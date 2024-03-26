from MinuOmaModul1 import *
from random import *
import smtplib, ssl
from email.message import EmailMessage
import imghdr
file = open("Ankeet.txt", "r", encoding='utf-8')
kasutajanimed=[]
salasõnad=[]  
while True:
    print("1-Administraatori registreerimine\n2-Kasutaja\n3-Andiminstarot")
    vastus=int(input("Sisestage arv"))
    print("arv")
    if vastus==1:
       print("Administraatori registreerimine")
       kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
    elif vastus==2:
           print("Kasutaja")
           print("Tere tulemast viktoriinile!")
           nimi=input("Mis on sinu nimi? ")
           print("Tere", nimi)      
           õigevastus=0  
           for rida in file:
               N=rida.split(":")
               print(N[0])
               katsed=3
               while katsed>0:
                   sisend=input("Vastus: ").strip()
                   if sisend==N[1].strip():
                      õigevastus+=1
                      print("Tubli!")
                      break
                   else:
                      katsed-=1
                      print("Viga. Teil on",katsed,"katse.")
               else:
                  print("Enam katseid pole jäänud. Õige vastus on:",N[1].strip())
           print("Õigete vastuste arv:",õigevastus)
           if õigevastus>7:
               print("Test läbitud")
               with open("Tulemusi.txt", "a") as file:
                   file.write(f"{nimi}")
                   smtp_server="smtp.gmail.com"
                   port=587 #For starttls
                   sender_email="veronikagagan2017@gmail.com"
                   password=input("Kirjuta oma salasõna ja vajuta enter: ")
                   context=ssl.create_default_context()
                   #msg="Tere tulemast!"
                   msg=EmailMessage()
                   msg.set_content("Tulemusi")
                   msg['Subject']="Kirja teema"
                   msg['From']="Veronika Hahan" #Nimi ka saab kirjutada #Kellelt
                   msg['To']="dom1ntiy@gmail.com" #Kellele   marina.oleinik@tthk.ee
                   with open("Tulemusi.txt", "r") as file:
                       file.read()
                   with open("tulemusi.jpg",'rb') as fpilt:
                        pilt=fpilt.read()
                   msg.add_attachment(pilt,maintype='image',subtype=imghdr.what(None, pilt))
                   try:
                        server=smtplib.SMTP(smtp_server,port)
                        server.starttls(context=context) #Secure the connection
                        server.login(sender_email,password)
                        server.send_message(msg) #server.sendmail(sender_email,to_email,msg)
                        print("Kiri on saadetud")
                   except Exception as e:
                        print(e)
                   finally:
                        server.quit()

           else:
               print("Test ebaõnnestus")
    elif vastus==3:
       autoriseerimine(kasutajanimed,salasõnad)
       küsimused=loe_ankeet("Ankeet.txt")
       print(f"Küsimused on: " + str(küsimused[0]),"Vastused on: " + str(küsimused[1]))
file.close()

   
failide_kustutamine()

ümber_kirjuta_fail(input("Faili nimi: "))

kirjuta_failisse("Päevad1.txt")

päevad=loe_failist("Päevad1.txt")
print(päevad)
for päev in päevad:
    print(päev)