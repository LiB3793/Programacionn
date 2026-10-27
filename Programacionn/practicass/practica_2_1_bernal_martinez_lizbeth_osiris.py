# Ejercicio 1: Datos personales
print("--- Ejercicio 1 ---")
#Prueba 1
Nombre = "Osiris"
Edad = 26
Ciudad = "Guadalajara"
print(Nombre, Edad, Ciudad)

#Ejercicio 2: Actualizar un contador
print("--- Ejercicio 2 ---")
Contador = 0
Contador = Contador + 1
print(Contador)
contador = Contador + 1
print(contador)
contador = contador + 1
print(contador)

#Prueba 2 (reiniciando con otro valor inicial o repitiendo la logica)
print("--- Prueba 2 ---")
Contador = 0
for i in range(3):
    Contador = Contador + 1
    print(Contador)

#Ejercicio 3: Constante de conversion
print("--- Ejercicio 3 ---")
Pulgadas_a_Centimetros = 2.54

#Prueba 1
pulgadas = 10
centimetros = pulgadas * Pulgadas_a_Centimetros
print(f"{pulgadas} pulgadas son {centimetros} centimetros")

#Prueba 2
pulgadas = 25.5
centimetros = pulgadas * Pulgadas_a_Centimetros
print(f"{pulgadas} pulgadas son {centimetros} centimetros")

#Ejercicio 4: area de un rectangulo (incluyendo extra de perimetro)
print("--- Ejercicio 4 ---")
#Prueba 1
base = 5
altura = 9
area = base * altura
perimetro = 2 * (base + altura)
print(f"El area del rectangulo es: {area}")
print(f"El perimetro del rectangulo es: {perimetro}")

#Prueba 2
base = 12.5
altura = 4
area = base * altura
perimetro = 2 * (base + altura)
print(f"El area del rectangulo es: {area}")
print(f"El perimetro del rectangulo es: {perimetro}")

#Ejercicio 5: Total con IVA
print("--- Ejercicio 5 ---")
IVA = 0.16

#Prueba 1
precio = 200
total = precio + (precio * IVA)
print(f"El total con IVA es: {total}")

#Prueba 2
precio = 1250.50
total = precio + (precio * IVA)
print(f"El total con IVA es: {total}")

#Ejercicio 6: Intercambio de valores (con Extra de Python)
print("--- Ejercicio 6 ---")
#Prueba 1 (Usando variable temporal)
a = 10
b = 20
print(f"Antes del intercambio: a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"Después del intercambio: a = {a}, b = {b}")

#Prueba 2 (Usando la forma abreviada en Python)
x = "hola"
y = "mundo"
print(f"Antes del intercambio: x = {x}, y = {y}")
x, y =y, x
print(f"Después del intercambio(forma abreviada): x = {x}, y = {y}")

#Ejercicio 7: Identificar tipos con type()
print("--- Ejercicio 7 ---")
#Prueba 1
variable_entero = 42
variable_decimal = 3.14
variable_texto = "programación"
variable_booleano = True

print(type(variable_entero))
print(type(variable_decimal))
print(type(variable_texto))
print(type(variable_booleano))

#Prueba 2 (con otros tipos de valores)
print("--- Prueba 2 ---")
v1 = -7
v2 = 0.001
v3 = "Python"
v4 = False

print(type(v1))
print(type(v2))
print(type(v3))
print(type(v4))

#Ejercicio 8: Convertir tipos
print("--- Ejercicio 8 ---")
#Prueba 1
texto_numero="25"
numero_convertido=int(texto_numero)
print("convertido a entero:", numero_convertido, type(numero_convertido))

entero_original=100
texto_convertido=str(entero_original)
print("convertido a texto:", texto_convertido, type(texto_convertido))

#Prueba 2
texto_num2="999"
numero_convertido2=int(texto_num2)
print("convertido a entero:", numero_convertido2, type(numero_convertido2))

entero_original2=5050
texto_convertido2=str(entero_original2)
print("convertido a texto:", texto_convertido2, type(texto_convertido2))

#Ejercicio 9: Booleanos y Comparaciones
print("--- Ejercicio 9 ---")
#Prueba 1
a = 8
b = 3
mayor = a > b
print(f"a={a}, b={b}, a es mayor que b: {mayor}")
print("Tipo:", type(mayor))

#Prueba 2
a=15
b=42
mayor = a > b
print(f"a={a}, b={b}, a es mayor que b: {mayor}")
print("Tipo:", type(mayor))
