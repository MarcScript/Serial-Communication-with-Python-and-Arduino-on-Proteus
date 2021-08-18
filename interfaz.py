import serial
import time
# Definición de Librerias
from datetime import datetime, timedelta
from tkinter import *
from tkinter import ttk
import os
# Creamos la ventana principal
arduino = serial.Serial("COM4", 9600)
time.sleep(2)
# Creamos la clase App que contendrá la interfaz grafica


class App(Tk):
    def __init__(self):
        super().__init__()
        # Aqui elegimos el alto y el ancho de la ventana
        i = 1
        height = 350
        witdh = 350
        self.geometry("{}x{}".format(height, witdh))
        # Titulo de la ventana
        self.title("Primera aplicación Hola Mundo")
        # Inhibimos cambiar de tamaño la ventana
        self.resizable(width=False, height=False)
        # Etiqueta Hola mundo
        self.Hello = Label(self, text="Hola mundo",
                           font="Times 20 bold")
        self.Hello.place(x=100, y=0)
        # Etiqueta de Nombre
        self.Name_tag = Label(self, text="Nombre:",
                              font="Times 12 bold")
        self.Name_tag.place(x=20, y=50)
        # Etiqueta de Apellido
        self.LastName_tag = Label(self, text="Apellido:",
                                  font="Times 12 bold")
        self.LastName_tag.place(x=20, y=90)
        # ComboBox de seleccion de materia
        self.Combo_tag = Label(self, text="Materia:",
                               font="Times 12 bold")
        self.Combo_tag.place(x=20, y=120)
        # Campo de Entrada de Nombre
        self.NameEnt = Entry(self, width=30, font=(
            'Helvetica', 10, 'bold'), fg="black", justify="left")
        self.NameEnt.place(x=100, y=55)
        # Campo de entrada de apellido
        self.LastNameEnt = Entry(self, width=30, font=(
            'Helvetica', 10, 'bold'), fg="black", justify="left")
        self.LastNameEnt.place(x=100, y=90)
        # Boton de Saludame!
        self.HolaBtn = Button(self, text="Saludame!", command=self.saludar,
                              width=20, height=1, font="Times 12 italic bold", activebackground='#00ff00')
        self.HolaBtn.place(x=100, y=150)
        self.Prende = Button(self, text="Prende", command=self.prenderLed,
                             width=20, height=1, font="Times 12 italic bold", background='#00ff00')
        self.Prende.place(x=100, y=250)
        self.Apaga = Button(self, text="Apaga", command=self.apagarLed,
                            width=20, height=1, font="Times 12 italic bold", background='#d92f0d')
        self.Apaga.place(x=100, y=300)
        # Mensaje de Saludo inicialmente oculto
        self.saludo = Label(self, text="",
                            font="Times 15 bold")
        self.saludo.place(x=50, y=190)
        vlist = ["Proyecto 3", "Proyecto 4"]
        # Lista Combo box
        self.Combo = ttk.Combobox(self, values=vlist)
        self.Combo.set("")
        self.Combo.place(x=100, y=120)
    # Método que saluda

    def saludar(self):

        print("Hola!  {} {}".format(
            self.NameEnt.get(), self.LastNameEnt.get()))
        self.saludo.config(text="Estudiante: {} {}\n Materia: {}".format(
            self.NameEnt.get(), self.LastNameEnt.get(), self.Combo.get()))

    def prenderLed(self):
        dato = "s"
        arduino.write(dato.encode())

    def apagarLed(self):
        dato = "n"
        arduino.write(dato.encode())


# Main del programa ejecutado en bucle
if __name__ == '__main__':
    app = App()
    app.mainloop()
