# Crear una lista tupla y rango con numeros del uno al 10
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
rango = range(1, 10)

print(lista, tupla, rango)

# Andree - Sintaxis de diccionario
persona = {
  "nombre": "Pablo",
  "apellido": "no se",
  "edad": "desconocida"
}
print( persona["apellido"], persona["edad"], persona["nombre"])


# Andree - Crea un conjunto

un_set = set([1,2,3,4,5])
otro_set = frozenset(un_set)
print(un_set, otro_set)


#Andree - f-strings