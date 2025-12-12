#escribir archivos txt

with open("alumnos.txt", "w") as archivo:
    archivo.write("Juan Perez, 20 años\n")
    archivo.write("Maria Gomez, 22 años\n")
    archivo.write("Luis Rodriguez, 19 años\n")

#leer archivos txt
with open("alumnos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

with open("alumnos.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())

#agregar contenido a un archivo txt
with open("alumnos.txt", "a") as archivo:
    nueva_linea ="nuevo texto"
    archivo.write(nueva_linea)
