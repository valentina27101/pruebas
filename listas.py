#listas

my_list = ['python', 53, False]
print(type(my_list))

print(my_list)
print(my_list[2])

#.append (agrega un objeto a la lista)

my_list.append('43')
print(my_list)

#.insert (agrega un objeto pero decidimos en que lugar ponerlo)
my_list.insert(3,'hola')
print(my_list)

#.remove (remueve lo que le digamos)
my_list.remove('hola')
print(my_list)

#.pop (remueve en la posicion q digamos)
print(my_list.pop(3)) #con el print nos devuelve el valor que borro
print(my_list)

#.reverse (pone la lista al reves)
my_list.reverse()
print(my_list)

#.clear (borra toda la lista)
my_list.clear()
print(my_list)

#.index busca la posicion de el producto
my_list.index()
print(my_list)

#conjuntos puedes ser modificados, pero no permiten duplicados 
frutas = {"manzana", "pera", "pera"}
print(frutas)
