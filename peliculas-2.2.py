
from tkinter import *
from tkinter import messagebox 

mainWindow = Tk()
mainWindow.title("Peliculas")
mainWindow.geometry("400x400")
mainWindow.config(bg="#DBBDBD",relief="solid",bd=2 )
mainWindow.resizable(0,0)
var= StringVar(mainWindow,value=None)

def añadirPelicula():
    pelicula= txt_inputPelicula.get()
    lbx_peliculas.insert(END,pelicula)
    if (pelicula.isspace() or len(pelicula) <= 1):
        messagebox.showinfo(message="El nombre de la película no debe comenzar con un espacio", title="Error")
    else:
        lbx_peliculas.insert(END,a)
        txt_inputPelicula.delete(0,END)


lbl_pelicula= Label(mainWindow, text= "Titulo de la Pelicula",bg="#258C99",fg="white",relief="solid", bd="2")
lbl_pelicula.grid(row=0 ,column=0,padx=10,pady=10,ipadx=10,ipady=10)

lbl_peliculas= Label(mainWindow, text="Peliculas",bg="#258C99",fg="white",relief="solid", bd="2")
lbl_peliculas.grid(row=0,column=1,padx=10,pady=10,ipadx=10,ipady=10)

txt_inputPelicula= Entry(mainWindow, textvariable= var,bg="#258C99",fg="white")
txt_inputPelicula.grid(row=2,column=0,padx=10,pady=10,ipadx=10,ipady=10)

btn_aceptar= Button(mainWindow, text="Aceptar", command=añadirPelicula,bg="#258C99",fg="white")
btn_aceptar.grid(row= 3, column=0,padx=10,pady=10,ipadx=10,ipady=10)

lbx_peliculas= Listbox(mainWindow,bg="#258C99",fg="white",relief="solid", bd="2")
lbx_peliculas.grid(row=2,column=1,padx=10,pady=10,ipadx=10,ipady=10)

mainWindow.mainloop()
