from tkinter import *



root = Tk()
root.geometry("900x900")

Hintergrundfile =PhotoImage(file="C:\\Users\\mcfre\\OneDrive\\Desktop\\Projekte\\Misc zeug\\TicTacToe_Label.png")
x = PhotoImage(file="C:\\Users\\mcfre\\OneDrive\\Desktop\\Projekte\\Misc zeug\\x.png.png")
o = PhotoImage(file="C:\\Users\\mcfre\\OneDrive\\Desktop\\Projekte\\Misc zeug\\O.png")

Hintergrund = Label(root,image=Hintergrundfile)
Hintergrund.pack()

def FenstererstellenX():
    new_root = Tk()
    label = Label(new_root,text="Spieler mit X hat gewonnen")
    label.pack()
    root.destroy()

def FenstererstellenO():
    new_root = Tk() #Toplevel()
    label = Label(new_root,text="Spieler mit O hat gewonnen")
    label.pack()
    root.destroy()

def displayX(event):
    if event.widget != Hintergrund  :

        event.widget.config(image=x, width=280, height=275)

def displayO(event):
    if event.widget != Hintergrund  :

        event.widget.config(image=o, width=280, height=275)

count = 0

List = [Hintergrund]
XList = []
OList = []

def play(event):
    if event.widget not in List:
        List.append(event.widget)
        global count
        if count == 0 or count == 2 or count == 4 or count == 6 or count == 8:
            displayX(event)
            XList.append(event.widget)
        else:
            displayO(event)
            OList.append(event.widget)
        count = count + 1
        
        
        if Feld_1 in XList and Feld_2 in XList and Feld_3 in XList or Feld_4 in XList and Feld_5 in XList and Feld_6 in XList or  Feld_7 in XList and Feld_8 in XList and Feld_9 in XList or  Feld_1 in XList and Feld_4 in XList and Feld_7 in XList or Feld_2 in XList and Feld_5 in XList and Feld_8 in XList or  Feld_3 in XList and Feld_6 in XList and Feld_9 in XList or  Feld_1 in XList and Feld_5 in XList and Feld_9 in XList or  Feld_3 in XList and Feld_5 in XList and Feld_7 in XList:
            FenstererstellenX()
        if Feld_1 in OList and Feld_2 in OList and Feld_3 in OList or Feld_4 in OList and Feld_5 in OList and Feld_6 in OList or  Feld_7 in OList and Feld_8 in OList and Feld_9 in OList or  Feld_1 in OList and Feld_4 in OList and Feld_7 in OList or Feld_2 in OList and Feld_5 in OList and Feld_8 in OList or  Feld_3 in OList and Feld_6 in OList and Feld_9 in OList or  Feld_1 in OList and Feld_5 in OList and Feld_9 in OList or  Feld_3 in OList and Feld_5 in OList and Feld_7 in OList:
            FenstererstellenO()
        
    



root.bind("<Button-1>",play)

Feld_1 = Label(root,bg="white",width=39,height=18)
Feld_1.place(x=-4,y=0)

Feld_4 = Label(root,bg="white",width=39,height=18)
Feld_4.place(x=-4,y=325)

Feld_7 = Label(root,bg="white",width=39,height=18)
Feld_7.place(x=-4,y=625)

Feld_2 = Label(root,bg="white",width=39,height=18)
Feld_2.place(x=320,y=0)

Feld_5 = Label(root,bg="white",width=39,height=18)
Feld_5.place(x=320,y=325)

Feld_8 = Label(root,bg="white",width=39,height=18)
Feld_8.place(x=320,y=625)

Feld_3 = Label(root,bg="white",width=39,height=18)
Feld_3.place(x=626,y=0)

Feld_6 = Label(root,bg="white",width=39,height=18)
Feld_6.place(x=626,y=325)

Feld_9 = Label(root,bg="white",width=39,height=18)
Feld_9.place(x=626,y=625)

root.mainloop()