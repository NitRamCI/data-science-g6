from tkinter import *
from tkinter import messagebox

def saludar():
    nombre = txt_nombre.get()
    print(f'Hola, {nombre}! Bienvenido a Tkinter.')
    messagebox.showinfo('saludo', f'Hola, {nombre}! Bienvenido a Tkinter.')


#creamos un objeto de la clase Tk
app = Tk()

#titulo de la ventana
app.title("Mi primera app con Tkinter")

#dimensiones de la ventana
app.geometry('300x100')

#creamos un objeto frame
frame = Frame(app)
frame.grid(row=0, column=0)

#creamos una etiqueta
lb_nombre = Label(frame, text="Nombre:")
lb_nombre.grid(row=0, column=0, padx=5, pady=5)

#creamos un campo de texto
txt_nombre = Entry(frame)
txt_nombre.grid(row=0, column=1, padx=5, pady=5)

#creamos un boton
btn_saludar = Button(frame, text="Saludar", command=saludar)
btn_saludar.grid(row=1, column=0)

#mostramos la ventana
app.mainloop()
