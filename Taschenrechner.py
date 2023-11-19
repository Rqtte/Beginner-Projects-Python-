from math import *
from tkinter import *

#
#Aufbau: 
#
#    Textfläche <-- Knöpfe mit denen man was da eingeben kann
#    
#    Enterknopf mit dem man das Berechnet
#
#

#Funktionen

def plus():
    aW=rf.cget("text")
    nW=aW + "+"
    rf.config(text=nW)

def minus():
    aW=rf.cget("text")
    nW=aW + "-"
    rf.config(text=nW)

def mal():
    aW=rf.cget("text")
    nW=aW + "*"
    rf.config(text=nW)

def geteilt():
    aW=rf.cget("text")
    nW=aW + "/"
    rf.config(text=nW)    

def plus():
    aW=rf.cget("text")
    nW=aW + "+"
    rf.config(text=nW)

def komma():
    aW=rf.cget("text")
    nW=aW + "."
    rf.config(text=nW)

def klammerlinks():
    aW=rf.cget("text")
    nW=aW + "("
    rf.config(text=nW)    

def klammerrechts():
    aW=rf.cget("text")
    nW=aW + ")"
    rf.config(text=nW)    
    
def eins():
    aW=rf.cget("text")
    nW=aW + "1"
    rf.config(text=nW)

def zwei():
    aW=rf.cget("text")
    nW=aW + "2"
    rf.config(text=nW)    

def drei():
    aW=rf.cget("text")
    nW=aW + "3"
    rf.config(text=nW)

def vier():
    aW=rf.cget("text")
    nW=aW + "4"
    rf.config(text=nW)

def fünf():
    aW=rf.cget("text")
    nW=aW + "5"
    rf.config(text=nW)

def sechs():
    aW=rf.cget("text")
    nW=aW + "6"
    rf.config(text=nW)

def sieben():
    aW=rf.cget("text")
    nW=aW + "7"
    rf.config(text=nW)

def acht():
    aW=rf.cget("text")
    nW=aW + "8"
    rf.config(text=nW)

def neun():
    aW=rf.cget("text")
    nW=aW + "9"
    rf.config(text=nW)

def Enter():
    aW=rf.cget("text")
    rf.config(text=str(eval(aW)))        

def remove():
    aW=rf.cget("text")
    nW = aW[slice(0,-1)]
    rf.config(text=nW)


#Fenster

Rechner = Tk()

Rechner.title("Taschenrechner")

icon = PhotoImage(file="C:\\Users\\mcfre\\OneDrive\\Desktop\\Projekte\\Misc zeug\\W Taschenrechner\\icon.png")
Rechner.iconphoto(True,icon)
Rechner.config(background="grey")

#Frame

#frame = Frame(Rechner)
#frame.pack()



#Eingabefenster

rf = Label(Rechner,bg="gray",width=15,height=2,text="")
rf.grid(row=1,column=1,columnspan=3)



#Knöpfe

b1 = Button(Rechner,text=1,command=eins,padx=10,pady=5,width=1)
b1.grid(row=2,column=1)

b2 = Button(Rechner,text=2,command=zwei,padx=10,pady=5,width=1)
b2.grid(row=2,column=2)

b3 = Button(Rechner,text=3,command=drei,padx=10,pady=5,width=1)
b3.grid(row=2,column=3)

b4 = Button(Rechner,text=4,command=vier,padx=10,pady=5,width=1)
b4.grid(row=3,column=1)

b5 = Button(Rechner,text=5,command=fünf,padx=10,pady=5,width=1)
b5.grid(row=3,column=2)

b6 = Button(Rechner,text=6,command=sechs,padx=10,pady=5,width=1)
b6.grid(row=3,column=3)

b7 = Button(Rechner,text=7,command=sieben,padx=10,pady=5,width=1)
b7.grid(row=4,column=1)

b8 = Button(Rechner,text=8,command=acht,padx=10,pady=5,width=1)
b8.grid(row=4,column=2)

b9 = Button(Rechner,text=9,command=neun,padx=10,pady=5,width=1)
b9.grid(row=4,column=3)

bplus = Button(Rechner,text="+",command=plus,padx=10,pady=5,width=1)
bplus.grid(row=5,column=1)

bminus = Button(Rechner,text="-",command=minus,padx=10,pady=5,width=1)
bminus.grid(row=5,column=2)

bmal = Button(Rechner,text="*",command=mal,padx=10,pady=5,width=1)
bmal.grid(row=5,column=3)

bgeteilt = Button(Rechner,text="/",command=geteilt,padx=10,pady=5,width=1)
bgeteilt.grid(row=6,column=1)

bklammerlinks = Button(Rechner,text="(",command=klammerlinks,padx=10,pady=5,width=1)
bklammerlinks.grid(row=6,column=2)

bklammerechts = Button(Rechner,text=")",command=klammerrechts,padx=10,pady=5,width=1)
bklammerechts.grid(row=6,column=3)

bkomma = Button(Rechner,text=",",command=komma,padx=10,pady=5,width=1)
bkomma.grid(row=7,column=2)


enter= Button(Rechner,text="Enter",command=Enter,padx=10,pady=5,width=8)
enter.grid(row=1,column=9)

entfernen= Button(Rechner,text="Entfernen",command=remove,padx=10,pady=5,width=8)
entfernen.grid(row=2,column=9)

Rechner.mainloop()