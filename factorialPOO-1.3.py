from tkinter import *

class Factorial():
    def __init__(self):
        self.mainWindow = Tk()
        self.mainWindow.title("Factorial")
        self.mainWindow.geometry("500x80")
        #fijamos los valores para que el usuario no extienda ni achique demasiado la ventana.
        self.mainWindow.minsize(500, 80) 
        self.mainWindow.maxsize(500, 80)
        self.mainWindow.config(bg="#DBBDBD")
        self.miFrame = Frame(self.mainWindow) #aqui creo y pruebo el frame ... como es
        self.miFrame.config(bg="#DBBDBD")
        self.miFrame.pack()

        self.n1 = IntVar(value=0)
        self.n2 = StringVar()

        self.lb1 = Label(self.miFrame, text="n")
        self.lb1.grid(row=0, column=0,padx=8)
        self.txt1 = Entry(self.miFrame, textvariable=self.n1, state="readonly")
        self.txt1.grid(row=0, column=1,padx=8)
        self.lb2 = Label(self.miFrame, text="Factorial (n)")
        self.lb2.grid(row=0, column=2,padx=8)
        self.txt2 = Entry(self.miFrame, textvariable=self.n2,state="readonly")
        self.txt2.grid(row=0, column=3, padx=8)
        self.btn = Button(self.miFrame, text="Siguiente", width=10, command=self.click_factorial)
        self.btn.grid(row=0, column=4,padx=8)

    def iniciar(self):
        self.mainWindow.mainloop()


    def click_factorial(self): 
        self.n1.set(self.n1.get() + 1)

        fact = 1
        for i in range(1, (self.n1.get()) + 1):
            fact = fact * i
        self.n2.set(fact)

a=Factorial()
a.iniciar()
