#las claves van siempre en comillas

persona = { 
    "nombre":'pablo',
    "edad": 18,
    "cuidad":'barranquilla' 
}

#mostrar diccionario
print(persona)

#para mostrar un valor en especifico
print(persona["nombre"])

#modificar un valor del diccionario
persona["edad"] = 30
print(persona)

#añadir algo al diccionario
persona["profesion"] = 'medico'
print(persona)

#eliminar algo del diccionario
del persona["cuidad"]
print(persona)

#iterar por las claves
for clave in persona:
    print(clave)

#iterar por valores 
for valor in persona.values():
    print(valor)

#iterar o acceder a las claves y valores
for clave, valor in persona.items():
    print(clave, valor)
