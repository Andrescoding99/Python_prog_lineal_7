#Formula: p = 2*pi*r / a = pi * r2^

print("Calculo del perimetro y area de un circulo")

#Definicion de variables
perimetro = 0
area = 0
radio = 0
PI = 3.14

#Capturar datos
radio = float(input("Ingresa el radio del círculo: "))

#Procesamiento de datos
perimetro = 2 * PI * radio
area = PI * radio**2

#Muestra
print("\n El perimetro de un circulo es: " , perimetro)#concatenado
print("El area de un circulo es: {}".format(area) )#interpolado es para mas valores


