import csv

with open('alumnos.csv', 'w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['dni', 'nombre','email'])
    escritor.writerow(['12345678','Juan Perez','perezgmail.com'])


#leer archivos csv
with open('alumnos.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print('---------------')
        for campo in fila:
            print(campo)
