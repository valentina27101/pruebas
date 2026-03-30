def agregar_producto(inventario, nombre, precio, cantidad):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)

inventario = []

nombre = input("Nombre del producto: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

agregar_producto(inventario, nombre, precio, cantidad)

print(inventario)
