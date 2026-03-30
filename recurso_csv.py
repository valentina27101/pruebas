def usuario_nuevo():
    import csv
    import os

    # Nombre del archivo CSV
    archivo_csv = "usuarios.csv"

    # Pedir datos al usuario
    nombre = input("Ingrese su primer nombre: ")
    apellido = input("Ingrese su primer apellido: ")
    cedula = input("Ingrese su número de cédula: ")
    while True:
            pin = input("Ingrese un PIN de 4 dígitos: ")

            if len(pin) != 4:
                print("El PIN debe tener exactamente 4 dígitos. Por favor, inténtelo de nuevo.")
            elif not pin.isdigit():
                print("El PIN debe contener solo dígitos. Por favor, inténtelo de nuevo.")
            else:
                print(f"Gracias {nombre} {apellido}, su cuenta ha sido registrada exitosamente.")
                break


    # Verificar si el archivo ya existe
    archivo_existe = os.path.isfile(archivo_csv)

    # Abrir el archivo en modo 'a' (agregar)
    with open(archivo_csv, "a", newline="", encoding="utf-8") as archivo:
            campos = ["Nombre", "Apellido", "Cédula", "PIN"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            # Si el archivo no existía, escribir encabezado
            if not archivo_existe:
                escritor.writeheader()
            
            # Escribir los datos del usuario
            escritor.writerow({"Nombre": nombre, "Apellido": apellido, "Cédula": cedula, "PIN": pin })

usuario_nuevo()
