finalizar = False
print("Calculadora\n1) Sumar\n2) Restar \n3) Multiplicar\n4) Dividir\n5) Salir")
while not(finalizar):
    opciones = int(input("Elija una opción: "))
    if opciones == 1:
     suma1 = int(input("Elija el primer número: "))
     suma2 = int(input("Elija el segundo número: "))
     print("El resultado es: " + str(suma1 + suma2))
    elif opciones == 2:
     resta1 = int(input("Elija el primer número: "))
     resta2 = int(input("Elija el segundo número: "))
     print("El resultado es: " + str(resta1 - resta2))
    elif opciones == 3:
     multiplicacion1 = int(input("Elija el primer número: "))
     multiplicacion2 = int(input("Elija el segundo número: "))
     print("El resultado es: " + str(multiplicacion1 + multiplicacion2))
    elif opciones == 4:
     division1 = int(input("Elija el primer número: "))
     division2 = int(input("Elija el segundo número: "))
     print("El resultado es: " + str(division1 / division2))
    elif opciones == 5:
     finalizar = True