#1 - 4 Etiquetas (Valor 1, Valor 2, Resultado y Operaciones)
#2 - 4 radioButton (Sumar, Restar, Multiplicar y Dividir)
#3 - 3 lineEdit (el lineEdit Resultado no puede ser modificado)
#4 - 1 botón Calcular, que al ser presionado realice la operación correspondiente.
from tkinter import *
from tkinter import messagebox

mainWindow = Tk()
mainWindow.title("Calculadora")
mainWindow.geometry("350x300")
mainWindow.config(bg="#DBBDBD",relief="solid",bd=2 )
mainWindow.resizable(0,0)
radioValue= IntVar(mainWindow)
num1= IntVar(mainWindow,value=None)
num2= IntVar(mainWindow,value=None)
resultado= IntVar(mainWindow,value=None)

def operacion():
    n1=num1.get()
    n2=num2.get()
    opcionRadio= radioValue.get()
    if opcionRadio==1:
        resultado.set(n1+n2)
    if opcionRadio==2:
        resultado.set(n1-n2)
    if opcionRadio==3:
        resultado.set(n1*n2)
    if opcionRadio==4:
        try:
            resultado.set(n1/n2)
        except ZeroDivisionError:
            messagebox.showerror(message="No se puede dividir por 0", title="ERROR")

    
lbl_operacion= Label(mainWindow,text="Operaciones")
lbl_operacion.grid(row=0,column=3,padx=5,pady=5,ipadx=5,ipady=5)

lbl_valor1= Label(mainWindow,text="Valor 1")
lbl_valor1.grid(row=1,column=0,padx=5,pady=5,ipadx=5,ipady=5)

lbl_valor2= Label(mainWindow,text="Valor 2")
lbl_valor2.grid(row=2, column=0,padx=5,pady=5,ipadx=5,ipady=5)

lbl_resultado= Label(mainWindow,text= "Resultado")
lbl_resultado.grid(row=3,column=0,padx=5,pady=5,ipadx=5,ipady=5)

txt_valor1= Entry(mainWindow, textvariable=num1)
txt_valor1.grid(row=1, column=1,padx=5,pady=5,ipadx=5,ipady=5)

txt_valor2= Entry(mainWindow, textvariable=num2)
txt_valor2.grid(row=2, column=1,padx=5,pady=5,ipadx=5,ipady=5)

txt_resultado= Entry(mainWindow,textvariable=resultado, state="readonly")
txt_resultado.grid(row=3,column=1,padx=5,pady=5,ipadx=5,ipady=5)

rbtn_suma= Radiobutton(mainWindow,text="Suma",variable=radioValue ,value=1)
rbtn_suma.grid(row=1,column=3,padx=3,pady=3,ipadx=5,ipady=5)

rbtn_resta= Radiobutton(mainWindow,text="Resta",variable=radioValue, value=2)
rbtn_resta.grid(row=2,column=3,padx=3,pady=3,ipadx=5,ipady=5)

rbtn_multiplicacion= Radiobutton(mainWindow,text="multiplicacion",variable=radioValue,value=3)
rbtn_multiplicacion.grid(row=3,column=3,padx=3,pady=3,ipadx=5,ipady=5)

rbtn_division= Radiobutton(mainWindow,text="Division",variable=radioValue,value=4)
rbtn_division.grid(row=4,column=3,padx=3,pady=3,ipadx=5,ipady=5)
btn_calcular= Button(mainWindow,text="Calcular", command= operacion)
btn_calcular.grid(row=5, column=1,padx=3,pady=3,ipadx=5,ipady=5)

mainWindow.mainloop()