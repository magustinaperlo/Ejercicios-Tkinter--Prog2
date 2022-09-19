from ast import Delete
from asyncio.windows_events import NULL
from cgitb import text
from tkinter import *
from tkinter import messagebox

#1 - Tres etiquetas (Primer número, Segundo número y Resultado)
#2 - 3 lineEdit (el lineEdit de Resultado no se puede modificar)
#3 - 6 Botones (+, -, *, /, % y RESET). El botón CLEAR debe borrar los
#3 lineEdit. Al presionar (+, -, *, / o %) el único campo que se modifica es Resultado.

mainWindow = Tk()
mainWindow.title("Calculadora")
mainWindow.geometry("350x400")
mainWindow.config(bg="#DBBDBD",relief="solid",bd=2 )
mainWindow.resizable(0,0)
var1= IntVar(mainWindow,value=None)
var2= IntVar(mainWindow,value=None)
var3= IntVar(mainWindow,value=None)

def sumar():
    suma= int(txt_primerNumero.get()) + int(txt_segundoNumero.get())
    return var3.set(suma)

def restar():
    resta= int(txt_primerNumero.get()) - int(txt_segundoNumero.get())
    return var3.set(resta)

def multiplicacion():
    mult=int(txt_primerNumero.get()) * int(txt_segundoNumero.get())
    return var3.set(mult)

def division():
    try:
        div= int(txt_primerNumero.get()) / int(txt_segundoNumero.get())
        return var3.set(div)
    except ZeroDivisionError:
        messagebox.showerror(message="No se puede dividir por 0", title="ERROR")

def reset():
    txt_primerNumero.delete(0,END)
    txt_segundoNumero.delete(0,END)
    txt_resultado.delete(0,END)


lbl_num1= Label(mainWindow, text= "Primer Numero",bg="#DBBDBD")
lbl_num1.grid(row= 0, column=0, padx=20, pady= 20,ipadx=20)

lbl_num2= Label(mainWindow, text="Segundo Numero",bg="#DBBDBD")
lbl_num2.grid(row=1 ,column= 0,padx=20, pady= 20,ipadx=20)

lbl_resultado= Label(mainWindow, text="Resultado",bg="#DBBDBD")
lbl_resultado.grid(row= 2, column=0, padx=20, pady= 20,ipadx=20)

txt_primerNumero= Entry(mainWindow,textvariable= var1)
txt_primerNumero.grid(row=0, column=1)

txt_segundoNumero= Entry(mainWindow,textvariable=var2)
txt_segundoNumero.grid(row=1, column= 1)

txt_resultado= Entry(mainWindow, state="readonly",textvariable= var3)
txt_resultado.grid(row=2, column= 1)

btn_suma= Button(mainWindow, text= "+", command= sumar,width=10)
btn_suma.grid(row=4, column=0,padx=20, pady= 20,ipadx=10)

btn_resta= Button(mainWindow,text="-", command= restar,width=10)
btn_resta.grid(row=4,column=1,padx=20, pady= 20,ipadx=10)

btn_multiplicacion= Button(mainWindow, text= "*",width=10, command= multiplicacion)
btn_multiplicacion.grid(row=5,column=0,padx=20, pady= 20,ipadx=10)

btn_division= Button(mainWindow,text="/",width=10, command= division)
btn_division.grid(row=5,column=1,padx=20, pady= 20,ipadx=10)

btn_reset= Button(mainWindow,text="RESET",width=10, command= reset)
btn_reset.grid(row= 6,column= 0,padx=20, pady= 20,ipadx=10)


mainWindow.mainloop()