
from tkinter import *

mainWindow= Tk()
mainWindow.title("Contador")
mainWindow.geometry("600x200")
mainWindow.resizable(0,0)
mainWindow.config(bg="#DBBDBD",relief="solid",bd=2)
valor= IntVar(mainWindow, value=0)


def incrementar():
    i=1
    suma= int(entry.get())+(i)
    return valor.set(suma)

def decrementar():
    i=1
    resta= int(entry.get())-(i)
    return valor.set(resta)

def resetear():
    valor.set(0)
    

contadorL= Label(mainWindow,text="Contador")
contadorL.grid(row=3,column=0,padx=10,pady=10,ipadx=5,ipady=5)

entry= Entry(mainWindow,state="readonly",textvariable=valor)
entry.grid(row=3,column=1,padx=10,pady=10,ipadx=5,ipady=5)

countUp= Button(mainWindow,text="Count Up",command= incrementar)
countUp.grid(row=3, column=2,padx=10,pady=10,ipadx=5,ipady=5)

countDown= Button(mainWindow,text="Count Down",command= decrementar)
countDown.grid(row=3, column=3,padx=10,pady=10,ipadx=5,ipady=5)

reset= Button(mainWindow,text= "Reset",command= resetear)
reset.grid(row=3, column=4,padx=10,pady=10,ipadx=5,ipady=5)


mainWindow.mainloop()