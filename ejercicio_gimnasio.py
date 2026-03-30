import json
import os

# Archivo para persistencia
ARCHIVO = "clientes.json"

# Lista global para guardar clientes
clientes = []

# -------------------- Funciones --------------------

# Cargar datos desde JSON
def cargar_datos():
    global clientes
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            clientes = json.load(f)

# Guardar datos en JSON
def guardar_datos():
    with open(ARCHIVO, "w") as f:
        json.dump(clientes, f, indent=4)

# Validar ID único y 4 dígitos
def pedir_id():
    while True:
        id_cliente = input("Ingrese ID (4 dígitos): ")
        if id_cliente.isdigit() and len(id_cliente) == 4:
            if any(c["id"] == id_cliente for c in clientes):
                print("Error: ID ya existe")
            else:
                return id_cliente
        else:
            print("Error: debe ser un número de 4 dígitos")

# Validar edad
def pedir_edad():
    while True:
        edad = input("Ingrese edad: ")
        if edad.isdigit():
            edad = int(edad)
            if 12 < edad <= 100:
                return edad
            else:
                print("Error: edad fuera de rango (13-100)")
        else:
            print("Error: solo se permiten números")

# Validar plan
def pedir_plan():
    while True:
        print("Tipos de plan:")
        print("1. Mensual")
        print("2. Trimestral")
        print("3. Anual")
        opcion = input("Seleccione plan (1-3): ")
        if opcion == "1":
            return "Mensual"
        elif opcion == "2":
            return "Trimestral"
        elif opcion == "3":
            return "Anual"
        else:
            print("Opción inválida")

# Validar estado
def pedir_estado():
    while True:
        estado = input("Estado (activo/inactivo): ").lower()
        if estado in ["activo", "inactivo"]:
            return estado
        else:
            print("Error: solo 'activo' o 'inactivo'")

# Crear cliente
def crear_cliente():
    print("\n--- Crear Cliente ---")
    cliente = {}
    cliente["id"] = pedir_id()
    cliente["nombre"] = input("Ingrese nombre: ").title()
    cliente["edad"] = pedir_edad()
    cliente["plan"] = pedir_plan()
    cliente["estado"] = pedir_estado()
    clientes.append(cliente)
    guardar_datos()
    print("Cliente creado exitosamente.\n")

# Listar clientes
def listar_clientes():
    if not clientes:
        print("No hay clientes registrados.\n")
        return
    print("\n--- Lista de Clientes ---")
    for c in clientes:
        print(f"ID: {c['id']}, Nombre: {c['nombre']}, Edad: {c['edad']}, Plan: {c['plan']}, Estado: {c['estado']}")
    print()

# Buscar cliente por ID o nombre
def buscar_cliente():
    busqueda = input("Ingrese ID o nombre a buscar: ").lower()
    encontrados = [c for c in clientes if c["id"] == busqueda or c["nombre"].lower() == busqueda]
    if encontrados:
        print("\n--- Cliente(s) encontrado(s) ---")
        for c in encontrados:
            print(f"ID: {c['id']}, Nombre: {c['nombre']}, Edad: {c['edad']}, Plan: {c['plan']}, Estado: {c['estado']}")
    else:
        print("No se encontraron clientes.\n")

# Actualizar cliente
def actualizar_cliente():
    id_buscar = input("Ingrese ID del cliente a actualizar: ")
    for c in clientes:
        if c["id"] == id_buscar:
            print(f"Actualizando cliente: {c['nombre']}")
            c["nombre"] = input(f"Nombre [{c['nombre']}]: ") or c['nombre']
            c["edad"] = pedir_edad()
            c["plan"] = pedir_plan()
            c["estado"] = pedir_estado()
            guardar_datos()
            print("Cliente actualizado.\n")
            return
    print("Cliente no encontrado.\n")

# Eliminar cliente
def eliminar_cliente():
    id_buscar = input("Ingrese ID del cliente a eliminar: ")
    for i, c in enumerate(clientes):
        if c["id"] == id_buscar:
            confirmar = input(f"Confirma eliminar a {c['nombre']}? (s/n): ").lower()
            if confirmar == "s":
                clientes.pop(i)
                guardar_datos()
                print("Cliente eliminado.\n")
            else:
                print("Operación cancelada.\n")
            return
    print("Cliente no encontrado.\n")

# -------------------- Menú Principal --------------------
def menu():
    cargar_datos()
    while True:
        print("=== Sistema de Gestión de Clientes ===")
        print("1. Crear cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Actualizar cliente")
        print("5. Eliminar cliente")
        print("6. Salir")
        opcion = input("Seleccione opción: ")
        
        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            actualizar_cliente()
        elif opcion == "5":
            eliminar_cliente()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente nuevamente.\n")

# Ejecutar programa
if __name__ == "__main__":
    menu()
