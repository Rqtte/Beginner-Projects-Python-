from tkinter import *
import random
import time




WIDTH = 1000
HEIGHT = 1000
ITEMGRÖßE = 50
GESCHWINDIGKEIT = 0.10

Liste = []
Listefutter = []
aussetzen = False
Punkte = 0
spielen = True


richtungx = + ITEMGRÖßE
richtungy = 0

class Blob:
    def __init__(self, root):
        self.root = root

    def createstart(self):
        global uno
        global dos
        
        uno = round(random.randint(0+(ITEMGRÖßE*4),int(WIDTH-(ITEMGRÖßE*6)))/ITEMGRÖßE) *ITEMGRÖßE
        dos = round(random.randint(0+(ITEMGRÖßE*4),int(HEIGHT-(ITEMGRÖßE*6)))/ITEMGRÖßE)*ITEMGRÖßE
        Liste.insert(-1,self.root.create_rectangle(uno,dos,uno+ITEMGRÖßE,dos+ITEMGRÖßE,fill="green"))
        Liste.insert(-1,self.root.create_rectangle(uno+ITEMGRÖßE,dos,uno+ITEMGRÖßE+ITEMGRÖßE,dos+ITEMGRÖßE,fill="green"))
        Liste.insert(-1,self.root.create_rectangle(uno+(2*ITEMGRÖßE),dos,uno+ITEMGRÖßE+(2*ITEMGRÖßE),dos+ITEMGRÖßE,fill="green"))

    def create(self):
        global uno
        global dos
        uno = uno + richtungx
        dos = dos + richtungy
        Liste.insert(0,self.root.create_rectangle(uno,dos,uno+ITEMGRÖßE,dos+ITEMGRÖßE,fill="green"))
        
        if aussetzen == False:
            canvas.delete(Liste[-1])
            Liste.pop(),

        


class Futter:
    def __init__(self, root):
        self.root = root 

    def create(self):
        wdh = True
        while wdh == True:
            wdh = False
            uno = round(random.randint(0,int(WIDTH-ITEMGRÖßE))/ITEMGRÖßE)*ITEMGRÖßE
            dos = round(random.randint(0,int(HEIGHT-ITEMGRÖßE))/ITEMGRÖßE)*ITEMGRÖßE
            unodos = [int(uno),int(dos),int(uno)+int(ITEMGRÖßE),int(dos)+int(ITEMGRÖßE)]
            for i in Liste:
                if unodos == canvas.coords(i):
                    wdh = True
        Listefutter.insert(0,self.root.create_oval(uno,dos,uno+ITEMGRÖßE,dos+ITEMGRÖßE,fill="red"))
                    
                
                    
                
  

    

def Richtungändernoben(event):
    global richtungx
    global richtungy
    richtungx=0
    richtungy=-ITEMGRÖßE
def Richtungändernunten(event):
    global richtungx
    global richtungy
    richtungx=0
    richtungy=+ITEMGRÖßE
def Richtungändernrechts(event):
    global richtungx
    global richtungy
    richtungx=+ITEMGRÖßE
    richtungy=0
def Richtungändernlinks(event):
    global richtungx
    global richtungy
    richtungx=-ITEMGRÖßE
    richtungy=0

def gameovercheck():
    Listeohnenr1 = Liste[1:]
    if aussetzen2 == False:   
        for i in Listeohnenr1:
            if canvas.coords(i) == canvas.coords(Liste[0]):
                gameover()
    
    for i in canvas.coords(Liste[0])[0::2]:
        if i < 0 or i > WIDTH:
            gameover()
    for i in canvas.coords(Liste[0])[1::2]:
        if i < 0 or i > HEIGHT:
            gameover()



def nochmalspielen():
    global x
    x = True
    varr.set(1)


def gameover():
    global varr
    canvas.create_text(WIDTH/2,HEIGHT/2,text="Verloren",fill="#7a0d05",font=("Comic Sans",ITEMGRÖßE*3))
    btn = Button(root,text="Nochmal spielen",font=("Comic Sans",30),command=nochmalspielen,bg="#025e07",fg="White",	activebackground="green",activeforeground="white")
    btn.place(x=WIDTH/2-175,y=HEIGHT/5*4-5)
    btn.wait_variable(varr)
    btn.destroy
    global spielen
    spielen = False



def abchecken():
    if canvas.coords(Listefutter[0]) == canvas.coords(Liste[0]):
        canvas.delete(Listefutter[0])
        Listefutter.pop()
        global aussetzen
        aussetzen = True

def submit():
    pass


            





root= Tk()
root.config(bg="#025e07")
varr = IntVar()
#icon = PhotoImage("Snake-Icon.png")
#root.iconphoto(True,icon)
x = True
while x == True:
    x = False

    Var = StringVar(root,str(Punkte))


    label = Label(root,textvariable=Var,font=("Comic Sans",ITEMGRÖßE),bg="#025e07",fg="#ffffff")
    label.pack()

    canvas= Canvas(root,width=WIDTH,height=HEIGHT,bg="black",borderwidth=0,highlightbackground="#025e07")
    canvas.pack()

    blob = Blob(canvas)
    blob.createstart()

    root.bind("<W>",Richtungändernoben)
    root.bind("<A>",Richtungändernlinks)
    root.bind("<S>",Richtungändernunten)
    root.bind("<D>",Richtungändernrechts)
    root.bind("<w>",Richtungändernoben)
    root.bind("<a>",Richtungändernlinks)
    root.bind("<s>",Richtungändernunten)
    root.bind("<d>",Richtungändernrechts)


    aussetzen2 = True
    spielen = True
    Punkte=0
    Var.set("Punkte: "+str(Punkte))
    while spielen == True:



        Blob(canvas).create()
        aussetzen = False

        if len(Listefutter) == 1:
            pass
        else:
            if aussetzen2 == False:
                Punkte = Punkte + 1
                Var.set("Punkte: "+str(Punkte))
            futter = Futter(canvas)
            futter.create()

        abchecken()
        gameovercheck()


        aussetzen2 = False
        sleep = False

        time.sleep(GESCHWINDIGKEIT)
        root.update()
    
    canvas.destroy()
    label.destroy()
    richtungx = + ITEMGRÖßE
    richtungy = 0
    aussetzen = False
    Liste = []
    Listefutter = []
    
    

root.mainloop()
