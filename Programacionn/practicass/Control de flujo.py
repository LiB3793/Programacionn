#temperatura = float(input("Ingrese la temperatura: "))

#if temperatura <10: 
   # print("Hace frío")
#elif temperatura <25: 
    #print("Es templado")
#else:
    #print("Hace calor")  


cantidad = input("Ingrese la cantidad: ")
cantidad = int(cantidad)

if cantidad > 100:
    descuento = cantidad * 0.20
    total = cantidad - descuento
    print("20% de descuento")
    print("Total a pagar:", total)

elif cantidad > 50:
    descuento = cantidad * 0.10
    total = cantidad - descuento
    print("10% de descuento")
    print("Total a pagar:", total)

else:
    print("No hay descuento")
    print("Total a pagar:", cantidad)