import math
from tkinter import *
import random

#1 - 3 Etiquetas (Número 1, Número 2 y Número Generado)
#2 - 2 Spin Box
#3 - 1 lineEdit que no pueda ser modificado
#4 - 1 Botón "Generar"
mainWindow= Tk()
mainWindow.title("Generador")
mainWindow.geometry("300x300")
mainWindow.resizable(0,0)
mainWindow.config(bg="#DBBDBD",relief="solid",bd=2)
var1= IntVar(mainWindow,value=0)
var2= IntVar(mainWindow,value=0)
resultado= IntVar(mainWindow, value=0)
infinito= math.inf


def generarNum():
    num1= int(sbx_num1.get())
    num2= int(sbx_num2.get())
    gen= random.randint(num1,num2)
    return resultado.set(gen)
    

lbl_num1= Label(mainWindow, text= "Numero 1")
lbl_num1.grid(row= 0, column=0,padx=10,pady=10,ipadx=5,ipady=5)

lbl_num2= Label(mainWindow, text="Numero 2")
lbl_num2.grid(row=1, column=0,padx=10,pady=10,ipadx=5,ipady=5)

lbl_numGenerado= Label(mainWindow, text="Numero Generado")
lbl_numGenerado.grid(row=3,column=0,padx=10,pady=10,ipadx=5,ipady=5)

sbx_num1= Spinbox(mainWindow, from_=0, to=infinito,increment=1, state="readonly")
sbx_num1.grid(row=0, column=1,padx=10,pady=10,ipadx=5,ipady=5)

sbx_num2= Spinbox(mainWindow, from_=0, to=infinito,increment=1,state="readonly")
sbx_num2.grid(row=1,column=1,padx=10,pady=10,ipadx=5,ipady=5)

txt_resultado= Entry(mainWindow,textvariable=resultado, state="readonly")
txt_resultado.grid(row=3,column=1,padx=10,pady=10,ipadx=5,ipady=5)

btn_aceptar= Button(mainWindow, text= "Aceptar", command=generarNum)
btn_aceptar.grid(row=4,column=1,padx=10,pady=10,ipadx=5,ipady=5)



mainWindow.mainloop()