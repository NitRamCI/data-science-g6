from tkinter import *
from tkinter import messagebox

def saluda():
    nombre = txt_nombre.get()
    dni = txt_dni.get()
    email = txt_email.get()
    print(f'Hola, {nombre}! Bienvenido.\n Tu DNI es {dni} \n Tu email es {email}.')
    messagebox.showinfo('saludo', f'Hola, {nombre}! Bienvenido.\n Tu DNI es {dni} \n Tu email es {email}.')

#creamos un objeto de la clase Tk
app = Tk()
#titulo de la ventana
app.title("Registro de Usuario")
#dimensiones de la ventana
app.geometry('400x200')
#creamos un objeto frame
frame = Frame(app)
frame.grid(row=0, column=0)

#creamos una etiqueta y campo de texto para el nombre
lb_nombre = Label(frame, text="Nombres:")
lb_nombre.grid(row=0, column=0, padx=5, pady=5)
txt_nombre = Entry(frame)
txt_nombre.grid(row=0, column=1, padx=5, pady=5)
#creamos una etiqueta y campo de texto para el dni
lb_dni = Label(frame, text="DNI:")
lb_dni.grid(row=1, column=0, padx=5, pady=5)
txt_dni = Entry(frame)
txt_dni.grid(row=1, column=1, padx=5, pady=5)
#creamos una etiqueta y campo de texto para el email
lb_email = Label(frame, text="Email:")
lb_email.grid(row=2, column=0, padx=5, pady=5)
txt_email = Entry(frame)
txt_email.grid(row=2, column=1, padx=5, pady=5)
#creamos un boton
btn_saluda = Button(frame, text="Registrar", command=saluda)
btn_saluda.grid(row=3, column=0)
#mostramos la ventana
app.mainloop()



