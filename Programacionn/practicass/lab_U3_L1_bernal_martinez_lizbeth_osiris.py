# Ejercicio 1
print("--- Clasificacion por edad ---")
edad = int(input("Ingresa tu edad: "))
if edad < 13:
    print("Clasificacion: niño")
elif edad <= 17:
    print("Clasificacion: adolescente")
else:
    print("Clasificacion: adulto")

# Ejercicio 2
print("\n--- Validar acceso ---")
usuario_correcto = "usuario"
contraseña_correcta = "clave123"

usuario = input("Ingresa el usuario: ")
contraseña = input("Ingresa la contraseña: ")

if usuario == usuario_correcto and contraseña == contraseña_correcta:
    print("Acceso concedido")
elif usuario == usuario_correcto:
    print("Contraseña incorrecta")
else:
    print("Usuario no encontrado")

# Ejercicio 3
print("\n--- Calculadora de envío ---")
peso_paquete = float(input("Ingresa el peso del paquete en kg: "))

if peso_paquete <= 1:
    costo_envio = 50
elif peso_paquete <= 5:
    costo_envio = 90
else:
    costo_envio = 150

if peso_paquete > 10:
    costo_envio *= 0.9

print(f"El costo de envío es: ${costo_envio:.2f}")

# Ejercicio 4
print("\n--- Clasificar la temperatura ---")
temperatura = float(input("Ingresa la temperatura en grados: "))
if temperatura < 10:
    print("Clasificación: frío")
elif temperatura < 25:
    print("Clasificación: templado")
else:
    print("Clasificación: calor")

# Ejercicio 5
print("\n--- Calificacion con letras ---")
calificacion = float(input("Ingresa una calificación de 0 a 100: "))
if calificacion >= 90:
    letra = "A"
elif calificacion >= 80:
    letra = "B"
elif calificacion >= 70:
    letra = "C"
elif calificacion >= 60:
    letra = "D"
else:
    letra = "F"
print(f"Letra: {letra}")

# Ejercicio 6
print("\n--- Descuento por monto de compra ---")
monto_compra = float(input("Ingresa el monto de la compra: $"))
if monto_compra > 500:
    descuento = 20
elif monto_compra > 200:
    descuento = 10
else:
    descuento = 0

monto_final = monto_compra * (1 - descuento / 100)
print(f"Descuento: {descuento}%")
print(f"Monto final a pagar: ${monto_final:.2f}")

# Ejercicio 7
print("\n--- Validar un rango ---")
numero = float(input("Ingresa un numero: "))
if 1 <= numero <= 100:
    print("El numero esta en el rango de 1 a 100.")
else:
    print("El numero no esta en el rango de 1 a 100.")

# Ejercicio 8
print("\n--- Clasificar el IMC ---")
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))
imc = peso / estatura ** 2

if imc < 18.5:
    categoria_imc = "bajo peso"
elif imc < 25:
    categoria_imc = "normal"
elif imc < 30:
    categoria_imc = "sobrepeso"
else:
    categoria_imc = "obesidad"

print(f"IMC: {imc:.2f}. Clasificación: {categoria_imc}")

# Ejercicio 9
print("\n--- Tarifas de electricidad ---")
consumo = float(input("Ingresa el consumo mensual en kWh: "))

if consumo <= 150:
    costo_total = consumo * 1.20
elif consumo <= 300:
    costo_total = (150 * 1.20) + ((consumo - 150) * 1.80)
else:
    costo_total = (150 * 1.20) + (150 * 1.80) + ((consumo - 300) * 2.50)

print(f"Consumo: {consumo:g} kWh")
print(f"Costo total: ${costo_total:.2f}")
