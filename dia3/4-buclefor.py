#BUCLE FOR

for contador in range(1,11,1):
    print(contador)

# tabla de multiplicar

tabla = int(input("ingresa la tabla de multiplicar que deseas:"))
for contador in range(1,13,1):
    resultado = tabla * contador
    print(f"{tabla} X {contador}= {resultado}")