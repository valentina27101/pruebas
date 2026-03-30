def buscar(nombre):
    if nombre == "Vale":
        return "Encontrado"
    return "No está"

def buscar_producto(inventario, nombre):
    for producto in inventario:
        if producto["nombre"] == nombre:
            return producto
    return None
# en main
nombre = input("Producto a buscar: ")
resultado = buscar_producto(inventario, nombre)

if resultado:
    print("Encontrado:", resultado)
else:
    print("No existe")
