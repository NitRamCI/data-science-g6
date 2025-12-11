# CALCULADORA

# datos de entrada
numero1 = int(input("ingresa el primer numero: "))
numero2= int(input("ingresa el segundo numero: "))
operacion = input("ingresa la operacion a realizar (+, -, *, /): ")
# procesamiento de datos
if operacion == "+":
    resultado = numero1+ numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Error: Division por cero"
else:
    print("Error: operacion invalida")
    exit()
# datos de salida
print(f"{numero1} {operacion} {numero2} = {resultado}")
