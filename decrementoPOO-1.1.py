#incremento con POO
from cgitb import text
from tkinter import *

class Window:
    def __init__(self):
        self.title= "Incremento"
        self.icon= "./Tkinter/Imagenes/Shield.ico"
        self.size= "300x300"

    def mainWindowPropiedades(self):
        #-----------------------VENTANA-------------------------------------
        #Creamos la ventana raiz
        mainWindow= Tk()

        #Le damos nombre a la ventana ----> title()
        mainWindow.title(self.title)

        #Icono para la ventana ----> iconbitmap(DIR)
        mainWindow.iconbitmap(self.icon)

        #tamaño de la ventana ---> geometry()
        mainWindow.geometry(self.size)

        mainWindow.config(bg= "#E3C2C2")

        self.mainWindow= mainWindow #debido a que ventana es una propiedad que no existe, variable local!

    def InsertarGrid(self,elemento): #funcion para ingresar los Widgets a Grid con validacion de input.
        while True:
            try:
                row= int(input(f'Ingrese el numero de fila en el que desea insertar el Widget {elemento}: '))
                column= int(input(f'Ingrese el numero de columna en el que desea insertar el Widget {elemento}: '))
            except ValueError:
                print("Ingreso erroneo, intente de nuevo...")
                continue
            else:
                break
        self.widget= elemento
        self.widget.grid(row=row,column=column, pady=2, padx=2)

    def crearLabel(self,texto,nombreLabel): #funcion para crear widget de tipo Label con sus propiedades y text value.
        nombreLabel= Label(self.mainWindow, text= texto)
        nombreLabel.config(padx=10,pady=10,font=("Arial",11),relief="sunken")
        self.label= nombreLabel #para usar en otros lados.

    def crearEntry(self, valor,nombreEntry): #Funcion para crear widget de tipo Entry con los parametros valor ()
        var= IntVar(self.mainWindow, value= valor)
        self.var= var
        nombreEntry= Entry(self.mainWindow, textvariable=self.var, state="readonly")
        nombreEntry.config()
        self.nombreEntry= nombreEntry

    def restar(self):
        i=1
        resta= int(self.nombreEntry.get())-(i)
        return self.var.set(resta)

    def crearPushButton(self,nombreButton):
        nombreButton= Button(self.mainWindow,relief="raised", text="-", command= self.restar)
        self.button= nombreButton

    def correrPrograma(self):
        self.mainWindow.mainloop()

ui= Window()
ui.mainWindowPropiedades()
ui.crearLabel("Contador","label1")
ui.InsertarGrid(ui.label)
ui.crearEntry(3,"entrySuma")
ui.InsertarGrid(ui.nombreEntry)
ui.crearPushButton("BotonResta")
ui.InsertarGrid(ui.button)
ui.correrPrograma()