print("Calculo de operaciones matemáticas")

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    if a/b == 0:
        return "No se puede dividir por cero"
    return a/b

def residuo(a,b):
    return a%b

def potencia(a,b):
    return a**b

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Residuo")
print("6. Potencia")

ops = {
1: "suma",
2: "resta",
3: "multiplicación",
4: "división",
5: "residuo",
6: "potencia"
}

opc = int(input("Selecciona una opción entre los numeros 1-6: "))
if opc not in ops:
    print("Opción inválida")

else:
    a = float(input("Escribir primer valor: "))
    b = float(input("Escribir segundo valor: "))

if opc == 1:
    print("Resultado de suma: ", suma(a, b))
elif opc == 2:
    print("Resultado de resta: ", resta(a, b))
elif opc == 3:
    print("Resultado de multiplicación: ", multiplicacion(a, b))
elif opc == 4:
    print("Resultado de división: ", division(a, b))
elif opc == 5:
    print("Resultado de residuo: ", residuo(a, b))
elif opc == 6:
    print("Resultado de potencia: ", potencia(a, b))