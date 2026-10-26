#Alumna: Lizbeth Osiris Bernal Martinez
#Descripcion: Programa para registar productos de compra,validar los datos ingresados y calcular el subsidio total,IVA(16%) y total final con formato de recibo.

#Seccion 1: Captura y validacion de productos:

#Pedir al usuario cuantos productos registrara.
entrada_cantidad_productos=input("¿Cuantos productos que desea registrar?: ")

#Validar que la cantidad de productos sea un numero entero positivo usando .isdigit() 
while not entrada_cantidad_productos.isdigit() or int(entrada_cantidad_productos) <= 0:
    print("Error: Debe ingresar un número entero positivo.")
    entrada_cantidad_productos=input("¿Cuantos productos que desea registrar?: ")

    cantidad_productos=int(entrada_cantidad_productos)

#Lista para almacenar la informacion de cada producto registrado
#lista_productos = []

 #Seccion 2: Registro y validacion de cada producto:

 for i in range(cantidad_productos):
    print(f"\nRegistro del producto {i+1}:")
    nombre_producto=input("Ingrese el nombre del producto: ")

    #Validar que el nombre del producto no este vacio
    while not nombre_producto.strip():
        print("Error: El nombre del producto no puede estar vacío.")
        nombre_producto=input("Ingrese el nombre del producto: ")

    #Validar que el precio sea un numero positivo usando .replace() y .isdigit()
    entrada_precio=input("Ingrese el precio del producto: ")
    while not entrada_precio.replace('.', '', 1).isdigit() or float(entrada_precio) <= 0:
        print("Error: Debe ingresar un número positivo para el precio.")
        entrada_precio=input("Ingrese el precio del producto: ")

    #Validar que la cantidad sea un numero entero positivo usando .isdigit()
    entrada_cantidad=input("Ingrese la cantidad del producto: ")
    while not entrada_cantidad.isdigit() or int(entrada_cantidad) <= 0:
        print("Error: Debe ingresar un número entero positivo para la cantidad.")
        entrada_cantidad=input("Ingrese la cantidad del producto: ")

    #Calcular el subtotal del producto
    subtotal = float(entrada_precio) * int(entrada_cantidad)

    #Guardar los datos en la lista de productos
    lista_productos.append({
        "nombre": nombre_producto,
        "precio": float(entrada_precio),
        "cantidad": int(entrada_cantidad)
    })

#Seccion 3: Calculo del subsidio, IVA y total final:

#Calcular el subsidio total (10% del subtotal de todos los productos)
subsidio_total = sum(producto["precio"] * producto["cantidad"] for producto in lista_productos) * 0.10

#Calcular el IVA (16% del subtotal de todos los productos)
iva = sum(producto["precio"] * producto["cantidad"] for producto in lista_productos) * 0.16

#Calcular el total final
total_final = sum(producto["precio"] * producto["cantidad"] for producto in lista_productos) + iva - subsidio_total

#Seccion 4: Impresion del recibo:
print("\nRecibo de compra:")
for producto in lista_productos:
    print(f"Producto: {producto['nombre']}, Precio: ${producto['precio']:.2f}, Cantidad: {producto['cantidad']}, Subtotal: ${producto['precio'] * producto['cantidad']:.2f}")
print(f"\nSubsidio total: ${subsidio_total:.2f}")
print(f"IVA: ${iva:.2f}")
print(f"Total final: ${total_final:.2f}")
print(f"\n¡Gracias por su compra! Vuelva pronto.")