import smtplib, ssl
from email.message import EmailMessage
import imghdr
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
