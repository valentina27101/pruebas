# Es una funcion que sirve para contar cuantos elementos hay en algo
len
numeros =[1,2,3,4]
print(len(numeros))

# Importa un dato a main
from menu import mostrar_menu

# Cuando defina una funcion poner a usarla al final con su nombre y ()
def main():
    while True:
        mostrar_menu() 
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("Agregar producto")

        elif opcion == "3":
            break

main()
