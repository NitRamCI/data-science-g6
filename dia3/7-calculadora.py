import os
import math

# CALCULADORA COMPLETA CON PYTHON
salir = "no"
while (salir == "no"):
    os.system("clear")

#entrada de datos 
    print("====== CALCULADORA =======")  
   
    print("======OPCIONES======")
    print("1. SUMA")
    print("2. RESTA")
    print("3. MULTIPLICACION")
    print("4. DIVISION")
    print("5. tablade multiplicar")
    print("7. potencia")
    print("6. raiz cuadrada")
    operacion = int(input("ingrese la operacion a realizar"))
    
    if operacion == 5:
        tabla = int(input("ingresa la tabla de multiplicar que deseas:"))
        for contador in range(1,13,1):
            resultado = tabla * contador
            print(f"{tabla} X {contador}= {resultado}")
        salir = input("desea salir?")
        if (salir == "si"):
            break
    elif operacion == 6:
        numeroraiz = int(input("ingresa el numero para sacar la raiz cuadrada:"))
        resultado = math.sqrt(numeroraiz)
        tipoOperacion = "RAIZ CUADRADA"
        print(f"La {tipoOperacion} de {numeroraiz} es: {resultado}")
    elif operacion == 7:
        base = int(input("ingresa la base:"))
        exponente = int(input("ingresa el exponente:"))
        resultado = math.pow(base,exponente)
        tipoOperacion = "POTENCIA"
        print(f"La {tipoOperacion} de {base} elevado a {exponente} es: {resultado}")
    elif operacion >=1 and operacion <=4:
        numero1 = int(input("ingresa el primer numero: "))
        numero2= int(input("ingresa el segundo numero: "))
                #proceso
        if operacion == 1:
            resultado = numero1 + numero2
            tipoOperacion = "SUMA"
        elif operacion == 2:
            resultado = numero1 - numero2
            tipoOperacion = "RESTA"
        elif operacion == 3:
            resultado = numero1 * numero2
            tipoOperacion = "MULTIPLICACION"
        elif operacion == 4:
            if numero2 != 0:
                resultado = numero1/numero2
                tipoOperacion = "DIVISION"
            else:
                print("ERROR: DIVISION EN CERO")
                break
        else:
            print("Operacion no valida")
            exit()

        # SALIDA DE DATOS
        print(f"la {tipoOperacion} de {numero1} y {numero2} es: {resultado}")

    salir = input("desea salir?")

    if (salir == "si"):
        
        break
        os.system("clear")

