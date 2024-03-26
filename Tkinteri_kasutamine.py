from tkinter import *
f=False
def tehtudvalik():
    global f 
    if f:
        texbox.configure(show="*")
        f=False
    else:
        texbox.configure(show="")
        f=True
def textpealkirjasse():
    t=texbox.get()
    pealkiri.configure(text=t)
    texbox.delete(0,END)
aken=Tk()
aken.geometry("600x560")
aken.title("Akna pealkiri")
aken.configure(bg="#9aab89")
aken.iconbitmap("iconn.ico")
pealkiri=Label(aken, text="Põhielemedid",bg="#d7b4ae",
              fg="#6fa287", cursor="arrow",
             font="Times_New_Roman 16", 
             justify=CENTER,
            height=3,
           width=20)
raam=Frame(aken) 
texbox=Entry(raam,bg="#6fa287",
             fg="#000000",
             font="Times_New_Roman 16",
             width=20)
pilt=PhotoImage(file="rabbit.png")
var=BooleanVar( )
valik=Checkbutton(raam,image=pilt,variable=var,onvalue=True, offvalue=False, command=tehtudvalik)
valik.deselect()
nupp=Button(raam,
            text="Vajuta mind",
            bg="#d7b4ae",
            fg="#6fa287",
            font="Times_New_Roman 16",
            width=16,
            command=textpealkirjasse)

pealkiri.pack()
raam.pack()
texbox.grid(row=0,column=0)
valik.grid(row=0,column=1)
nupp.grid(row=0,column=2)


aken.mainloop()

